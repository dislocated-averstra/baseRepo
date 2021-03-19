import pygame


class MazeWalls(pygame.sprite.Sprite):
    '''A class to hold the maze walls.'''

    BLOCK_SIZE = 10

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True

        # need an surface variable image and a rectange of that suface rect
        self.image = pygame.Surface((self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.rect = self.image.get_rect();

        # set the position of the surface by setting the position of the rect
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        surface = pygame.Surface((self.BLOCK_SIZE, self.BLOCK_SIZE))
        surface.fill((0, 0, 0))
        if self.left_wall:
            pygame.draw.line(surface, (0, 0, 255), (0, 0), (0, 10), 2)
        if self.top_wall:
            pygame.draw.line(surface, (0, 0, 255), (0, 0), (10, 0), 2)
        if self.right_wall:
            pygame.draw.line(surface, (0, 0, 255), (8, 0), (8, 8), 2)
        if self.bottom_wall:
            pygame.draw.line(surface, (0, 0, 255), (0, 8), (10, 8), 2)
        self.image = surface
