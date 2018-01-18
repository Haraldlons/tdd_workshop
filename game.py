import numpy as np

ROWS = 3
COLUMNS = 3
WIN_CONDITION = ROWS

def checkIfInBounds(row, column):
    if row >= 0 and column >= 0:
        if row < ROWS and column < COLUMNS:
            return True
    return False


class Board(object):

    def __init__(self):
        self.board = np.zeros((ROWS, COLUMNS))

    def place(self, row, column, value):

        if (value == 1 or value == -1) and checkIfInBounds(row, column):
            self.board[row][column] = value
            return True
        else:
            return False

    def isFull(self):
        for row in range(ROWS):
            for column in range(COLUMNS):
                if self.board[row][column] == 0:
                    return False
        return True

    def checkIfWinHorizontal(self):
        for row in range(ROWS):
            if np.sum(self.board[row,:]) == WIN_CONDITION:
                return 1
            elif np.sum(self.board[row,:]) == -WIN_CONDITION:
                return 2
        return 0

    def checkIfWinVertical(self):
        for column in range(COLUMNS):
            if np.sum(self.board[:,column]) == WIN_CONDITION:
                return 1
            elif np.sum(self.board[:,column]) == -WIN_CONDITION:
                return 2
        print("SUM: ")
        print(np.sum(self.board[:][0]))
        return 0

    def checkIfWinDiagonal(self):

    def checkIfWin():
        if checkIfWinVertical == 2:
