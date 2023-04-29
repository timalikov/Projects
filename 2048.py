import pygame

class Game2048:
    def __init__(self) -> None:
        self.N = 4
        self.cellSize = 100
        self.gap = 5
        self.windowBgColor = (187, 173, 160)
        self.blockSize = self.cellSize + self.gap * 2

        self.windowWidth = self.blockSize * 4
        self.windowHeight = self.windowWidth

        pygame.init()

        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption("2048")

    def drawBoard(self):
        self.window.fill(self.windowBgColor)

        for r in range(self.N):
            rectY = self.blockSize * r + self.gap
            for c in range(self.N):
                rectX = self.blockSize * c + self.gap

                pygame.draw.rect(
                    self.window,
                    (0,0,0),
                    pygame.Rect(rectX, rectY, self.cellSize, self.cellSize)
                )

    def play(self):
        running = True
        while running:
            self.drawBoard()
            pygame.display.update()

if __name__ == "__main__":
    game = Game2048()
    game.play()