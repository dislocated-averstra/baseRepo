# main build the window and start the program
import pygame, sys
from pygame.locals import *
from GameObject.game_player import *

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768

RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (21, 156, 75)

PLAYER_SIZE = 20
BGCOLOR = DARKGREEN
FPS = 60

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, player

    player = Player(502, 374)
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Main Game')
    run_game()


def run_game():
    '''The main code for the game I expect we will refactor this several times as we go'''
    while True:
        checkForQuit()
        for event in pygame.event.get():
            if event.type == KEYUP: # a person let go of the key
                player.set_move(None)
            if event.type == KEYDOWN: # a person is pressed or is pressing a key
                if event.key in (K_a, K_LEFT) and player.get_move() is None:
                    player.set_move('LEFT')
                if event.key in (K_d, K_RIGHT) and player.get_move() is None:
                    player.set_move('RIGHT')

        move_player(player.get_move())
        DISPLAYSURF.fill(BGCOLOR)
        draw_player_icon(player.get_x_position(), player.get_y_position())
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def move_player(move_direction):
    if move_direction == 'LEFT' and player.get_x_position() - 2 > 0:
        player.set_x_position(player.get_x_position() - 2)
    if move_direction == 'RIGHT' and player.get_x_position() + 2 < (WINDOWWIDTH - PLAYER_SIZE):
        player.set_x_position(player.get_x_position() + 2)

def draw_player_icon(x_position, y_position):
    player_icon = pygame.Rect(x_position, y_position, PLAYER_SIZE, PLAYER_SIZE)
    pygame.draw.rect(DISPLAYSURF, RED, player_icon)

def terminate():
    '''Terminates games.'''
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

if __name__ == '__main__':
    main()