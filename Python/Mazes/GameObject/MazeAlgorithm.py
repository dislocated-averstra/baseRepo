import random

from Python.Mazes.Utilities.Stack import Stack


class GenerateMaze:
    """ constructor for maze """

    def __init__(self, maze_containers):
        self.container = maze_containers
        self.stack = Stack()
        self.visited = []
        self.largestStack = 0
        self.largestStackLocation = (0, 0)
        if len(maze_containers.maze_wall) > 0:
            self.row_container_length = len(maze_containers.maze_wall)
            if len(maze_containers.maze_wall[0]) > 0:
                self.col_container_length = len(maze_containers.maze_wall[0])

    """ recursive """

    def maze_algorithm(self, x_index, y_index, directions_list):
        self.stack.push(self.container.maze_wall[y_index][x_index])
        self.visited.append(self.stack.top())
        if self.stack.size() > self.largestStack and (self.largestStackLocation[0] < x_index
                                                      or self.largestStackLocation[1] < y_index):
            self.largestStack = self.stack.size()
            self.largestStackLocation = (x_index, y_index)

        for i in range(3):
            random_neighbor_direction = self.pick_direction(directions_list)
            if random_neighbor_direction is not None:
                self.remove_walls(random_neighbor_direction)
                neighbor_x_index, neighbor_y_index = self.neighbor(random_neighbor_direction)
                self.maze_algorithm(neighbor_x_index, neighbor_y_index, ["LEFT", "RIGHT", "UP", "DOWN"])
        self.stack.pop()

    def neighbor(self, direction):
        x_index = None
        y_index = None
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
            self.container.maze_wall[y_index][x_index].right_wall = False
        if direction == 'RIGHT':
            current_maze_wall.right_wall = False
            self.container.maze_wall[y_index][x_index].left_wall = False
        if direction == 'UP':
            current_maze_wall.top_wall = False
            self.container.maze_wall[y_index][x_index].bottom_wall = False
        if direction == 'DOWN':
            current_maze_wall.bottom_wall = False
            self.container.maze_wall[y_index][x_index].top_wall = False

    def pick_direction(self, direction):
        random_direction = random.sample(direction, 1)
        direction.remove(random_direction[0])
        if self.is_valid_move(random_direction[0]):
            return random_direction[0]
        else:
            return None

    def is_valid_move(self, direction):
        x_index, y_index = self.neighbor(direction)
        if x_index in range(0, self.row_container_length) and y_index in range(0, self.col_container_length) \
                and self.container.maze_wall[y_index][x_index] not in self.visited:
            return True
        else:
            return False
