import unittest
import game
import numpy as np

class TestClass(unittest.TestCase):

    def test_checkIfInBounds_forLowerBoundry(self):
        expected = False
        self.assertEqual(expected, game.checkIfInBounds(-1, 1))
        self.assertEqual(expected, game.checkIfInBounds(1, -1))

    def test_checkIfInBounds_insideBoundry(self):
        self.assertEqual(True, game.checkIfInBounds(game.ROWS-1,game.ROWS-1))
        self.assertEqual(True, game.checkIfInBounds(game.ROWS-2,game.ROWS-2))

    def test_checkIfInBounds_forHigherBoundry(self):
        self.assertEqual(False, game.checkIfInBounds(game.ROWS + 1,game.ROWS))
        self.assertEqual(False, game.checkIfInBounds(game.ROWS,game.ROWS-2))
        self.assertEqual(False, game.checkIfInBounds(game.ROWS-2,game.ROWS+2))

    def test_initObject(self):
        brett = game.Board()
        self.assertEqual(True, np.array_equal(np.zeros((game.ROWS, game.COLUMNS)), brett.board))

    def test_placePiece(self):
        brett = game.Board()
        brett.place(0,0,1)
        self.assertEqual(1,brett.board[0][0])

    def test_placePiece_correctValue(self):
        brett = game.Board()

        self.assertEqual(True, brett.place(0,0,1))
        self.assertEqual(True, brett.place(0,0,-1))

    def test_placePiece_incorrectValue(self):
        brett = game.Board()

        self.assertEqual(False, brett.place(0,0,2))

    def test_checkIfFull_forFull(self):
        brett = game.Board()
        for row in range(game.ROWS):
            for column in range(game.COLUMNS):
                brett.place(row, column, 1)

        self.assertEqual(True, brett.isFull())

    def test_checkIfWinHorizontal_first_row(self):
        brett = game.Board()
        for column in range(game.COLUMNS):
            brett.place(0, column, 1)
        self.assertEqual(1, brett.checkIfWinHorizontal())
        brett.place(0,0,-1)
        self.assertEqual(0, brett.checkIfWinHorizontal())

    def test_checkIfWinHorizontal_second_row(self):
        brett = game.Board()
        for column in range(game.COLUMNS):
            brett.place(1, column, 1)
        self.assertEqual(1, brett.checkIfWinHorizontal())

    def test_checkIfWinHorizontal_second_row_player_2_win(self):
        brett = game.Board()
        for column in range(game.COLUMNS):
            brett.place(1, column, -1)
        self.assertEqual(2, brett.checkIfWinHorizontal())

    def test_checkIfWinHorizontal_noWin(self):
        brett = game.Board()
        for column in range(game.COLUMNS):
            brett.place(1, column, 0)
        self.assertEqual(0, brett.checkIfWinHorizontal())

    def test_checkIfWinVertical_first_column(self):
        brett = game.Board()
        for row in range(game.ROWS):
            brett.place(row, 0, 1)
        self.assertEqual(1, brett.checkIfWinVertical())

    def test_checkIfWinVertical_third_column_player_1_win(self):
        brett = game.Board()
        for row in range(game.ROWS):
            brett.place(row, 2, 1)
        self.assertEqual(1, brett.checkIfWinVertical())

    def test_checkIfWinVertical_third_column_player_2_win(self):
        brett = game.Board()
        for row in range(game.ROWS):
            brett.place(row, 2, -1)
        self.assertEqual(2, brett.checkIfWinVertical())

    def test_checkIfWinVertical_noWin(self):
        brett = game.Board()
        for row in range(game.ROWS):
            brett.place(row, 0, 0)
        self.assertEqual(0, brett.checkIfWinVertical())


    def test_checkIfWinDiagonal_Win (self):
        brett = game.Board()
        for diagonal in range(game.ROWS):
            brett.place(diagonal, diagonal, 1)
        self.assertEqual(1, brett.checkIfWinDiagonal)




if __name__ == '__main__':
    unittest.main()
