import pygame


class maze_walls(pygame.sprite.Sprite):
    '''A class to hold the maze walls.'''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True