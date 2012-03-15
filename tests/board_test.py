import unittest
from mock import Mock
from src import board


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board_id = 5
        self.cards = None

    def test_constructor(self):
        test_board = board.Board(self.board_id, self.cards)
        self.assertEqual(test_board.board_id, self.board_id)

