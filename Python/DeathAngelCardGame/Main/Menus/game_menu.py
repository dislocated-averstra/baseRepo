import pygame

from Python.DeathAngelCardGame.Main.Utils.colors import Color
from Python.DeathAngelCardGame.Main.Utils.game_utils import makeTextObjs

MENU_WIDTH = 300
MENU_HEIGHT = 200


class Game_Menu(pygame.sprite.Sprite):
    def __init__(self, window_height, window_width):
        pygame.sprite.Sprite.__init__(self, self.containers)
        # init the containing window height and width so that we can use them later to calculate the relative
        # position of mouse clicks
        self.containing_window_height = window_height
        self.containing_window_width = window_width

        # create the menu surface and rectangle
        self.image = pygame.Surface((MENU_WIDTH, MENU_HEIGHT))
        self.rect = pygame.Rect(window_width / 2 - 150, window_height / 2 - 100, MENU_WIDTH, MENU_HEIGHT)

        # fill in the surface with a background color
        self.image.fill(Color.ROYAL_BLUE.value)

        # draw the menu boarder
        pygame.draw.rect(self.image, (212, 175, 155),
                         (0, 0, MENU_WIDTH, MENU_HEIGHT), 5)

        # create the quit text and add it to the menu
        menu_font = pygame.font.SysFont('arial', 20)
        self.quit_surf, self.quit_rect = makeTextObjs("Quit", menu_font, Color.RED.value)
        self.quit_rect.midtop = (MENU_WIDTH / 2, 10)
        self.image.blit(self.quit_surf, self.quit_rect)

        # create the close menu 'X'
        self.close_surf = pygame.image.load('Main/SpriteImages/x_icon.png')
        self.close_rect = self.close_surf.get_rect()
        self.close_rect.x = MENU_WIDTH - 38
        self.close_rect.y = 5
        self.image.blit(self.close_surf, self.close_rect)

    def get_menu_surface(self):
        return self.image

    def get_menu_rect(self):
        return self.rect

    def is_quit_button_clicked(self, pos):
        gap_between_menu_and_window_horizontal = self.containing_window_width / 2 - MENU_WIDTH / 2
        x_pos = pos[0] - gap_between_menu_and_window_horizontal
        gap_between_menu_and_window_vertical = self.containing_window_height / 2 - MENU_HEIGHT / 2
        y_pos = pos[1] - gap_between_menu_and_window_vertical
        return self.quit_rect.collidepoint(x_pos, y_pos)

    def is_close_button_clicked(self, pos):
        gap_between_menu_and_window_horizontal = self.containing_window_width / 2 - MENU_WIDTH / 2
        x_pos = pos[0] - gap_between_menu_and_window_horizontal
        gap_between_menu_and_window_vertical = self.containing_window_height / 2 - MENU_HEIGHT / 2
        y_pos = pos[1] - gap_between_menu_and_window_vertical
        return self.close_rect.collidepoint(x_pos, y_pos)
