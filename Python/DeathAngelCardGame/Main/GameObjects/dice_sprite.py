import random

import pygame


class DiceSprite(pygame.sprite.Sprite):
    """A class to hold the individual dice sprites the sprite_x and sprite_y are the top left corner of the sprite on
    the sprite sheet """

    dice_positions = {'1': (0, 0),
                      '2': (32, 0),
                      '3': (0, 32),
                      '4': (32, 32),
                      '5': (0, 64),
                      '6': (32, 64)}
    display_number = 1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.sprite_sheet = pygame.image.load('Main/SpriteImages/dice_sprites.png')
        self.image = self.sprite_sheet.subsurface(pygame.Rect(0, 0, 32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def roll_dice(self):
        self.display_number = random.randint(1, 6)

    def set_display_number(self, number_to_display):
        self.display_number = number_to_display

    def update(self):
        self.image = self.sprite_sheet.subsurface(
            pygame.Rect(self.dice_positions[str(self.display_number)][0], self.dice_positions[str(self.display_number)][1], 32,
                        32))
