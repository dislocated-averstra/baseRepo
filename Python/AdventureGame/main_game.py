# main build the window and start the program

import csv
import sys

import pygame
from pygame.locals import *

from GameBoard.game_board import *
from GameObject.game_enemy import *
from GameObject.game_player import *

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

MAXHEALTH = 3


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
    loop_through_brick_file(board)
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

        check_for_enemy_player_overlap(player.get_x_position(), player.get_y_position(), enemy.get_x_position(),
                                       enemy.get_y_position())
        did_player_hit_wall(board.get_board(), player.get_x_position(), player.get_y_position())
        player.move_player(WINDOWHEIGHT, WINDOWWIDTH)
        did_player_hit_wall(board.get_board(), player.get_x_position(), player.get_y_position())
        #enemy.move_enemy(player.get_x_position(), player.get_y_position())
        DISPLAYSURF.fill(BGCOLOR)
        draw_board(board.get_board())
        draw_player_icon(player.get_x_position(), player.get_y_position(), PLAYER_SIZE, PLAYER_SIZE, RED)
        #draw_player_icon(enemy.get_x_position(), enemy.get_y_position(), PLAYER_SIZE, PLAYER_SIZE, BLACK)
        showTextScreen('Battle Square')
        drawHealthMeter(3)

        # move_element(board)
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


def did_player_hit_wall(board, player_x_position, player_y_position):
    '''Checks if the player hit the wall.'''
    for i in range(0, len(board)):
        for q in range(0, len(board[i])):
            if board[i][q] == 'brick':
                player_rect = pygame.Rect(player_x_position, player_y_position, PLAYER_SIZE, PLAYER_SIZE)
                wall_rect = pygame.Rect(i * 32, q * 32, 32, 32)

                if pygame.Rect.colliderect(player_rect, wall_rect) == True:
                    if 'LEFT' in player.get_horizontal_directions():
                        player.set_x_position(player_x_position + 2)
                    if 'RIGHT' in player.get_horizontal_directions():
                        player.set_x_position(player_x_position - 2)
                    if 'UP' in player.get_vertical_directions():
                        player.set_y_position(player_y_position + 2)
                    if 'DOWN' in player.get_vertical_directions():
                        player.set_y_position(player_y_position - 2)



def drawHealthMeter(currentHealth):
    for i in range(currentHealth):  # draw red health bars
        pygame.draw.rect(DISPLAYSURF, RED, (900, 50 + (10 * MAXHEALTH) - i * 10, 20, 10))
    for i in range(MAXHEALTH):  # draw the white outlines
        pygame.draw.rect(DISPLAYSURF, WHITE, (900, 50 + (10 * MAXHEALTH) - i * 10, 20, 10), 1)


def draw_board(board):
    '''Draws the board with bricks.'''
    brick_wall = pygame.image.load('gameSprites/BrickWall.png')
    for i in range(0, len(board)):
        for q in range(0, len(board[i])):
            if board[i][q] == 'brick':
                DISPLAYSURF.blit(brick_wall, (i * 32, q * 32))


def loop_through_brick_file(board):
    with open('LevelLayout/brick.csv') as f:
        data = csv.reader(f)
        for row in data:
            ab = data.line_num - 1
            for i in range(0, len(row) - 1):
                board.add_to_gameboard(i, ab, row[i])


'''def move_element(board):
    with open('/Users/ngocphan/PycharmProjects/baseRepo/Python/AdventureGame/LevelLayout/brick.csv') as f:
        data = csv.reader(f)
        for row in data:
            ab = data.line_num - 1
            for i in range(0, len(row) - 1):
                board.remove_element(i, ab, row[i])'''


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
