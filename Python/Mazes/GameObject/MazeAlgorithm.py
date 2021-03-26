import sys
import pygame
from pygame.locals import *
from Python.Mazes.Utilities.Stack import Stack
from Python.Mazes.GameObject.maze_container import MazeContainer


class GenerateMaze:
    """ constructor for maze """

    def __init__(self, maze_containers):
        self.container = maze_containers
        self.stack = Stack()

    """ store starting point to stack """

    def maze_algorithm(self):
        self.stack.push(self.container.maze_wall[0][0])

    def neighbor(self):
        top = self.stack.top()
        rows = top.x_index
        colunms = top.y_index
        top_neighbor = self.container.maze_wall[rows][colunms - 1]
        right_neighbor = self.container.maze_wall[rows + 1][colunms]
        left_neighbor = self.container.maze_wall[rows - 1][colunms]
        bottom_neighbor = self.container.maze_wall[rows][colunms + 1]
        neighbor = []
