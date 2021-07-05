import sys

import pygame
from pygame.locals import *

from Python.Mazes.GameObject.MazeAlgorithm import GenerateMaze
from Python.Mazes.GameObject.maze_container import MazeContainer
from Python.Mazes.GameObject.player_zame import PlayerZame

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
GRAY = (185, 185, 185)
LIGHTRED = (175, 20, 20)
FPS = 60
PLAYER_SIZE = 8


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FPSCLOCK = pygame.time.Clock()
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption('Mazes')
    showStartScreen()
    while True:
        run_game()


def run_game():
    # create the render group that is going to hold all the sprite for the time being
    render_update_group = pygame.sprite.RenderUpdates()
    MazeContainer.containers = render_update_group
    PlayerZame.containers = render_update_group
    maze = MazeContainer()
    player = PlayerZame(308, 308, PLAYER_SIZE)
    generate_maze = GenerateMaze(maze)
    generate_maze.maze_algorithm(0, 0, ['LEFT', 'RIGHT', 'UP', 'DOWN'])
    maze = generate_maze.container
    maze.check_9_squares_around_player(player.player_x_array_position, player.player_y_array_position, True)
    maze.draw_maze_walls()
    maze.set_position(300, 300)

    while True:
        checkForQuit()
        winMode = check_for_win(player)

        for event in pygame.event.get():
            if event.type == KEYDOWN:  # a person is pressed or is pressing a key
                if event.key in (K_a, K_LEFT) and check_if_player_move_valid(player, maze, 'LEFT') and winMode is False:
                    player.move_player('LEFT')
                if event.key in (K_d, K_RIGHT) and check_if_player_move_valid(player, maze,
                                                                              'RIGHT') and winMode is False:
                    player.move_player('RIGHT')
                if event.key in (K_w, K_UP) and check_if_player_move_valid(player, maze, 'UP') and winMode is False:
                    player.move_player('UP')
                if event.key in (K_s, K_DOWN) and check_if_player_move_valid(player, maze, 'DOWN') and winMode is False:
                    player.move_player('DOWN')
                if winMode and event.key == K_r:
                    return

        if winMode is not True:
            if player.previous_position_x != player.player_x_array_position or player.previous_position_y != player.player_y_array_position:
                maze.vision_change(player.previous_position_x, player.previous_position_y, False)

                player.previous_position_x = player.player_x_array_position
                player.previous_position_y = player.player_y_array_position
                maze.look_at_the_wall_from_player(player.player_x_array_position, player.player_y_array_position)
                maze.draw_maze_walls()

            DISPLAYSURF.fill(GRAY)

            # clear all the sprites
            render_update_group.clear(DISPLAYSURF, DISPLAYSURF)

            # update all the sprites
            render_update_group.update()

            dirty = render_update_group.draw(DISPLAYSURF)

            pygame.display.update(dirty)
            FPSCLOCK.tick(FPS)


def check_for_win(player):
    # recalculate here
    if player.player_x_array_position == 19 and player.player_y_array_position == 19:
        showWinningMessage()
        return True
    else:
        return False


def check_if_player_move_valid(player, maze, direction):
    if direction == 'LEFT' and maze.maze_wall[player.get_player_array_y_position()][
        player.get_player_array_x_position()].left_wall:
        return False
    elif direction == 'RIGHT' and maze.maze_wall[player.get_player_array_y_position()][
        player.get_player_array_x_position()].right_wall:
        return False
    elif direction == 'UP' and maze.maze_wall[player.get_player_array_y_position()][
        player.get_player_array_x_position()].top_wall:
        return False
    elif direction == 'DOWN' and maze.maze_wall[player.get_player_array_y_position()][
        player.get_player_array_x_position()].bottom_wall:
        return False
    else:
        return True


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


def showWinningMessage():
    titleSurf, titleRect = makeTextObjs('You won the game', BIGFONT, LIGHTRED)
    titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)

    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play again.', BASICFONT, LIGHTRED)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    pygame.display.update()
    FPSCLOCK.tick()


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
