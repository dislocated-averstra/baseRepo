import pygame


class PlayerZame(pygame.sprite.Sprite):
    RED = (255, 0, 0)
    PLAYER_SIZE = 8

    def __init__(self, x_position, y_position):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.x_position = x_position
        self.y_position = y_position

        self.image = pygame.Surface((self.PLAYER_SIZE, self.PLAYER_SIZE))
        pygame.draw.circle(self.image, self.RED, (4, 4), 4)

        self.rect = self.image.get_rect()
