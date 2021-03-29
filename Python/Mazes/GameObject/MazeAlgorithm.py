import sys
import pygame
from pygame.locals import *
from Python.Mazes.Utilities.Stack import Stack
from Python.Mazes.GameObject.maze_container import MazeContainer
import random
from random import sample


class GenerateMaze:
    """ constructor for maze """

    def __init__(self, maze_containers):
        self.container = maze_containers
        self.stack = Stack()
        self.visited = []
        self.neighbor = []
        self.direction = ["LEFT", "RIGHT", "UP", "DOWN"]

    """ store starting point to stack """

    def maze_algorithm(self):
        self.stack.push(self.container.maze_wall[0][0])
        self.visited.append(self.stack.top())
        self.neighbor()
        # random_neighbor_index = self.pick_direction()
        # self.stack.push(self.neighbor[random_neighbor_index])
    def recursive_function(self):


    def neighbor(self):
        top = self.stack.top()
        rows = top.x_index
        colunms = top.y_index
        top_neighbor = self.container.maze_wall[rows][colunms - 1]
        right_neighbor = self.container.maze_wall[rows + 1][colunms]
        left_neighbor = self.container.maze_wall[rows - 1][colunms]
        bottom_neighbor = self.container.maze_wall[rows][colunms + 1]
        self.check(top_neighbor)
        self.check(right_neighbor)
        self.check(left_neighbor)
        self.check(bottom_neighbor)

    def check(self, surrounding_neighbor):
        if surrounding_neighbor not in self.visited:
            self.neighbor.append(surrounding_neighbor)

    #you may need to change this , you dont need neihbor func or list
    def pick_direction(self):
        random_direction = random.sample(self.direction, 1)
        self.direction.remove(random_direction[0])
        if self.is_valid_move(random_direction[0]):
            return random_direction[0]
        else:
            return None

    def is_valid_move(self, direction):
        if direction == "LEFT":
            current_maze_wall = self.stack.top()
            x_index = current_maze_wall.x_index - 1
            y_index = current_maze_wall.y_index
            if x_index >= 0 and self.container.maze_wall[x_index][y_index] not in self.visited:
                return True
            else:
                return False

        # TODO FINISH FUNCTION
        if direction == "RIGHT":
            current_maze_wall = self.stack.top()
            x_index = current_maze_wall.x_index + 1
            y_index = current_maze_wall.y_index
            if x_index <= 20 and self.container.maze_wall[x_index][y_index] not in self.visited:
                return True
            else:
                return False
        if direction == "UP":
            current_maze_wall = self.stack.top()
            x_index = current_maze_wall.x_index
            y_index = current_maze_wall.y_index - 1
            if y_index >= 0 and self.container.maze_wall[x_index][y_index] not in self.visited:
                return True
            else:
                return False
        if direction == "DOWN":
            current_maze_wall = self.stack.top()
            x_index = current_maze_wall.x_index
            y_index = current_maze_wall.y_index + 1
            if y_index <= 20 and self.container.maze_wall[x_index][y_index] not in self.visited:
                return True
            else:
                return False

