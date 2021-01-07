"""
Unittests for the function def make_scorecard_pretty
"""
import io
import unittest
from unittest import TestCase
from unittest.mock import patch
from yahtzee import make_scorecard_pretty


class printPrettyScorecard(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_pretty_scorecard(self, mock_stdout):
        scores_diction = {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '', 'Fives': '', 'Sixes': '',
                          'Total': 0, 'Bonus': 0, 'Three of a kind': '', 'Four of a kind': '',
                          'Full house': '', 'Small straight': '', 'Large straight': '',
                          'Chance': '', 'YAHTZEE': ''}
        scores_diction_player_two = {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '', 'Fives': '', 'Sixes': '',
                                     'Total': 0, 'Bonus': 0, 'Three of a kind': '', 'Four of a kind': '',
                                     'Full house': '', 'Small straight': '', 'Large straight': '',
                                     'Chance': '', 'YAHTZEE': ''}
        expected = (f"    *Yahtzee Scorecard*\n"
                    f"|     Top Half Scores     |\n"
                    f"|-------------------------|\n"
                    f"| Player One | Player Two |\n"
                    f"|-------------------------|\n"
                    f"| Ones: {scores_diction['Ones']}    | Ones: {scores_diction_player_two['Ones']}\n"
                    f"| Twos: {scores_diction['Twos']}    | Twos: {scores_diction_player_two['Twos']}\n"
                    f"| Threes: {scores_diction['Threes']}  | Threes: {scores_diction_player_two['Threes']}\n"
                    f"| Fours: {scores_diction['Fours']}   | Fours: {scores_diction_player_two['Fours']}\n"
                    f"| Fives: {scores_diction['Fives']}   | Fives: {scores_diction_player_two['Fives']}\n"
                    f"| Sixes: {scores_diction['Sixes']}   | Sixes: {scores_diction_player_two['Sixes']}\n"
                    f"|-------------------------|\n"
                    f"| Bonus: {scores_diction['Bonus']}  | Bonus: {scores_diction_player_two['Bonus']}\n"
                    f"|-------------------------|\n"
                    f"|           Lower Half Scores             |\n"
                    f"|-----------------------------------------|\n"
                    f"| Three of a kind: {scores_diction['Three of a kind']} | Three of a kind: \
{scores_diction_player_two['Three of a kind']}\n"
                    f"| Four of a kind: {scores_diction['Four of a kind']}  | Four of a kind: \
{scores_diction_player_two['Four of a kind']}\n"
                    f"| Full house: {scores_diction['Full house']}      | Full house: \
{scores_diction_player_two['Full house']}\n"
                    f"| Small straight: {scores_diction['Small straight']}  | Small straight: \
{scores_diction_player_two['Small straight']}\n"
                    f"| Large straight: {scores_diction['Large straight']}  | Large straight: \
{scores_diction_player_two['Large straight']}\n"
                    f"| Chance: {scores_diction['Chance']}          | Chance: \
{scores_diction_player_two['Chance']}\n"
                    f"| YAHTZEE: {scores_diction['YAHTZEE']}         | YAHTZEE: \
{scores_diction_player_two['YAHTZEE']}\n"
                    f"|-----------------------------------------|\n\n")
        make_scorecard_pretty(scores_diction, scores_diction_player_two)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_pretty_scorecard_filled_values(self, mock_stdout):
        scores_diction = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                          'Total': 0, 'Bonus': 35, 'Three of a kind': 21, 'Four of a kind': 27,
                          'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                          'Chance': 17, 'YAHTZEE': 50}
        scores_diction_player_two = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                                     'Total': 0, 'Bonus': 0, 'Three of a kind': 21, 'Four of a kind': 27,
                                     'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                                     'Chance': 17, 'YAHTZEE': 0}
        expected = (f"    *Yahtzee Scorecard*\n"
                    f"|     Top Half Scores     |\n"
                    f"|-------------------------|\n"
                    f"| Player One | Player Two |\n"
                    f"|-------------------------|\n"
                    f"| Ones: {scores_diction['Ones']}    | Ones: {scores_diction_player_two['Ones']}\n"
                    f"| Twos: {scores_diction['Twos']}    | Twos: {scores_diction_player_two['Twos']}\n"
                    f"| Threes: {scores_diction['Threes']}  | Threes: {scores_diction_player_two['Threes']}\n"
                    f"| Fours: {scores_diction['Fours']}   | Fours: {scores_diction_player_two['Fours']}\n"
                    f"| Fives: {scores_diction['Fives']}   | Fives: {scores_diction_player_two['Fives']}\n"
                    f"| Sixes: {scores_diction['Sixes']}   | Sixes: {scores_diction_player_two['Sixes']}\n"
                    f"|-------------------------|\n"
                    f"| Bonus: {scores_diction['Bonus']}  | Bonus: {scores_diction_player_two['Bonus']}\n"
                    f"|-------------------------|\n"
                    f"|           Lower Half Scores             |\n"
                    f"|-----------------------------------------|\n"
                    f"| Three of a kind: {scores_diction['Three of a kind']} | Three of a kind: \
{scores_diction_player_two['Three of a kind']}\n"
                    f"| Four of a kind: {scores_diction['Four of a kind']}  | Four of a kind: \
{scores_diction_player_two['Four of a kind']}\n"
                    f"| Full house: {scores_diction['Full house']}      | Full house: \
{scores_diction_player_two['Full house']}\n"
                    f"| Small straight: {scores_diction['Small straight']}  | Small straight: \
{scores_diction_player_two['Small straight']}\n"
                    f"| Large straight: {scores_diction['Large straight']}  | Large straight: \
{scores_diction_player_two['Large straight']}\n"
                    f"| Chance: {scores_diction['Chance']}          | Chance: \
{scores_diction_player_two['Chance']}\n"
                    f"| YAHTZEE: {scores_diction['YAHTZEE']}         | YAHTZEE: \
{scores_diction_player_two['YAHTZEE']}\n"
                    f"|-----------------------------------------|\n\n")
        make_scorecard_pretty(scores_diction, scores_diction_player_two)
        self.assertEqual(mock_stdout.getvalue(), expected)
