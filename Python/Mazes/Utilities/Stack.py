import pygame

class Stack():
    '''A class to build the mazes.'''

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def top(self):
        if len(self.stack) >= 1:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def pop(self):
        if len(self.stack) >= 1:
            return self.stack.pop()
        else:
            return None

    def push(self, item):
        self.stack.append(item)