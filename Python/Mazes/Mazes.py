import sys

import pygame
from pygame.locals import *

from Python.Mazes.GameObject.maze_container import MazeContainer

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
GRAY = (185, 185, 185)
LIGHTRED = (175, 20, 20)
FPS = 60


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FPSCLOCK = pygame.time.Clock()
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption('Mazes')
    showStartScreen()
    run_game()


def run_game():
    # create the render group that is going to hold all the sprite for the time being
    render_update_group = pygame.sprite.RenderUpdates()
    MazeContainer.containers = render_update_group

    maze = MazeContainer()
    maze.set_position(300, 300)

    while True:
        checkForQuit()
        DISPLAYSURF.fill(GRAY)

        # clear all the sprites
        render_update_group.clear(DISPLAYSURF, DISPLAYSURF)

        # update all the sprites
        render_update_group.update()

        dirty = render_update_group.draw(DISPLAYSURF)

        pygame.display.update(dirty)
        FPSCLOCK.tick(FPS)




def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    checkForQuit()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None


def showStartScreen():
    titleSurf, titleRect = makeTextObjs('Mazes', BIGFONT, LIGHTRED)
    titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)

    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, LIGHTRED)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
