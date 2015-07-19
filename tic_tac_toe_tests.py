#! /usr/bin/python3

import tic_tac_toe
import unittest

class TicTacToeTests(unittest.TestCase):
    
    def testNothing(self):
        self.assertTrue(True)

    def testInitBoard(self):
        board = tic_tac_toe.TicTacToe()
        self.assertListEqual(
            [
                ' ', ' ', ' ',
                ' ', ' ', ' ',
                ' ', ' ', ' '
            ],
            board.state)

    def testSetAndGetPosition(self):
        board = tic_tac_toe.TicTacToe()
        self.assertEqual(' ', board.GetPosition(1, 2))
        board.SetPosition('X', 1, 2)
        self.assertEqual('X', board.GetPosition(1, 2))

    def testSetPosition(self):
        board = tic_tac_toe.TicTacToe()
        board.SetPosition('X', 1, 2)

        self.assertListEqual(
            [
                ' ', ' ', ' ',
                ' ', ' ', 'X',
                ' ', ' ', ' '
            ],
            board.state)

    def testSetPositionOutOfBounds(self):
        pass

    def testRenderEmptyBoard(self):
        board = tic_tac_toe.TicTacToe()

        self.assertMultiLineEqual(
            "   |   |   \n"
            "   |   |   \n"
            "   |   |   \n"
            "---+---+---\n"
            "   |   |   \n"
            "   |   |   \n"
            "   |   |   \n"
            "---+---+---\n"
            "   |   |   \n"
            "   |   |   \n"
            "   |   |   \n",
            board.RenderBoard())

    def testRenderBoard(self):
        board = tic_tac_toe.TicTacToe()
        
        board.SetPosition('X', 1, 0)

        self.assertMultiLineEqual(
            "   |   |   \n"
            "   |   |   \n"
            "   |   |   \n"
            "---+---+---\n"
            "   |   |   \n"
            " X |   |   \n"
            "   |   |   \n"
            "---+---+---\n"
            "   |   |   \n"
            "   |   |   \n"
            "   |   |   \n",
            board.RenderBoard())

    def testWinnerEmptyBoardIsNone(self):
        board = tic_tac_toe.TicTacToe()
        
        self.assertEqual(None, board.Winner())
            
    def testGameOverEmptyBoard(self):
        board = tic_tac_toe.TicTacToe()
        
        self.assertFalse(board.GameOver())

    def testGameOverStalemate(self):
        board = tic_tac_toe.TicTacToe()
        
        board.SetPosition('X', 0, 0)
        board.SetPosition('O', 0, 1)
        board.SetPosition('X', 0, 2)
        board.SetPosition('O', 1, 0)
        board.SetPosition('X', 1, 1)
        board.SetPosition('O', 1, 2)
        board.SetPosition('X', 2, 0)
        board.SetPosition('O', 2, 1)
        board.SetPosition('X', 2, 2)

        self.assertTrue(board.GameOver())

    def testIfXWinner(self):
        board = tic_tac_toe.TicTacToe()
        
        board.SetPosition('X', 0, 0)
        board.SetPosition('O', 0, 1)
        board.SetPosition('X', 0, 2)
        board.SetPosition('O', 1, 0)
        board.SetPosition('X', 1, 1)
        board.SetPosition('X', 1, 2)
        board.SetPosition('X', 2, 0)
        board.SetPosition('O', 2, 1)
        board.SetPosition('X', 2, 2)

        self.assertEqual(board.Winner(), "X" )
        
    def testIfOWinner(self):
        board = tic_tac_toe.TicTacToe()
        
        board.SetPosition('X', 0, 0)
        board.SetPosition('O', 0, 1)
        board.SetPosition('X', 0, 2)
        board.SetPosition('O', 1, 0)
        board.SetPosition('O', 1, 1)
        board.SetPosition('O', 1, 2)
        board.SetPosition('X', 2, 0)
        board.SetPosition('O', 2, 1)
        board.SetPosition('X', 2, 2)

        self.assertEqual(board.Winner(), "O" )
        
    def testIfNoWinner(self):
        board = tic_tac_toe.TicTacToe()
        
        board.SetPosition('X', 0, 0)
        board.SetPosition('O', 0, 1)
        board.SetPosition('O', 0, 2)
        board.SetPosition('O', 1, 0)
        board.SetPosition('X', 1, 1)
        board.SetPosition('X', 1, 2)
        board.SetPosition('O', 2, 0)
        board.SetPosition('X', 2, 1)
        board.SetPosition('O', 2, 2)

        self.assertEqual(board.Winner(), None)
        
    def testIfTwoWinners(self):
        board = tic_tac_toe.TicTacToe()
        
        board.SetPosition('X', 0, 0)
        board.SetPosition('X', 0, 1)
        board.SetPosition('X', 0, 2)
        board.SetPosition('O', 1, 0)
        board.SetPosition('O', 1, 1)
        board.SetPosition('O', 1, 2)
        board.SetPosition(' ', 2, 0)
        board.SetPosition(' ', 2, 1)
        board.SetPosition(' ', 2, 2)

        self.assertEqual(board.Winner(), None)
        
class MainTest(unittest.TestCase):
    def testMain(self):
        tic_tac_toe.main()

if __name__ == '__main__':
    unittest.main()
