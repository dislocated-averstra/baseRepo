import pygame

from Python.DeathAngelCardGame.Main.Emuns.facing_emun import Facing
from Python.DeathAngelCardGame.Main.GameObjects.facing_arrow import FacingArrow


class SpaceMarine(pygame.sprite.Sprite):

    def __init__(self, image_file_location):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(pygame.image.load(image_file_location), (240, 120))
        self.rect = self.image.get_rect()
        self.facing = Facing.LEFT
        self.is_selected = False
        # a bunch of stuff to hold the arrow that go with a space marine sprite
        self.arrow_render_group = pygame.sprite.RenderUpdates()
        FacingArrow.containers = self.arrow_render_group
        self.facing_arrow = FacingArrow()

    def get_is_selected(self):
        return self.is_selected

    def set_is_selected(self, is_selected):
        self.is_selected = is_selected

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.facing_arrow.set_position(int(x + 5), int(y + 40))

    def get_rect(self):
        return self.rect

    def get_rect_x(self):
        return self.rect.x

    def get_rect_y(self):
        return self.rect.y

    def get_arrow_containers(self):
        return self.arrow_render_group

    def get_facing(self):
        return self.facing

    def set_facing(self, facing):
        if facing is Facing.LEFT:
            self.facing = Facing.LEFT
        elif facing is Facing.RIGHT:
            self.facing = Facing.RIGHT

    def check_if_facing_arrow_clicked(self, x_click_position, y_click_position):
        if self.facing_arrow.arrow_clicked(x_click_position, y_click_position):
            self.image = pygame.transform.flip(self.image, True, False)
