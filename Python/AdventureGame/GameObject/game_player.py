class Player:
    move = None

    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

    def get_x_position(self):
        return self.x_position

    def get_y_position(self):
        return self.y_position

    def get_move(self):
        return self.move

    def set_x_position(self, x_position):
        self.x_position = x_position

    def set_y_position(self, y_position):
        self.y_position = y_position

    def set_move(self, move):
        self.move = move

    def to_string(self):
        return 'X position: %s, Y position: %s' % (self.x_position, self.y_position)
