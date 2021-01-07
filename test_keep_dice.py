"""
Unittests for the function def kept_die
"""
import io
from unittest import TestCase, mock
from unittest.mock import patch

from yahtzee import keep_dice


class TestKeepDice(TestCase):
    @patch('builtins.input', side_effect=['1 2 3 4 5'])
    @patch("random.randint", new=mock.Mock(return_value=1))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_kept_die(self, mock_output, mock_input):
        expected = "Your hand is now [1, 1, 1, 1, 1]\n"
        final_hand = [1, 2, 3, 4, 5]
        with self.assertRaises(StopIteration):
            keep_dice(final_hand)
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', side_effect=['1 2 3 4 5'])
    @patch("random.randint", new=mock.Mock(return_value=2))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_kept_die_different_values(self, mock_output, mock_input):
        expected = "Your hand is now [2, 2, 2, 2, 2]\n"
        final_hand = [3, 2, 4, 5, 4]
        with self.assertRaises(StopIteration):
            keep_dice(final_hand)
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', side_effect=['1 2 3 4 5'])
    @patch("random.randint", new=mock.Mock(return_value=3))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_kept_die_other_values(self, mock_output, mock_input):
        expected = "Your hand is now [3, 3, 3, 3, 3]\n"
        final_hand = [6, 1, 2, 4, 5]
        with self.assertRaises(StopIteration):
            keep_dice(final_hand)
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', side_effect=['a'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_kept_die_invalid_string(self, mock_output, mock_input):
        expected = "That doesn't work!\n"
        final_hand = [6, 1, 2, 4, 5]
        with self.assertRaises(StopIteration):
            keep_dice(final_hand)
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', side_effect=['7'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_kept_die_outside_index_range(self, mock_output, mock_input):
        expected = "Not a valid index\n"
        final_hand = [6, 1, 2, 4, 5]
        with self.assertRaises(StopIteration):
            keep_dice(final_hand)
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_kept_die_blank_string(self, mock_output, mock_input):
        expected = "Your hand is now [6, 1, 2, 4, 5]\n"
        final_hand = [6, 1, 2, 4, 5]
        with self.assertRaises(StopIteration):
            keep_dice(final_hand)
        self.assertEqual(mock_output.getvalue(), expected)
