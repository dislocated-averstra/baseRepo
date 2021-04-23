import unittest
import pygame
from Python.Mazes.GameObject.MazeAlgorithm import GenerateMaze
from Python.Mazes.GameObject.maze_container import MazeContainer

class MyTestCase(unittest.TestCase):
    def test_something(self):
        render_update_group = pygame.sprite.RenderUpdates()
        MazeContainer.containers = render_update_group
        test_maze = MazeContainer()
        test_algor = GenerateMaze(test_maze)
        test_algor.maze_algorithm(0, 0,["LEFT", "RIGHT", "UP", "DOWN"])
        for x in test_algor.container.maze_wall:
            for y in x:
                self.assertTrue(self.helper_fun(y))

    def helper_fun(self, maze_wall_item):
        if maze_wall_item.left_wall is False:
            return True
        elif maze_wall_item.right_wall is False:
            return True
        elif maze_wall_item.top_wall is False:
            return True
        elif maze_wall_item.bottom_wall is False:
            return True
        else:
            return False


if __name__ == '__main__':
    unittest.main()
