import pygame


class MazeWalls(pygame.sprite.Sprite):
    '''A class to hold the maze walls.'''

    BLOCK_SIZE = 15
    WALL_WIDTH = 2

    def __init__(self, x_index, y_index, container_boarder_width):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True

        #position indexes
        self.x_index = x_index
        self.y_index = y_index

        # need an surface variable image and a rectange of that suface rect
        self.image = pygame.Surface((self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.image.fill((0, 0, 0))
        if self.left_wall:
            pygame.draw.line(self.image, (0, 0, 255), (0, 0), (0, self.BLOCK_SIZE), self.WALL_WIDTH)
        if self.top_wall:
            pygame.draw.line(self.image, (0, 0, 255), (0, 0), (self.BLOCK_SIZE, 0), self.WALL_WIDTH)
        if self.right_wall:
            pygame.draw.line(self.image, (0, 0, 255), (self.BLOCK_SIZE - self.WALL_WIDTH, 0),
                             (self.BLOCK_SIZE - self.WALL_WIDTH, self.BLOCK_SIZE - self.WALL_WIDTH), self.WALL_WIDTH)
        if self.bottom_wall:
            pygame.draw.line(self.image, (0, 0, 255), (0, self.BLOCK_SIZE - self.WALL_WIDTH),
                             (self.BLOCK_SIZE, self.BLOCK_SIZE - self.WALL_WIDTH), self.WALL_WIDTH)

        self.rect = self.image.get_rect()

        # set the position of the surface by setting the position of the rect
        self.rect.x = (self.x_index * self.BLOCK_SIZE) + container_boarder_width
        self.rect.y = (self.y_index * self.BLOCK_SIZE) + container_boarder_width
