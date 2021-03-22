import sys
import pygame
from pygame.locals import *
from Python.Mazes.Utilities.Stack import Stack
from Python.Mazes.GameObject.maze_container import MazeContainer


class GenerateMaze():
    '''list of list for maze'''

    def __init__(self, maze_containers):
        self.container = maze_containers
        self.stack = Stack()

    def maze_algorithm(self):
        self.stack.push(self.container.maze_wall[0][0])

