"""
Unittests for the function def create_scorecard
"""
from unittest import TestCase
from yahtzee import create_scorecard


class TestCreateScorecard(TestCase):
    def test_create_scorecard(self):
        expected = ({'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '', 'Fives': '', 'Sixes': '', 'Total': 0,
                     'Bonus': 0, 'Three of a kind': '', 'Four of a kind': '', 'Full house': '',
                     'Small straight': '', 'Large straight': '', 'Chance': '', 'YAHTZEE': ''})
        actual = create_scorecard()
        self.assertEqual(actual, expected)
