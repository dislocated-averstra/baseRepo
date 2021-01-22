# main build the window and start the program

import csv
import sys

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
SPRITE_SIZE = 32
BGCOLOR = DARKGREEN
FPS = 60

DIRECTIONS = ['LEFT', 'RIGHT', ' UP', 'DOWN']

MAXHEALTH = 3

KEYSIZE = 20

player_item = []


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, player, enemy, board, BIGFONT

    player = Player(64, 30, PLAYER_SIZE)
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

        # check_for_enemy_player_overlap(player.get_x_position(), player.get_y_position(), enemy.get_x_position(),
        # enemy.get_y_position())
        player.move_player(WINDOWHEIGHT, WINDOWWIDTH)
        did_player_hit_wall(board.get_board(), player.get_x_position(), player.get_y_position())
        #enemy.move_enemy(WINDOWHEIGHT, WINDOWWIDTH)
        DISPLAYSURF.fill(BGCOLOR)
        draw_board(board.get_board())
        draw_player_icon()
        # draw_player_icon(enemy.get_x_position(), enemy.get_y_position(), PLAYER_SIZE, PLAYER_SIZE, BLACK)
        showTextScreen('Battle Square')
        healthHeart(board.get_board())
        #drawHealthMeter(3)
        # move_element(board)
        player_eat_key(board.get_board(), player.get_x_position(), player.get_y_position())
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def draw_player_icon():
    DISPLAYSURF.blit(player.get_player_image(), (player.get_x_position(), player.get_y_position()))




def check_for_enemy_player_overlap(player_x_position, player_y_position, enemy_x_position, enemy_y_position):
    '''Checks to see if the enemy has overtaken the player.'''
    player_rect = pygame.Rect(player_x_position, player_y_position, PLAYER_SIZE, PLAYER_SIZE)
    enemy_rect = pygame.Rect(enemy_x_position, enemy_y_position, PLAYER_SIZE, PLAYER_SIZE)
    if pygame.Rect.colliderect(player_rect, enemy_rect):
        terminate()


def player_eat_key(board, player_x_position, player_y_position):
    for i in range(0, len(board)):
        for q in range(0, len(board[i])):
            if board[i][q] == 'key':
                player_rect = pygame.Rect(player_x_position, player_y_position, PLAYER_SIZE, PLAYER_SIZE)
                key_rect = pygame.Rect(i * SPRITE_SIZE, q * SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE)
                if pygame.Rect.colliderect(player_rect, key_rect) == True:
                    player.add_key()
                    board[i][q] = ""

def use_key(board, player_x_position, player_y_position, i, q): #need to add function call. use did player hit wall for colli detect.
    '''Use key to open door or chest.'''
    if player.get_key() == 0:
        player.stop_player(player_x_position, player_y_position, i, q)
    if player.get_key() > 0:
        player_rect = pygame.Rect(player_x_position, player_y_position, PLAYER_SIZE, PLAYER_SIZE)
        if pygame.Rect.colliderect(player_rect, pygame.Rect(i * SPRITE_SIZE, q * SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE)):
            player.remove_key()
            board[i][q] = ""

