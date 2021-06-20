import pygame


class MazeShoud(pygame.sprite.Sprite):
    BLACK = (0, 0, 0)
    SHOUD_SIZE = 320

    def __init__(self, x_position, y_position, size):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.image = pygame.Surface((self.SHOUD_SIZE, self.SHOUD_SIZE))
        #transparent square set to 250 for now
        self.image.set_alpha(250)

        pygame.draw.rect(self.image, self.BLACK, (300, 300, 600, 600))
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

