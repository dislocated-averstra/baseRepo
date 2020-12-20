from Python.AdventureGame.GameObject.game_object import GameBaseObject


class Player( GameBaseObject):
    horizontal_directions = []
    vertical_directions = []

    def __init__(self, x_position, y_position, size):
        # GameObject__init__(self, x_position, y_position)
        self.size = size
        super().__init__(x_position, y_position)



    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def get_horizontal_directions(self):
        return self.horizontal_directions

    def add_horizontal_direction(self, direction):
       if direction not in self.horizontal_directions:
           self.horizontal_directions.insert(0, direction)

    def remove_horizontal_direction(self, direction):
        self.horizontal_directions.remove(direction)

    def get_vertical_directions(self):
        return self.vertical_directions

    def add_vertical_direction(self, direction):
        if direction not in self.vertical_directions:
            self.vertical_directions.insert(0, direction)

    def remove_vertical_direction(self, direction):
        self.vertical_directions.remove(direction)

    def get_current_direction(self):
        if len(self.horizontal_directions) == 0 and len(self.vertical_directions) == 0:
            return None, None
        elif len(self.horizontal_directions) != 0 and len(self.vertical_directions) == 0:
            return self.horizontal_directions[0], None
        elif len(self.horizontal_directions) == 0 and len(self.vertical_directions) != 0:
            return None, self.vertical_directions[0]
        else:
            return self.horizontal_directions[0], self.vertical_directions[0]

    def move_player(self, window_height, window_width):
        horizontal_direction, vertical_direction = self.get_current_direction()
        if horizontal_direction is None and vertical_direction is not None:
            if vertical_direction == 'UP' and self.get_y_position() - 2 > 0:
                self.set_y_position(self.get_y_position() - 2)
            if vertical_direction == 'DOWN' and self.get_y_position() + 2 < (window_height - self.size):
                self.set_y_position(self.get_y_position() + 2)
        elif horizontal_direction is not None and vertical_direction is None:
            if horizontal_direction == 'LEFT' and self.get_x_position() - 2 > 0:
                self.set_x_position(self.get_x_position() - 2)
            if horizontal_direction == 'RIGHT' and self.get_x_position() + 2 < (window_width - self.size):
                self.set_x_position(self.get_x_position() + 2)
        elif horizontal_direction is not None and vertical_direction is not None:
            if vertical_direction == 'UP' and self.get_y_position() - 1 > 0:
                self.set_y_position(self.get_y_position() - 1)
            if vertical_direction == 'DOWN' and self.get_y_position() + 1 < (window_height - self.size):
                self.set_y_position(self.get_y_position() + 1)
            if horizontal_direction == 'LEFT' and self.get_x_position() - 1 > 0:
                self.set_x_position(self.get_x_position() - 1)
            if horizontal_direction == 'RIGHT' and self.get_x_position() + 1 < (window_width - self.size):
                self.set_x_position(self.get_x_position() + 1)


    def to_string(self):
        return 'X position: %s, Y position: %s' % (self.x_position, self.y_position)
