import pygame

from Python.Mazes.GameObject.maze_walls import MazeWalls


class MazeContainer(pygame.sprite.Sprite):
    '''construtor for maze container'''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.Surface((310, 310))
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, (0, 255, 0), (0, 0, 310, 310), 10)
        self.rect = self.image.get_rect()

        # give the maze walls a container before we create them
        self.maze_wall_update_group = pygame.sprite.RenderUpdates()
        MazeWalls.containers = self.maze_wall_update_group

        # create the maze wall and put them into a 2d array
        rows, cols = (20, 20)
        self.maze_wall = [[MazeWalls(i, j, 5) for i in range(cols)] for j in range(rows)]

        self.maze_wall_update_group.draw(self.image)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw_maze_walls(self):
        for maze_list in self.maze_wall:
            for wall in maze_list:
                wall.draw_self()
        self.maze_wall[19][19].draw_self_set_background_color(0, 255, 0)
        self.maze_wall_update_group.draw(self.image)

    def vision_change(self, x, y, boolean_val):
        self.check_9_squares_around_player(x, y, boolean_val)

    def check_9_squares_around_player(self, player_position_x, player_position_y, boolean):
        """ check the 9 squares around the player and change visuality to True """
        if player_position_x == 0 and player_position_y == 0:  # top left
            for i in range(0, 2):
                for q in range(0, 2):
                    self.maze_wall[q][i].visuality = boolean
        elif player_position_x == 0 and player_position_y != 19:  # left side
            for i in range(0, 2):
                for q in range(player_position_y - 1, player_position_y + 2):
                    self.maze_wall[q][i].visuality = boolean
        elif player_position_x == 19 and player_position_y == 0:  # top right
            for i in range(player_position_x - 1, player_position_x + 1):
                for q in range(player_position_y - 1, player_position_y + 2):
                    self.maze_wall[q][i].visuality = boolean
        elif player_position_y == 0 and player_position_x != 19:  # top side
            for i in range(player_position_x - 1, player_position_x + 2):
                for q in range(0, player_position_y + 2):
                    self.maze_wall[q][i].visuality = boolean
        elif player_position_x == 19 and player_position_y != 19:  # right side
            for i in range(player_position_x - 1, player_position_x + 1):
                for q in range(player_position_y - 1, player_position_y + 2):
                    self.maze_wall[q][i].visuality = boolean
        elif player_position_y == 19 and player_position_x != 19:  # bottom side
            for i in range(player_position_x - 1, player_position_x + 2):
                for q in range(player_position_y - 1, player_position_y + 1):
                    self.maze_wall[q][i].visuality = boolean
        elif player_position_x == 19 and player_position_y == 19:  # bottom right
            for i in range(17, 19):
                for q in range(17, 19):
                    self.maze_wall[q][i].visuality = boolean
        else:  # middle of board
            for i in range(player_position_x - 1, player_position_x + 2):
                for q in range(player_position_y - 1, player_position_y + 2):
                    self.maze_wall[q][i].visuality = boolean
