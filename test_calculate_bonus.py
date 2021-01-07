"""
Unittests for the function def calculate_bonus
"""
from unittest import TestCase
from yahtzee import calculate_bonus


class TestCalculateBonus(TestCase):
    def test_calculate_bonus_all_filled(self):
        scores_diction = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                          'Total': 0, 'Bonus': 35, 'Three of a kind': 21, 'Four of a kind': 27,
                          'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                          'Chance': 17, 'YAHTZEE': 50}
        scores_diction_player_two = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                                     'Total': 0, 'Bonus': 0, 'Three of a kind': 21, 'Four of a kind': 27,
                                     'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                                     'Chance': 17, 'YAHTZEE': 0}
        expected = True
        actual = calculate_bonus(scores_diction, scores_diction_player_two)
        self.assertEqual(actual, expected)

    def test_calculate_bonus_no_calculation_yet_not_all_filled(self):
        scores_diction = {'Ones': '', 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                          'Total': 0, 'Bonus': 35, 'Three of a kind': 21, 'Four of a kind': 27,
                          'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                          'Chance': 17, 'YAHTZEE': 50}
        scores_diction_player_two = {'Ones': '', 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                                     'Total': 0, 'Bonus': 0, 'Three of a kind': 21, 'Four of a kind': 27,
                                     'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                                     'Chance': 17, 'YAHTZEE': 0}
        expected = False
        actual = calculate_bonus(scores_diction, scores_diction_player_two)
        self.assertEqual(actual, expected)

    def test_calculate_bonus_no_calculation_yet_not_all_filled_player_one(self):
        scores_diction = {'Ones': '', 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                          'Total': 0, 'Bonus': 35, 'Three of a kind': 21, 'Four of a kind': 27,
                          'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                          'Chance': 17, 'YAHTZEE': 50}
        scores_diction_player_two = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                                     'Total': 0, 'Bonus': 0, 'Three of a kind': 21, 'Four of a kind': 27,
                                     'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                                     'Chance': 17, 'YAHTZEE': 0}
        expected = False
        actual = calculate_bonus(scores_diction, scores_diction_player_two)
        self.assertEqual(actual, expected)

    def test_calculate_bonus_no_calculation_yet_not_all_filled_player_two(self):
        scores_diction = {'Ones': 3, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                          'Total': 0, 'Bonus': 35, 'Three of a kind': 21, 'Four of a kind': 27,
                          'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                          'Chance': 17, 'YAHTZEE': 50}
        scores_diction_player_two = {'Ones': '', 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 12,
                                     'Total': 0, 'Bonus': 0, 'Three of a kind': 21, 'Four of a kind': 27,
                                     'Full house': 25, 'Small straight': 30, 'Large straight': 40,
                                     'Chance': 17, 'YAHTZEE': 0}
        expected = False
        actual = calculate_bonus(scores_diction, scores_diction_player_two)
        self.assertEqual(actual, expected)