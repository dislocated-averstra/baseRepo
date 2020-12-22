# main build the window and start the program


import sys
import pygame
from pygame.locals import *
from GameObject.game_enemy import *
from GameObject.game_player import *
from GameBoard.game_board import *

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (21, 156, 75)
GRAY = (185, 185, 185)
WHITE = (255, 255, 255)

TEXTSHADOWCOLOR = GRAY
TEXTCOLOR = WHITE

PLAYER_SIZE = 20
BGCOLOR = DARKGREEN
FPS = 60

DIRECTIONS = ['LEFT', 'RIGHT', ' UP', 'DOWN']


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, player, enemy, board, BIGFONT

    player = Player(502, 374, PLAYER_SIZE)
    enemy = Enemy(0, 0)
    board = GameBoard(int(WINDOWWIDTH / 32), int(WINDOWHEIGHT / 32))
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BIGFONT = pygame.font.Font('freesansbold.ttf', 40)
    pygame.display.set_caption('Main Game')
    run_game()


def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def run_game():
    '''The main code for the game I expect we will refactor this several times as we go'''
    while True:
        checkForQuit()
        for event in pygame.event.get():
            if event.type == KEYUP:  # a person let go of the key
                if event.key in (K_a, K_LEFT):
                    player.remove_horizontal_direction('LEFT')
                if event.key in (K_d, K_RIGHT):
                    player.remove_horizontal_direction('RIGHT')
                if event.key in (K_w, K_UP):
                    player.remove_vertical_direction('UP')
                if event.key in (K_s, K_DOWN):
                    player.remove_vertical_direction('DOWN')
            if event.type == KEYDOWN:  # a person is pressed or is pressing a key
                if event.key in (K_a, K_LEFT):
                    player.add_horizontal_direction('LEFT')
                if event.key in (K_d, K_RIGHT):
                    player.add_horizontal_direction('RIGHT')
                if event.key in (K_w, K_UP):
                    player.add_vertical_direction('UP')
                if event.key in (K_s, K_DOWN):
                    player.add_vertical_direction('DOWN')

        check_for_enemy_player_overlap(player.get_x_position(), player.get_y_position(), enemy.get_x_position(), enemy.get_y_position())
        board.add_to_board(0, 'brick')
        brick_wall = pygame.image.load('gameSprites/BrickWall.png')
        player.move_player(WINDOWHEIGHT, WINDOWWIDTH)
        enemy.move_enemy(player.get_x_position(), player.get_y_position())
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(brick_wall, (0, 0))
        draw_player_icon(player.get_x_position(), player.get_y_position(), PLAYER_SIZE, PLAYER_SIZE, RED)
        draw_player_icon(enemy.get_x_position(), enemy.get_y_position(), PLAYER_SIZE, PLAYER_SIZE, BLACK)
        showTextScreen('Battle Square')
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def draw_player_icon(x_position, y_position, icon_width_, icon_height, color):
    rect_icon = pygame.Rect(x_position, y_position, icon_width_, icon_height)
    pygame.draw.rect(DISPLAYSURF, color, rect_icon)


def check_for_enemy_player_overlap(player_x_position, player_y_position, enemy_x_position, enemy_y_position):
    '''Checks to see if the enemy has overtaken the player.'''
    player_rect = pygame.Rect(player_x_position, player_y_position, PLAYER_SIZE, PLAYER_SIZE)
    enemy_rect = pygame.Rect(enemy_x_position, enemy_y_position, PLAYER_SIZE, PLAYER_SIZE)
    if pygame.Rect.colliderect(player_rect, enemy_rect) == True:
        terminate()


def terminate():
    '''Terminates games.'''
    pygame.quit()
    sys.exit()


def showTextScreen(text):
    # This function displays large text in the
    # center of the screen until a key is pressed.
    # Draw the text drop shadow
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.topleft = (int(WINDOWWIDTH - 290), 0)
    DISPLAYSURF.blit(titleSurf, titleRect)


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
