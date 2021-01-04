import sys

import pygame


class FacingArrow(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        try:
            self.image = pygame.image.load('Main\SpriteImages\Arrow.png')
        except FileNotFoundError:
            try:
                self.image = pygame.image.load('..\..\Main\SpriteImages\Arrow.png')
            except FileNotFoundError:
                print("facing arrow file not found")
                pygame.quit()
                sys.exit()

        self.rect = self.image.get_rect()

    def set_position(self, x_position, y_position):
        self.rect.x = x_position
        self.rect.y = y_position

    def arrow_clicked(self, x_click_position, y_position_click):
        return self.rect.collidepoint(x_click_position, y_position_click)
