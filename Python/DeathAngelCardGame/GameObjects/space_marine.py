import pygame


class SpaceMarine(pygame.sprite.Sprite):

    def __init__(self, image_file_location):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(pygame.image.load(image_file_location), (480, 240))
        self.rect = self.image.get_rect()
