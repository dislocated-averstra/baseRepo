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
        for i in range(3):
            random_neighbor_direction = self.pick_direction()
            if random_neighbor_direction is not None:
                self.remove_walls(random_neighbor_direction)


    def neighbor(self, direction):
        x_index, y_index = None
        current_maze_wall = self.stack.top()
        if direction == 'LEFT':
            x_index = current_maze_wall.x_index - 1
            y_index = current_maze_wall.y_index
        if direction == "RIGHT":
            x_index = current_maze_wall.x_index + 1
            y_index = current_maze_wall.y_index
        if direction == "UP":
            x_index = current_maze_wall.x_index
            y_index = current_maze_wall.y_index - 1
        if direction == "DOWN":
            x_index = current_maze_wall.x_index
            y_index = current_maze_wall.y_index + 1
        return x_index, y_index

    def remove_walls(self, direction):
        '''Turns walls from true to false'''
        current_maze_wall = self.stack.top()
        x_index, y_index = self.neighbor(direction)
        if direction == 'LEFT':
            current_maze_wall.left_wall = False
            self.container.maze_wall[x_index][y_index].right_wall = False
        if direction == 'RIGHT':
            current_maze_wall.right_wall = False
            self.container.maze_wall[x_index][y_index].left_wall = False
        if direction == 'UP':
            current_maze_wall.top_wall = False
            self.container.maze_wall[x_index][y_index].bottom_wall = False
        if direction == 'DOWN':
            current_maze_wall.bottom_wall = False
            self.container.maze_wall[x_index][y_index].top_wall = False

    # you may need to change this , you dont need neihbor func or list
    def pick_direction(self):
        random_direction = random.sample(self.direction, 1)
        self.direction.remove(random_direction[0])
        if self.is_valid_move(random_direction[0]):
            return random_direction[0]
        else:
            return None
# TODO have is valid use neighbor function, check multiple returns
    def is_valid_move(self, direction):
        if direction == "LEFT":
            current_maze_wall = self.stack.top()
            x_index = current_maze_wall.x_index - 1
            y_index = current_maze_wall.y_index
            if x_index >= 0 and self.container.maze_wall[x_index][y_index] not in self.visited:
                return True
            else:
                return False

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