def did_player_hit_wall(board, player_x_position, player_y_position):
    '''Checks if the player hit the wall.'''
    x_index = player_x_position // SPRITE_SIZE
    y_index = player_y_position // SPRITE_SIZE
    if x_index == 0 and y_index == 0:  # top left
        for i in range(0, 2):
            for q in range(0, 2):
                if board[i][q] == 'brick':
                    player.stop_player(player_x_position, player_y_position, i, q)
                elif board[i][q] == 'chest' or board[i][q] == 'door':
                    use_key(board, player_x_position, player_y_position, i, q)
    elif x_index == 0 and y_index != 23:  # left side
        for i in range(0, 2):
            for q in range(y_index - 1, y_index + 2):
                if board[i][q] == 'brick':
                    player.stop_player(player_x_position, player_y_position, i, q)
                elif board[i][q] == 'chest' or board[i][q] == 'door':
                    use_key(board, player_x_position, player_y_position, i, q)
    elif x_index == 31 and y_index == 0:  # top right
        for i in range(x_index - 1, x_index + 1):
            for q in range(y_index - 1, y_index + 2):
                if board[i][q] == 'brick':
                    player.stop_player(player_x_position, player_y_position, i, q)
                elif board[i][q] == 'chest' or board[i][q] == 'door':
                    use_key(board, player_x_position, player_y_position, i, q)
    elif y_index == 0 and x_index != 31:  # top side
        for i in range(x_index - 1, x_index + 2):
            for q in range(0, y_index + 2):
                if board[i][q] == 'brick':
                    player.stop_player(player_x_position, player_y_position, i, q)
                elif board[i][q] == 'chest' or board[i][q] == 'door':
                    use_key(board, player_x_position, player_y_position, i, q)
    elif x_index == 31 and y_index != 23:  # right side
        for i in range(x_index - 1, x_index + 1):
            for q in range(y_index - 1, y_index + 2):
                if board[i][q] == 'brick':
                    player.stop_player(player_x_position, player_y_position, i, q)
                elif board[i][q] == 'chest' or board[i][q] == 'door':
                    use_key(board, player_x_position, player_y_position, i, q)
    elif y_index == 23 and x_index != 31:  # bottom side
        for i in range(x_index - 1, x_index + 2):
            for q in range(y_index - 1, y_index + 1):
                if board[i][q] == 'brick':
                    player.stop_player(player_x_position, player_y_position, i, q)
                elif board[i][q] == 'chest' or board[i][q] == 'door':
                    use_key(board, player_x_position, player_y_position, i, q)
    elif x_index == 31 and y_index == 23:  # bottom right
        for i in range(30, 32):
            for q in range(22, 24):
                if board[i][q] == 'brick':
                    player.stop_player(player_x_position, player_y_position, i, q)
                elif board[i][q] == 'chest' or board[i][q] == 'door':
                    use_key(board, player_x_position, player_y_position, i, q)
    else:  # middle of board
        for i in range(x_index - 1, x_index + 2):
            for q in range(y_index - 1, y_index + 2):
                if board[i][q] == 'brick':
                    player.stop_player(player_x_position, player_y_position, i, q)
                elif board[i][q] == 'chest' or board[i][q] == 'door':
                    use_key(board, player_x_position, player_y_position, i, q)


def healthHeart(board):
    full_heart = pygame.image.load('gameSprites/Fullheart.png')
    full_heart = pygame.transform.scale(full_heart, (100, 100))
    DISPLAYSURF.blit(full_heart, (780, 30))
    empty_heart = pygame.image.load('gameSprites/EmptyHeart.png')
    empty_heart = pygame.transform.scale(empty_heart, (100, 100))
    DISPLAYSURF.blit(empty_heart, (860, 30))


def draw_board(board):
    '''Draws the board with bricks.'''
    brick_wall = pygame.image.load('gameSprites/BrickWall2.png')
    key = pygame.image.load('gameSprites/Key.png')
    chest = pygame.image.load('gameSprites/chest_sprite.png')
    door = pygame.image.load('gameSprites/door_sprite.png')
    for i in range(0, len(board)):
        for q in range(0, len(board[i])):
            if board[i][q] == 'brick':
                DISPLAYSURF.blit(brick_wall, (i * SPRITE_SIZE, q * SPRITE_SIZE))
            if board[i][q] == 'key':
                DISPLAYSURF.blit(key, (i * SPRITE_SIZE, q * SPRITE_SIZE))
            if board[i][q] == 'chest':
                DISPLAYSURF.blit(chest, (i * SPRITE_SIZE, q * SPRITE_SIZE))
            if board[i][q] == 'door':
                DISPLAYSURF.blit(door, (i * SPRITE_SIZE, q * SPRITE_SIZE))


def loop_through_brick_file(board):
    try:
        with open('LevelLayout/brick.csv') as f:
            data = csv.reader(f)
            for row in data:
                ab = data.line_num - 1
                for i in range(0, len(row)):
                    board.add_to_gameboard(i, ab, row[i])
    except FileNotFoundError:
        print("Not found")
    finally:
        f.close()


'''def move_element(board):
    with open('/Users/ngocphan/PycharmProjects/baseRepo/Python/AdventureGame/LevelLayout/brick.csv') as f:
        data = csv.reader(f)
        for row in data:
            ab = data.line_num - 1
            for i in range(0, len(row)):
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
