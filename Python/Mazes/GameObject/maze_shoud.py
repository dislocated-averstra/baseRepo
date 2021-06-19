import pygame



class MazeShoud(pygame.sprite.Sprite):
    BLACK = (0, 0, 0)
    SHOUD_SIZE = 600

    def __init__(self, x_position, y_position, size):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.image = pygame.Surface((self.SHOUD_SIZE, self.SHOUD_SIZE))
        pygame.draw.rect(self.image, self.BLACK, (300, 300, 600, 600))
        self.rect = self.image.get_rect()
