"""
Unittests for the function def roll_die
"""
import io
from unittest import TestCase, mock
from unittest.mock import patch
from yahtzee import roll_die


class TestRollDie(TestCase):
    @patch("random.randint", new=mock.Mock(return_value=1))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_die(self, mock_output):
        expected = [1, 1, 1, 1, 1]
        expected_2 = "You rolled the following: [1, 1, 1, 1, 1]\n"
        actual = roll_die()
        self.assertEqual(actual, expected)
        self.assertEqual(mock_output.getvalue(), expected_2)

    @patch("random.randint", new=mock.Mock(return_value=3))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_die(self, mock_output):
        expected = [3, 3, 3, 3, 3]
        expected_2 = "You rolled the following: [3, 3, 3, 3, 3]\n"
        actual = roll_die()
        self.assertEqual(actual, expected)
        self.assertEqual(mock_output.getvalue(), expected_2)

    @patch("random.randint", new=mock.Mock(return_value=4))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_die(self, mock_output):
        expected = [4, 4, 4, 4, 4]
        expected_2 = "You rolled the following: [4, 4, 4, 4, 4]\n"
        actual = roll_die()
        self.assertEqual(actual, expected)
        self.assertEqual(mock_output.getvalue(), expected_2)
