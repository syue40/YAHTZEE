"""
Unittests for the function def declare_winner
"""
import io
from unittest import TestCase
from unittest.mock import patch

from yahtzee import declare_winner


class TestDeclareWinner(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_declare_winner_player_one_wins(self, mock_output):
        scores_diction = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                          'Total': 0, 'Bonus': 35, 'Three of a kind': 21, 'Four of a kind': 27,
                          'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                          'Chance': 17, 'YAHTZEE': 50}
        scores_diction_player_two = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                                     'Total': 0, 'Bonus': 0, 'Three of a kind': 21, 'Four of a kind': 27,
                                     'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                                     'Chance': 17, 'YAHTZEE': 0}
        expected = ("THE FINAL SCORE IS: 318 FOR PLAYER ONE! AND 233 FOR PLAYER TWO!\n\n"
                    "PLAYER ONE WINS! BETTER LUCK NEXT TIME PLAYER TWO!\n\n"
                    "Game Over!\n\n")
        with self.assertRaises(SystemExit) as cm:
            declare_winner(scores_diction, scores_diction_player_two)
        self.assertEqual(cm.exception.code, None)
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_declare_winner_player_two_wins(self, mock_output):
        scores_diction_player_two = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                                     'Total': 0, 'Bonus': 35, 'Three of a kind': 21, 'Four of a kind': 27,
                                     'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                                     'Chance': 17, 'YAHTZEE': 50}
        scores_diction = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                          'Total': 0, 'Bonus': 0, 'Three of a kind': 21, 'Four of a kind': 27,
                          'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                          'Chance': 17, 'YAHTZEE': 0}
        expected = ("THE FINAL SCORE IS: 233 FOR PLAYER ONE! AND 318 FOR PLAYER TWO!\n\n"
                    "PLAYER TWO WINS! BETTER LUCK NEXT TIME PLAYER ONE!\n\n"
                    "Game Over!\n\n")
        with self.assertRaises(SystemExit) as cm:
            declare_winner(scores_diction, scores_diction_player_two)
        self.assertEqual(cm.exception.code, None)
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_declare_winner_player_draw(self, mock_output):
        scores_diction_player_two = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                                     'Total': 0, 'Bonus': 35, 'Three of a kind': 21, 'Four of a kind': 27,
                                     'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                                     'Chance': 17, 'YAHTZEE': 50}
        scores_diction = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                          'Total': 0, 'Bonus': 35, 'Three of a kind': 21, 'Four of a kind': 27,
                          'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                          'Chance': 17, 'YAHTZEE': 50}
        expected = ("THE FINAL SCORE IS: 318 FOR PLAYER ONE! AND 318 FOR PLAYER TWO!\n\n"
                    "\nIts a draw! Sorry you had to go out like this...\n\n")
        with self.assertRaises(SystemExit) as cm:
            declare_winner(scores_diction, scores_diction_player_two)
        self.assertEqual(cm.exception.code, None)
        self.assertEqual(mock_output.getvalue(), expected)
