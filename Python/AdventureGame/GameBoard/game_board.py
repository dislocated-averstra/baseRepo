# this is just a class that will contain the sprites that will need to appear at a given game location
class GameBoard:
    # this will be the board based on the width and height we will add a list to it for each column
    board = []

    def __init__(self, width, height):
        '''Create the board and store the width and height for future use'''
        self.width = width
        self.height = height
        for i in range(0, width):
            self.board.append([])

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_board(self):
        return self.board

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def add_to_board(self, width_index, board_piece):
        self.board[width_index].append(board_piece)

    def add_to_gameboard(self, width_index, height_index, string):
        self.board[width_index].insert(height_index, string)

    def remove_element(self, width_index, height_index, string):
        self.board[width_index].remove(string)

    def remove_item(self,width_index, height_index):
        self.board[width_index][height_index]=""
