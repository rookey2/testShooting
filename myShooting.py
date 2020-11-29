import pygame
import sys
from time import sleep

BLACK = (0, 0, 0)
WINDOWS_HEIGHT = 640;
WINDOWS_WIDTH = 480;

def initGame() :
    global gamePad, clock
    pygame.init()
    gamePad = pygame.display.set_mode( (WINDOWS_WIDTH, WINDOWS_HEIGHT))
    pygame.display.set_caption('PyShooting')
    clock = pygame.time.Clock()


def runGame() :
    global gamePad, clock
    onGame = False;
    while not onGame:
        for event in pygame.event.get() :
            if event.type in [pygame.QUIT] :
                pygame.quit()
                sys.exit()

        gamePad.fill(BLACK)
        pygame.display.update();
        clock.tick(60)
    pygame.quit()


initGame()
runGame()




