import pygame
import time

from Python.AdventureGame.GameObject.game_object import GameBaseObject

PLAYER_SIZE = 20
SPRITE_SIZE = 32


class Player(GameBaseObject):
    horizontal_directions = []
    vertical_directions = []
    player_item = {'key': 0}
    player_sprite_positions = {'1': (0, 0),
                               '2': (32, 0),
                               '3': (64, 0),
                               '4': (96, 0),
                               '5': (128, 0),
                               '6': (160, 0),
                               '7': (192, 0),
                               '8': (224, 0)}
    image_number = 0
    total_roll_time = 3
    time_between_sprite_change = .1
    last_change_time = 0
    dice_roll_start_time = 0

    def __init__(self, x_position, y_position, size):
        # GameObject__init__(self, x_position, y_position)
        self.size = size
        self.sprite_sheet = pygame.image.load('gameSprites/WalkAnimation.png')
        self.player_image = self.sprite_sheet.subsurface(pygame.Rect(0, 0, 32, 32))
        self.is_dice_rolling = False
        super().__init__(x_position, y_position)

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def get_player_image(self):
        return self.player_image

    def set_player_image(self): #flip the image for left and add clocks
        if self.horizontal_directions[0] == 'RIGHT':
            self.player_image = self.sprite_sheet.subsurface(pygame.Rect(self.image_number, 0, 32, 32))
            self.add_to_image_number()
        elif self.horizontal_directions[0] == 'LEFT':
            self.player_image = pygame.transform.flip(self.sprite_sheet.subsurface(pygame.Rect(self.image_number, 0, 32, 32), True, False))
            self.add_to_image_number()

    def add_to_image_number(self):
        self.image_number += 32
        if self.image_number == 256:
            self.image_number = 0

    def roll_dice(self):
        self.is_dice_rolling = True
        start_time = time.time()
        self.dice_roll_start_time = start_time
        self.last_change_time = start_time

    def image_updater(self):
        if self.is_dice_rolling:
            current_time = time.time()
            if current_time - self.dice_roll_start_time < self.total_roll_time:
                if current_time - self.last_change_time < self.time_between_sprite_change:
                    self.set_player_image()
                elif current_time - self.last_change_time >= self.time_between_sprite_change:
                    self.last_change_time = current_time
                    self.set_player_image()
            elif current_time - self.dice_roll_start_time >= self.total_roll_time:
                self.is_dice_rolling = False

    def add_key(self):
        self.player_item['key'] += 1

    def remove_key(self):
        self.player_item['key'] -= 1

    def get_horizontal_directions(self):
        return self.horizontal_directions

    def add_horizontal_direction(self, direction):
        if direction not in self.horizontal_directions:
            self.horizontal_directions.insert(0, direction)

    def remove_horizontal_direction(self, direction):
        self.horizontal_directions.remove(direction)

    def get_vertical_directions(self):
        return self.vertical_directions

    def add_vertical_direction(self, direction):
        if direction not in self.vertical_directions:
            self.vertical_directions.insert(0, direction)

    def remove_vertical_direction(self, direction):
        self.vertical_directions.remove(direction)

    def get_current_direction(self):
        if len(self.horizontal_directions) == 0 and len(self.vertical_directions) == 0:
            return None, None
        elif len(self.horizontal_directions) != 0 and len(self.vertical_directions) == 0:
            return self.horizontal_directions[0], None
        elif len(self.horizontal_directions) == 0 and len(self.vertical_directions) != 0:
            return None, self.vertical_directions[0]
        else:
            return self.horizontal_directions[0], self.vertical_directions[0]

    def move_player(self, window_height, window_width):
        horizontal_direction, vertical_direction = self.get_current_direction()

        if horizontal_direction is None and vertical_direction is not None:
            if vertical_direction == 'UP' and self.get_y_position() - 2 > 0:
                self.set_y_position(self.get_y_position() - 2)
            if vertical_direction == 'DOWN' and self.get_y_position() + 2 < (window_height - self.size):
                self.set_y_position(self.get_y_position() + 2)
        elif horizontal_direction is not None and vertical_direction is None:
            if horizontal_direction == 'LEFT' and self.get_x_position() - 2 > 0:
                self.set_x_position(self.get_x_position() - 2)
                self.image_updater()
            if horizontal_direction == 'RIGHT' and self.get_x_position() + 2 < (window_width - self.size):
                self.set_x_position(self.get_x_position() + 2)
                self.image_updater()
        elif horizontal_direction is not None and vertical_direction is not None:
            if vertical_direction == 'UP' and self.get_y_position() - 1 > 0:
                self.set_y_position(self.get_y_position() - 1)
            if vertical_direction == 'DOWN' and self.get_y_position() + 1 < (window_height - self.size):
                self.set_y_position(self.get_y_position() + 1)
            if horizontal_direction == 'LEFT' and self.get_x_position() - 1 > 0:
                self.set_x_position(self.get_x_position() - 1)
            if horizontal_direction == 'RIGHT' and self.get_x_position() + 1 < (window_width - self.size):
                self.set_x_position(self.get_x_position() + 1)

    def stop_player(self, player_x_position, player_y_position, i_wall_coord, q_wall_coord):
        player_rect = pygame.Rect(player_x_position, player_y_position, PLAYER_SIZE, PLAYER_SIZE)
        wall_rect = pygame.Rect(i_wall_coord * SPRITE_SIZE, q_wall_coord * SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE)
        if pygame.Rect.colliderect(wall_rect, player_rect):
            if 'LEFT' in self.get_horizontal_directions():
                self.set_x_position(player_x_position + 2)
            if 'RIGHT' in self.get_horizontal_directions():
                self.set_x_position(player_x_position - 2)
            if 'UP' in self.get_vertical_directions():
                self.set_y_position(player_y_position + 2)
            if 'DOWN' in self.get_vertical_directions():
                self.set_y_position(player_y_position - 2)

    def get_key(self):
        return self.player_item['key']

    def to_string(self):
        return 'X position: %s, Y position: %s' % (self.x_position, self.y_position)
