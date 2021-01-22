from Python.AdventureGame.GameObject.game_object import GameBaseObject


class Enemy(GameBaseObject):
    directions = ["LEFT"]
    horizontal_directions = []
    vertical_directions = []

    def __init__(self, x_position, y_position, size):
        self.size = size
        super().__init__(x_position, y_position)

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def get_directions(self):
        return self.directions

    def set_direction(self, move):
        self.move = move

    def get_horizontal_directions(self):
        return self.horizontal_directions

    def get_vertical_directions(self):
        return self.vertical_directions

    def add_direction(self, direction):
        if direction not in self.directions:
            self.directions.insert(0, direction)

    def remove_direction(self, direction):
        self.directions.remove(direction)

    def get_current_direction(self):
        if len(self.directions) == 0:
            return None
        else:
            return self.directions[0]

    def remove_horizontal_direction(self, direction):
        self.horizontal_directions.remove(direction)

    def remove_vertical_direction(self, direction):
        self.vertical_directions.remove(direction)

    def move_enemy(self, window_height, window_width):

        if self.directions[0] == "LEFT" and self.get_x_position() - 2 > 0:
            self.set_x_position(self.get_x_position() - 2)
            if self.get_x_position() == 32:
                self.remove_direction("LEFT")
                self.directions.append("RIGHT")

        if self.directions[0] == "RIGHT" and self.get_x_position() + 2 < (window_width - self.size):
            self.set_x_position(self.get_x_position() + 2)
            if self.get_x_position() == 900:
                self.remove_direction("RIGHT")
                self.directions.append("DOWN")

        if self.directions[0] == 'DOWN' and self.get_y_position() + 2 < (window_height - self.size):
            self.set_y_position(self.get_y_position() + 2)
            if self.get_y_position() == 500:
                self.remove_direction("DOWN")
                self.directions.append("UP")

        if self.directions[0] == 'UP' and self.get_y_position() -2>0:
            self.set_y_position(self.get_y_position() - 2)
            if self.get_y_position() == 300:
                self.remove_direction("UP")
                self.directions.append("LEFT")

    def to_string(self):
        return 'X position: %s, Y position: %s' % (self.x_position, self.y_position)
