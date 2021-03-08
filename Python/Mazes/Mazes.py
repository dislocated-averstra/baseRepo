import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
GRAY = (185, 185, 185)
FPS = 60



def main():
    global FPSCLOCK, DISPLAYSURF

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FPSCLOCK = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Mazes')
    run_game()

def run_game():
    while True:
        checkForQuit()
        DISPLAYSURF.fill(GRAY)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back

if __name__ == '__main__':
    main()
