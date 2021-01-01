import sys

import pygame
from pygame.locals import *

from Python.DeathAngelCardGame.Main.GameObjects.space_marine import SpaceMarine

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
FPS = 60

BLACK = (0, 0, 0)
BLUE = (0, 0, 155)

BORDERCOLOR = BLUE
BGCOLOR = BLACK


def main():
    global FPSCLOCK, DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Death Angel')
    run_game()


def run_game():
    render_update_group = pygame.sprite.RenderUpdates()
    SpaceMarine.containers = render_update_group

    first_test_sprite = SpaceMarine('Main\SpriteImages/chaplain_raziel.png')
    second_test_sprite = SpaceMarine('Main\SpriteImages/brother_metraen.png')
    third_test_sprite = SpaceMarine('Main\SpriteImages/brother_zael.png')
    forth_test_sprite = SpaceMarine('Main\SpriteImages/brother_omnio.png')

    first_test_sprite.set_position(400, 52)
    second_test_sprite.set_position(400, 172)
    third_test_sprite.set_position(400, 292)
    forth_test_sprite.set_position(400, 412)

    space_marine_sprite_list = [first_test_sprite, second_test_sprite, third_test_sprite, forth_test_sprite]

    background = DISPLAYSURF.copy()
    background.fill(BLACK)

    selected_space_marine = None

    while True:
        DISPLAYSURF.blit(background, (0, 0))
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR,
                         (394, 50, 250, 485), 5)

        checkForQuit()
        for event in pygame.event.get():  # event handling loop
            if event.type == MOUSEBUTTONUP:
                x_click_position, y_click_position = event.pos
                first_test_sprite.check_if_facing_arrow_clicked(x_click_position, y_click_position)
                if selected_space_marine is not None:
                    selected_space_marine = None
            if event.type == MOUSEBUTTONDOWN:
                x_click_position, y_click_position = event.pos
                is_mouse_over_a_space_marine(space_marine_sprite_list, x_click_position, y_click_position)
                selected_space_marine = get_selected_space_marine(space_marine_sprite_list)
            if event.type == MOUSEMOTION:
                x_click_position, y_click_position = event.pos
                if selected_space_marine is not None:
                    selected_space_marine.set_position(x_click_position, y_click_position)

        # clear all the sprites
        render_update_group.clear(DISPLAYSURF, background)

        # update all the sprites
        render_update_group.update()
        first_test_sprite.get_arrow_containers().update()

        dirty = render_update_group.draw(DISPLAYSURF)
        dirty_arrows = first_test_sprite.get_arrow_containers().draw(DISPLAYSURF)
        pygame.display.update(dirty)
        pygame.display.update(dirty_arrows)

        FPSCLOCK.tick(FPS)


def terminate():
    '''Terminates games.'''
    pygame.quit()
    sys.exit()


def is_a_space_marine_selected(space_marine_list):
    for space_marine in space_marine_list:
        if space_marine.get_is_selected():
            return True
    return False


def is_mouse_over_a_space_marine(space_marine_list, x_mouse_position, y_mouse_position):
    for space_marine in space_marine_list:
        if space_marine.get_rect().collidepoint(x_mouse_position, y_mouse_position):
            space_marine.set_is_selected(True)
            break


def get_selected_space_marine(space_marine_list):
    for space_marine in space_marine_list:
        if space_marine.get_is_selected():
            return space_marine


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate  if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
