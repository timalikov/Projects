import pygame       #needed libraries
import random
import time
from datetime import datetime as dt
from colors import colors


class Game2048:                 
    def __init__(self) -> None:
        pygame.init()           #pygame initialization


        self.score = 0          #initializing needed variables
        self.N = 4              #number of blocks => current 4x4. I used it to change the number of blocks depending on difficulty level
        self.cellSize = 80      
        self.gap = 5
        self.blockSize = self.cellSize + self.gap * 2
        self.font = pygame.font.SysFont("Arial", 24)
        self.game_over = False
        self.saved_h_score = 0
        self.when_high_scored = ''
        with open("high_score.txt", 'r') as f:      #read highest score from .txt file
            try:                                    #if not recorded yet or null, default high score = 0
                self.saved_h_score = int(f.readline())
                self.when_high_scored = f.readline()
            except:
                self.saved_h_score = 0
            
        self.high_score = self.saved_h_score
        self.board = [[0 for _ in range(self.N)] for _ in range(self.N)]    #create board

        self.windowWidth = self.blockSize * self.N                     #initialize frame sizes
        self.windowHeight = self.windowWidth + 100

        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption("2048")

        self.fps = 60                       #initialize frames per second to limit frame rate
        self.timer = pygame.time.Clock()            

    def new_value(self):                    #method for creating random 2's or 4's
        added = False
        while any(0 in row for row in self.board) and added == False:   #while we have space for them
            r = random.randint(0, self.N - 1)                    #pick random places for row and column
            c = random.randint(0, self.N - 1)
            if self.board[r][c] == 0:                       #if empty(equals to 0) add a value
                added = True
                if random.randint(1, 10) == 10:             #1 of 10 chance to creting 4 valued block
                    self.board[r][c] = 4
                else:
                    self.board[r][c] = 2                
        if added:               #return False or True to know whether value is added or not
            return False        #if not then we don't have space for new value and Game is over
        else:
            return True
        
    def draw_details(self):       #method for displaiyng scores
        font_name = pygame.font.get_default_font()                  
        text_font = pygame.font.Font(font_name, 4 * self.N)     # using * self.N to make the text little responsive according to blocks' sizes
        score_text = text_font.render(f'Score: {self.score}', True, 'black')
        high_score_text = text_font.render(f'High Score: {self.high_score}', True, 'black')
        small_text_font = pygame.font.Font(font_name, 3 * self.N)
        when_high_scored_text = small_text_font.render(f'When:{self.when_high_scored}', True, 'black')
        self.window.blit(score_text, (10, self.windowHeight - 90 + (10 * (self.N - 4))))    #decided to use height as starting point and (10 * (self.N - 4)) is also to make responsive layout 
        self.window.blit(high_score_text, (10,  self.windowHeight - 60 + (10 * (self.N - 4))))
        self.window.blit(when_high_scored_text, (15, self.windowHeight - 40 + (10 * (self.N - 4))))

    def draw_game_over(self):   #game over message
        pygame.draw.rect(self.window, 'black', [50 , 50, 300 + (100 * (self.N - 4)), 100 + (10 * (self.N - 4))], 0, 10)  #немного криво получилось, но не стал на это тратить время
        font = pygame.font.Font(pygame.font.get_default_font(), 24 + (6 * (self.N - 4)))    #same logic as in the previous method
        game_over_text1 = font.render('Game Over!', True, 'white')
        game_over_text2 = font.render('Press Enter to Restart', True, 'white')
        self.window.blit(game_over_text1, (130, 65))
        self.window.blit(game_over_text2, (70, 105))

    def game_over_save(self):       #method for storing the high score to a .txt file
        # self.draw_game_over()
        if self.high_score > self.saved_h_score:
            file = open("high_score.txt", "w")
            # Write the score value to the first line
            file.write(str(self.high_score) + "\n")
            # Write the current datetime to the next line
            formatted_datetime = dt.now().strftime("%d.%m.%Y, %H:%M")
            file.write(str(formatted_datetime) + "\n")
            # Close the file
            file.close()


    def drawBoard(self):                #main display drawing
        self.window.fill(colors['bg'])  

        for r in range(self.N):
            rectY = self.blockSize * r + self.gap       
            for c in range(self.N):
                rectX = self.blockSize * c + self.gap    #initializing the starting points of blocks

                value = self.board[r][c]        
                if value > 8:
                    value_color = colors['light text']  #get value and if it is more than 8 make it bright
                else:
                    value_color = colors['dark text']

                if value <= 2048:
                    color = colors[value]       #get color by value
                else:
                    color = colors['other']     #if more than 2048 then we don't need any colors 

                pygame.draw.rect(
                    self.window,
                    color,
                    pygame.Rect(rectX, rectY, self.cellSize, self.cellSize)     #draw each cell
                )

                if value > 0:
                    value_len = len(str(value))
                    self.font = pygame.font.Font(pygame.font.get_default_font(), 48 - (5 * value_len))    #depending on value length font size changes to fit the cell size
                    value_text = self.font.render(str(value), True, value_color)
                    text_rect = value_text.get_rect(center = (self.blockSize * c + self.gap + self.cellSize/2, self.blockSize * r + self.gap + self.cellSize/2))  #place value to the center of cell
                    self.window.blit(value_text, text_rect)

    def take_turn(self, direc):     #Challenging part/ creating the logic and execution of each turn
        merged = [[False for _ in range(self.N)] for _ in range(self.N)]       #list that keeps track what pieces has merged. current : nothing is merged
        if direc == 'UP':
            for i in range(1, self.N):      #start from second row because don't need to move up first row
                for j in range(self.N):
                    shift = 0               
                    for q in range(i):      #count how many shifts need to do till the value
                        if self.board[q][j] == 0:
                            shift += 1
                    if shift > 0:           
                        self.board[i - shift][j] = self.board[i][j]  #move current piece up to needed place
                        self.board[i][j] = 0                         #empty current piece's
                    if self.board[i - shift - 1][j] == self.board[i - shift][j] and not merged[i - shift][j] \
                        and not merged[i - shift - 1][j]:       #if new piece and piece right above are equal
                        self.board[i - shift - 1][j] *= 2       #then double it's value
                        self.score += self.board[i - shift - 1][j]      #add its value to track the score
                        self.board[i - shift][j] = 0            
                        merged[i - shift - 1][j] = True
        elif direc == 'DOWN':
            for i in range(self.N - 1):  #don't need to move down last row
                for j in range(self.N):
                    shift = 0
                    for q in range(i + 1):      #same logic: count number of shifts and shift
                        if self.board[self.N - 1 - q][j] == 0:
                            shift += 1
                    if shift > 0:
                        self.board[self.N - 2 - i + shift][j] = self.board[self.N - 2 - i][j]
                        self.board[self.N - 2 - i][j] = 0
                    if self.N - i + shift <= self.N:
                        if self.board[self.N - 2 - i + shift][j] == self.board[self.N - 1 - i + shift][j] and not merged[self.N - 1 - i + shift][j] \
                                and not merged[self.N - 2 - i + shift][j]:
                            self.board[self.N - 1 - i + shift][j] *= 2
                            self.score += self.board[self.N - 1 - i + shift][j]
                            self.board[self.N - 2 - i + shift][j] = 0
                            merged[self.N - 1 - i + shift][j] = True
        elif direc == 'LEFT':
            for i in range(self.N):
                for j in range(self.N):
                    shift = 0
                    for q in range(j):
                        if self.board[i][q] == 0:
                            shift += 1
                    if shift > 0:
                        self.board[i][j - shift] = self.board[i][j]
                        self.board[i][j] = 0
                    if self.board[i][j - shift] == self.board[i][j - shift - 1] and not merged[i][j - shift - 1] \
                            and not merged[i][j - shift]:
                        self.board[i][j - shift - 1] *= 2
                        self.score += self.board[i][j - shift - 1]
                        self.board[i][j - shift] = 0
                        merged[i][j - shift - 1] = True
        elif direc == 'RIGHT':
            for i in range(self.N):
                for j in range(self.N):
                    shift = 0
                    for q in range(j):
                        if self.board[i][self.N - 1 - q] == 0:
                            shift += 1
                    if shift > 0:
                        self.board[i][self.N - 1 - j + shift] = self.board[i][self.N - 1 - j]
                        self.board[i][self.N - 1 - j] = 0
                    if self.N - j + shift <= self.N - 1:
                        if self.board[i][self.N - j + shift] == self.board[i][self.N - 1 - j + shift] and not merged[i][self.N - j + shift] \
                                and not merged[i][self.N - 1 - j + shift]:
                            self.board[i][self.N - j + shift] *= 2
                            self.score += self.board[i][self.N - j + shift]
                            self.board[i][self.N - 1 - j + shift] = 0
                            merged[i][self.N - j + shift] = True       

    def draw_levels(self):      #method for drawing the level buttons
        easy = self.draw_button(150, 170, "Easy",color='green')
        medium = self.draw_button(150, 200, "Medium",color='orange')
        hard = self.draw_button(150, 230, "Hard")
        return easy, medium, hard

    def draw_button(self, x, y, text, color = 'red', text_pos_x = 5, text_pos_y = 13):  #method for drawing any button, has default values and we can change them if needed
        rec = pygame.Rect(x + (70 * (self.N - 3)), y + (100 * (self.N - 3)), 100, 40)   
        pygame.draw.rect(self.window, color, rec)
        button_font = pygame.font.Font(pygame.font.get_default_font(), 9 if self.N == 3 else 14)    #if we have 3x3 cells use 9 for font size, otherwise 14
        button_text = button_font.render(text, True, (255, 255, 255))
        self.window.blit(button_text, (x + text_pos_x + (70 * (self.N - 3)), y + text_pos_y + (100 * (self.N - 3))))
        return rec
    
    def set_mode(self, n):      #method for chaning the number of blocks depending on difficulty level
        self.N = n
        self.windowWidth = self.blockSize * self.N
        self.windowHeight = self.windowWidth + 100
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.board = [[0 for _ in range(self.N)] for _ in range(self.N)]
    

    def play(self):         #make the game work
        self.timer.tick(self.fps)       #frames per second
        running = True          
        just_started = True
        need_new = True
        direction = ''
        possible_directions = ['UP', 'DOWN', 'RIGHT', 'LEFT']
        bot_is_playing = False
        dif_button_clicked = False
        popup_img = pygame.image.load("on_fire_100.jpg")
        popup_image_100 = pygame.transform.scale(popup_img, (200 + (200 * (self.N - 3)), 200 + (200 * (self.N - 3))))
        popup_displayed_100 = False

        #game loop
        while running:      #do all needed drawings
            self.drawBoard()
            self.draw_details()
            dif_levels_button = self.draw_button(150, 270, "Difficulty", (155, 0, 0), text_pos_x = 15)

            if dif_button_clicked:  #show difficulty levels if dif_button clicked
                bot_is_playing = False     #stop the bot to let the user pick the difficulty
                easy_button, medium_button, hard_button = self.draw_levels()

            if not bot_is_playing:      #button variants depending on what is clicked
                bot_play_button = self.draw_button(150, 310, "Bot will play")
            else:
                bot_play_button = self.draw_button(150, 310, "Bot is playing")

            if need_new:    #create random values on empty cells
                if just_started:        #create 2 (1 extra) of them at start
                    self.game_over = self.new_value()   #check every time when generating random values if there is space otherwise game is over
                    just_started = False                
                self.game_over = self.new_value()
                need_new = False    

            if bot_is_playing:      #bot chooses random directions and plays instead of user
                direction = random.choice(possible_directions)
                time.sleep(0.3)     #to make the bot go little slower
                self.take_turn(direction)
                direction = ''
                need_new = True
            else:
                if direction != '':     #user's choice to make a turn
                    self.take_turn(direction)
                    direction = ''
                    need_new = True     #generate new value after turn

            if self.game_over == True:      #game over display if there is no space for new values
                self.draw_game_over()
                self.game_over_save()
                

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    self.game_over_save()
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:     
                    if event.button == 1:                   #if clicked left side of mouse
                        mouse_pos = pygame.mouse.get_pos()
                        if bot_play_button.collidepoint(mouse_pos): #if mouse click position was on bot_play_button
                            if not bot_is_playing:                  #make bot play
                                bot_is_playing = True
                            else:
                                bot_is_playing = False
                        elif dif_levels_button.collidepoint(mouse_pos):     #show difficulty levels
                            if dif_button_clicked:
                                dif_button_clicked = False
                            else:
                                dif_button_clicked = True
                        elif dif_button_clicked and easy_button.collidepoint(mouse_pos):    #change the mode according to dif_levels
                            if self.N != 5:                    #and start a new game after changing difficulty
                                self.set_mode(5)
                                need_new = True
                                just_started = True
                                self.score = 0
                                direction = ''
                                self.game_over = False
                        elif dif_button_clicked and medium_button.collidepoint(mouse_pos):
                            if self.N != 4:
                                self.set_mode(4)
                                need_new = True
                                just_started = True
                                self.score = 0
                                direction = ''
                                self.game_over = False
                        elif dif_button_clicked and hard_button.collidepoint(mouse_pos):
                            if self.N != 3:
                                self.set_mode(3)
                                need_new = True
                                just_started = True
                                self.score = 0
                                direction = ''
                                self.game_over = False

                if event.type == pygame.KEYDOWN:        #keyboard commands from user
                    if event.key == pygame.K_UP:
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN:
                        direction = 'DOWN'
                    elif event.key == pygame.K_RIGHT:
                        direction = 'RIGHT'
                    elif event.key == pygame.K_LEFT:
                        direction = 'LEFT'
                    elif event.key == pygame.K_ESCAPE:
                        self.game_over_save()
                        running = False
                    if self.game_over:              
                        if event.key == pygame.K_RETURN:      #Start a new game after Enter is clicked
                            self.board = [[0 for _ in range(self.N)] for _ in range(self.N)]
                            need_new = True
                            just_started = True
                            self.score = 0
                            direction = ''
                            self.game_over = False
            
            if self.score > self.high_score:    #if reached the high score set the new one
                self.high_score = self.score
                self.when_high_scored = dt.now().strftime("%d.%m.%Y, %H:%M")    #with date formatted to dd.mm.yyyy, hh:mm

            if self.score > 100 and not popup_displayed_100:        #extra feature that shows funny/incouraging image when hitting 100 score
                popup_displayed_100 = True
                popup_timer_start = time.time()         #start the timer

            if popup_displayed_100 and time.time() - popup_timer_start <= 1:    #and disappear after 1 second
                self.window.blit(popup_image_100, (0, 0))    
            
            pygame.display.flip()




if __name__ == "__main__":      #make an instance of the class
    game = Game2048()           #start the game <3
    game.play()
    pygame.quit()
