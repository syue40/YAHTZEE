"""
Unittests for the function def quit_game
"""
from unittest import TestCase
from yahtzee import quit_game


class quittingGame(TestCase):
    def test_quit_game(self):
        with self.assertRaises(SystemExit) as cm:
            quit_game()
        self.assertEqual(cm.exception.code, None)
