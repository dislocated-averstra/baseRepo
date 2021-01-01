import unittest

import pygame

from Python.DeathAngelCardGame.Main.GameObjects.space_marine import SpaceMarine


class MyTestCase(unittest.TestCase):

    def test_move(self):
        render_update_group = pygame.sprite.RenderUpdates()
        SpaceMarine.containers = render_update_group

        test_sprite = SpaceMarine('../../Main/SpriteImages/chaplain_raziel.png')
        test_sprite.move(100, 100)
        self.assertEqual(test_sprite.get_rect_x(), 100)
        self.assertEqual(test_sprite.get_rect_y(), 100)


if __name__ == '__main__':
    unittest.main()
