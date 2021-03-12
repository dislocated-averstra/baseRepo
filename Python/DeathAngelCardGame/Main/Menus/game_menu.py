import pygame

MENU_WIDTH = 300
MENU_HEIGHT = 200


class Game_Menu(pygame.sprite.Sprite):
    def __init__(self, window_height, window_width):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.Surface((MENU_WIDTH, MENU_HEIGHT))
        self.image.fill((0, 0, 155))
        #draw the menu boarder
        pygame.draw.rect(self.image, (212, 175, 155),
                         (0, 0, MENU_WIDTH, MENU_HEIGHT), 5)
        self.top_left_x = window_width / 2 - 150
        self.top_left_y = window_height / 2 - 100
        self.rect = pygame.Rect(self.top_left_x, self.top_left_y, MENU_WIDTH, MENU_HEIGHT)

    def get_menu_surface(self):
        return self.image

    def get_menu_rect(self):
        return self.rect
