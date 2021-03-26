import sys

import pygame
from pygame.locals import *

from Python.DeathAngelCardGame.Main.GameObjects.dice_sprite import DiceSprite
from Python.DeathAngelCardGame.Main.Menus.game_menu import Game_Menu
from Python.DeathAngelCardGame.Main.Utils.game_utils import *

WINDOWWIDTH = 1360
WINDOWHEIGHT = 768
CARDHEIGHT = 120
CARDWIDTH = 240
SCREENRECT = pygame.Rect(0, 0, 1360, 768)
FPS = 60

BLACK = (0, 0, 0)
BLUE = (0, 0, 155)

BORDERCOLOR = BLUE
BGCOLOR = BLACK


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    fullscreen = False
    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    DISPLAYSURF = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 40)
    pygame.display.set_caption('Death Angel')
    run_game()


def run_game():
    render_update_group = pygame.sprite.RenderUpdates()
    SpaceMarine.containers = render_update_group
    DiceSprite.containers = render_update_group
    Game_Menu.containers = render_update_group

    space_marine_list = init_game()
    y_position = 25
    for space_marine in space_marine_list:
        space_marine.set_position(int((WINDOWWIDTH / 2) - 60), y_position)
        y_position += 120

    roll_surf, roll_rect = makeTextObjs('ROLL', BASICFONT, BLUE)
    menu_text, menu_rect = makeTextObjs('MENU', BASICFONT, BLUE)

    dice = DiceSprite()
    game_menu = None

    background = DISPLAYSURF.copy()
    background.fill(BLACK)

    selected_space_marine = None

    while True:
        DISPLAYSURF.blit(background, (0, 0))
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR,
                         (int((WINDOWWIDTH / 2) - 65), 20, 250, 730), 5)

        roll_rect.topleft = (0, 32)
        DISPLAYSURF.blit(roll_surf, roll_rect)

        menu_rect.topleft = (WINDOWWIDTH - 130, 0)
        DISPLAYSURF.blit(menu_text, menu_rect)

        checkForQuit()
        for event in pygame.event.get():  # event handling loop
            if event.type == MOUSEBUTTONUP:
                if selected_space_marine is not None:
                    selected_space_marine.set_is_selected(False)
                    selected_space_marine = None
            if event.type == MOUSEBUTTONDOWN:
                # at this point we set the starting mouse position
                previous_x_mouse_position, previous_y_mouse_position = event.pos
                is_mouse_over_a_space_marine(space_marine_list, previous_x_mouse_position,
                                             previous_y_mouse_position)
                selected_space_marine = get_selected_space_marine(space_marine_list)
                if roll_rect.collidepoint(event.pos) and not dice.is_dice_rolling:
                    dice.roll_dice()

                elif menu_rect.collidepoint(event.pos):
                    game_menu = Game_Menu(WINDOWHEIGHT, WINDOWWIDTH)
                    DISPLAYSURF.blit(game_menu.get_menu_surface(), game_menu.get_menu_rect())

                elif game_menu is not None and game_menu.is_quit_button_clicked(event.pos):
                    terminate()

            if event.type == MOUSEMOTION:
                x_click_position, y_click_position = pygame.mouse.get_pos()
                if selected_space_marine is not None:
                    selected_space_marine.move_relative_to_mouse_movement(
                        int(previous_x_mouse_position - x_click_position),
                        int(previous_y_mouse_position - y_click_position))
                    previous_x_mouse_position = x_click_position
                    previous_y_mouse_position = y_click_position



        # clear all the sprites
        render_update_group.clear(DISPLAYSURF, background)

        # update all the sprites
        render_update_group.update()

        dirty = render_update_group.draw(DISPLAYSURF)

        pygame.display.update(dirty)

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
