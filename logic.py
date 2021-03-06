import random
import numpy as np


class Board:

    def __init__(self):
        self.board = np.zeros((4, 4), dtype='int32')
        self.empty_list = []

        # generating random numbers in board
        for _ in range(2):
            self.generate_random()

    # for right
    def compress(self):

        change = False
        for _ in range(3):
            for x in range(4):
                for y in range(3):
                    if self.board[x][y] != 0:
                        if self.board[x][y + 1] == 0:
                            self.board[x][y + 1] = self.board[x][y]
                            self.board[x][y] = 0
                            change = True
        return change

    # for right
    def merge(self):
        change = False
        for x in range(4):
            for y in reversed(range(3)):
                if self.board[x][y] != 0:
                    if self.board[x][y] == self.board[x][y + 1]:
                        self.board[x][y] *= 2
                        self.board[x][y + 1] = 0
                        change = True

    # generate free possibilities
    def empty_spaces(self):

        # resetting list
        self.empty_list = []
        for x in range(4):
            for y in range(4):
                if self.board[x][y] == 0:
                    self.empty_list.append((x, y))
        if len(self.empty_list) == 0:
            return False
        else:
            return True

    def generate_random(self):
        self.empty_spaces()
        if len(self.empty_list) != 0:
            index = random.choice(self.empty_list)
            self.board[index[0]][index[1]] = 2
            return True
        return False

    def right_swipe(self):
        val1 = self.compress()
        self.merge()
        val = self.compress()
        if val or val1:
            self.generate_random()
        return list(filter(None, [val, val1]))

    def left_swipe(self):
        self.board = np.fliplr(self.board)
        val1 = self.compress()
        self.merge()
        val = self.compress()
        if val or val1:
            self.generate_random()
        self.board = np.fliplr(self.board)
        return list(filter(None, [val, val1]))

    def up_swipe(self):
        self.board = np.fliplr(np.transpose(self.board))
        val1 = self.compress()
        self.merge()
        val = self.compress()
        if val or val1:
            self.generate_random()
        self.board = np.transpose(np.fliplr(self.board))
        return list(filter(None, [val, val1]))

    def down_swipe(self):
        self.board = np.transpose(self.board)
        val1 = self.compress()
        self.merge()
        val = self.compress()
        if val or val1:
            self.generate_random()
        self.board = np.transpose(self.board)
        return list(filter(None, [val, val1]))

    def check_win_game_over(self, compress_val):
        if (self.check_all_filled() is True) and (compress_val == []):
            board = self.board
            # checking if all the way it cannot move
            if (self.right_swipe() == []) and (self.up_swipe() == []) and (self.down_swipe() == []) and (
                    self.left_swipe() == []):
                self.board = board
                return False
            self.board = board
            return None

        if 2048 in self.board:
            return True  # ie win
        return None  # ie not win and not lose

    def check_all_filled(self):
        if np.count_nonzero(self.board) == 16:
            return True
        return False
