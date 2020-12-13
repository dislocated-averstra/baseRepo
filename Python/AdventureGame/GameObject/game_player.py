class Player:
    directions = []

    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

    def get_x_position(self):
        return self.x_position

    def get_y_position(self):
        return self.y_position

    def get_directions(self):
        return self.directions

    def set_x_position(self, x_position):
        self.x_position = x_position

    def set_y_position(self, y_position):
        self.y_position = y_position

    def set_direction(self, move):
        self.move = move

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

    def to_string(self):
        return 'X position: %s, Y position: %s' % (self.x_position, self.y_position)
