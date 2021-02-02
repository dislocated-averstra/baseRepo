PLAYER_SIZE = 20
SPRITE_SIZE = 32
class GameBaseObject:

    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

    def get_x_position(self):
        return self.x_position

    def get_y_position(self):
        return self.y_position

    def set_x_position(self, x_position):
        self.x_position = x_position

    def set_y_position(self, y_position):
        self.y_position = y_position

    def hello_bounce(self,func):
        greeting_1 =func(self.bounce_call_function)

    def hello_stop_key(self,func):
        greeting_2=(self.stop_use_key_call_func)

    def did_player_hit_wall(self,board, player_x_position, player_y_position):
        '''Checks if the player hit the wall.'''
        x_index = player_x_position // SPRITE_SIZE
        y_index = player_y_position // SPRITE_SIZE

        if x_index == 0 and y_index == 0:  # top left
            for i in range(0, 2):
                for q in range(0, 2):
                    self.stop_use_key_call_func(board, player_x_position, player_y_position, i, q)
        elif x_index == 0 and y_index != 23:  # left side
            for i in range(0, 2):
                for q in range(y_index - 1, y_index + 2):
                    self.stop_use_key_call_func(board, player_x_position, player_y_position, i, q)
        elif x_index == 31 and y_index == 0:  # top right
            for i in range(x_index - 1, x_index + 1):
                for q in range(y_index - 1, y_index + 2):
                    self.stop_use_key_call_func(board, player_x_position, player_y_position, i, q)
        elif y_index == 0 and x_index != 31:  # top side
            for i in range(x_index - 1, x_index + 2):
                for q in range(0, y_index + 2):
                    self.stop_use_key_call_func(board, player_x_position, player_y_position, i, q)
        elif x_index == 31 and y_index != 23:  # right side
            for i in range(x_index - 1, x_index + 1):
                for q in range(y_index - 1, y_index + 2):
                    self.stop_use_key_call_func(board, player_x_position, player_y_position, i, q)
        elif y_index == 23 and x_index != 31:  # bottom side
            for i in range(x_index - 1, x_index + 2):
                for q in range(y_index - 1, y_index + 1):
                    self.stop_use_key_call_func(board, player_x_position, player_y_position, i, q)
        elif x_index == 31 and y_index == 23:  # bottom right
            for i in range(30, 32):
                for q in range(22, 24):
                    self.stop_use_key_call_func(board, player_x_position, player_y_position, i, q)
        else:  # middle of board
            for i in range(x_index - 1, x_index + 2):
                for q in range(y_index - 1, y_index + 2):
                    self.stop_use_key_call_func(board, player_x_position, player_y_position, i, q)


