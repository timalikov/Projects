import pygame
from colors import colors

class Game2048:
    def __init__(self) -> None:

        pygame.init()

        self.N = 4
        self.cellSize = 100
        self.gap = 5
        self.blockSize = self.cellSize + self.gap * 2
        self.font = pygame.font.SysFont("Arial", 36)
        self.board = [
            [0, 0, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 2, 0],
            [0, 0, 2, 0],
        ]

        self.windowWidth = self.blockSize * 4
        self.windowHeight = self.windowWidth + 100


        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption("2048")

        self.fps = 60
        self.timer = pygame.time.Clock()

    def drawBoard(self):
        self.window.fill(colors['bg'])

        for r in range(self.N):
            rectY = self.blockSize * r + self.gap
            for c in range(self.N):
                rectX = self.blockSize * c + self.gap

                value = self.board[r][c]
                if value > 8:
                    value_color = colors['light text']
                else:
                    value_color = colors['dark text']

                if value <= 2048:
                    color = colors[value]
                else:
                    color = colors['other']

                pygame.draw.rect(
                    self.window,
                    color,
                    pygame.Rect(rectX, rectY, self.cellSize, self.cellSize)
                )

                if value > 0:
                    value_len = len(str(value))
                    self.font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                    value_text = self.font.render(str(value), True, value_color)
                    text_rect = value_text.get_rect(center = (self.blockSize * c + self.gap, self.blockSize * r + self.gap))
                    self.window.blit(value_text, text_rect)


    def play(self):
        self.timer.tick(self.fps)    
        running = True
        while running:
            self.drawBoard()
            pygame.display.update()

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("U")
                        print(colors[0])
                    elif event.key == pygame.K_DOWN:
                        print("D")
                    elif event.key == pygame.K_RIGHT:
                        print("R")
                    elif event.key == pygame.K_LEFT:
                        print("L")

if __name__ == "__main__":
    game = Game2048()
    game.play()
    pygame.quit()
