import pygame


class PlayerZame(pygame.sprite.Sprite):
    RED = (255, 0, 0)
    PLAYER_SIZE = 8

    def __init__(self, x_position, y_position, size):
        pygame.sprite.Sprite.__init__(self, self.containers)


        self.image = pygame.Surface((self.PLAYER_SIZE, self.PLAYER_SIZE))
        pygame.draw.circle(self.image, self.RED, (4, 4), 4)

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

    def move_player(self, move_direction):
        '''moves the player 10 pixels in a given direction'''
        if move_direction == 'LEFT':
            self.rect.x -= 15
        if move_direction == 'RIGHT':
            self.rect.x += 15
        if move_direction == 'UP':
            self.rect.y -= 15
        if move_direction == 'DOWN':
            self.rect.y += 15