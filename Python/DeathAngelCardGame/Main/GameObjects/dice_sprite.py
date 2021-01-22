import random
import time

import pygame


class DiceSprite(pygame.sprite.Sprite):
    """A class to hold the individual dice sprites the sprite_x and sprite_y are the top left corner of the sprite on
    the sprite sheet """

    dice_positions = {'1': (0, 0),
                      '2': (32, 0),
                      '3': (0, 32),
                      '4': (32, 32),
                      '5': (0, 64),
                      '0': (32, 64)}
    display_number = 1
    total_roll_time = 3
    time_between_sprite_change = .1
    last_change_time = 0
    dice_roll_start_time = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.sprite_sheet = pygame.image.load('Main/SpriteImages/dice_sprites2.png')
        self.image = self.sprite_sheet.subsurface(pygame.Rect(0, 0, 32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.is_dice_rolling = False

    def roll_dice(self):
        self.is_dice_rolling = True
        start_time = time.time()
        self.dice_roll_start_time = start_time
        self.last_change_time = start_time
        self.display_number = random.randint(0, 5)

    def set_display_number(self, number_to_display):
        self.display_number = number_to_display

    def update(self):
        if self.is_dice_rolling:
            current_time = time.time()
            if current_time - self.dice_roll_start_time < self.total_roll_time:
                if current_time - self.last_change_time < self.time_between_sprite_change:
                    self.image = self.sprite_sheet.subsurface(
                        pygame.Rect(self.dice_positions[str(self.display_number)][0],
                                    self.dice_positions[str(self.display_number)][1], 32, 32))
                elif current_time - self.last_change_time >= self.time_between_sprite_change:
                    self.last_change_time = current_time
                    self.display_number = random.randint(0, 5)
                    self.image = self.sprite_sheet.subsurface(
                        pygame.Rect(self.dice_positions[str(self.display_number)][0],
                                    self.dice_positions[str(self.display_number)][1],
                                    32, 32))
            elif current_time - self.dice_roll_start_time >= self.total_roll_time:
                self.is_dice_rolling = False
