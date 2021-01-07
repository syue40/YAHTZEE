"""
Unittests for the function def get_score_to_update
"""
import io
from unittest import TestCase
from unittest.mock import patch

from yahtzee import select_score_category


class TestGetScoreToUpdate(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_get_score_to_update_ones(self, mock_input):
        expected = 1
        actual = select_score_category()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['13'])
    def test_get_score_to_update_yahtzee(self, mock_input):
        expected = 13
        actual = select_score_category()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['14', '1'])
    def test_get_score_to_update_out_of_integer_range(self, mock_input, mock_output):
        expected = "Please assign the score to a value between 1 and 13!\n"
        select_score_category()
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['0', '1'])
    def test_get_score_to_update_out_of_integer_range_zero(self, mock_input, mock_output):
        expected = "Please assign the score to a value between 1 and 13!\n"
        select_score_category()
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['-3', '1'])
    def test_get_score_to_update_out_of_integer_range_negative(self, mock_input, mock_output):
        expected = "Please assign the score to a value between 1 and 13!\n"
        select_score_category()
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['ab', '1'])
    def test_get_score_to_update_not_a_number(self, mock_input, mock_output):
        expected = "That's not an acceptable value.\n"
        select_score_category()
        self.assertEqual(mock_output.getvalue(), expected)