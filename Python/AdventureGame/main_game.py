# main build the window and start the program
import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 1680
WINDOWHEIGHT = 1050

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Main Game')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        pygame.display.update()

def terminate():
    '''Terminates games.'''
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()