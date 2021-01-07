"""
Unittests for the function def get_player_option
"""
import io
import unittest
from unittest import TestCase
from unittest.mock import patch

from yahtzee import get_player_option


class TestGettingOption(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_get_player_option_continue(self, mock_input):
        expected = 1
        actual = get_player_option()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_get_player_option_quit(self, mock_input):
        with self.assertRaises(SystemExit) as cm:
            get_player_option()
        self.assertEqual(cm.exception.code, None)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3', '1'])
    def test_get_player_option_invalid_number(self, mock_input, mock_output):
        expected = "Please enter either a 1 or 2.\n"
        get_player_option()
        self.assertEqual(mock_output.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['a', '1'])
    def test_get_player_option_invalid_single_string(self, mock_input, mock_output):
        expected = "That's not a valid input! Please enter either 1 or 2!\n"
        get_player_option()
        self.assertEqual(mock_output.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['ab c', '1'])
    def test_get_player_option_invalid_entry_string(self, mock_input, mock_output):
        expected = "That's not a valid input! Please enter either 1 or 2!\n"
        get_player_option()
        self.assertEqual(mock_output.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3', '2'])
    def test_get_player_option_invalid_number_then_quit(self, mock_input, mock_output):
        expected = "Please enter either a 1 or 2.\n"
        with self.assertRaises(SystemExit) as cm:
            get_player_option()
        self.assertEqual(cm.exception.code, None)
        self.assertEqual(mock_output.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['a', '2'])
    def test_get_player_option_invalid_single_string_then_quit(self, mock_input, mock_output):
        expected = "That's not a valid input! Please enter either 1 or 2!\n"
        with self.assertRaises(SystemExit) as cm:
            get_player_option()
        self.assertEqual(cm.exception.code, None)
        self.assertEqual(mock_output.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['ab c', '2'])
    def test_get_player_option_invalid_entry_string_then_quit(self, mock_input, mock_output):
        expected = "That's not a valid input! Please enter either 1 or 2!\n"
        with self.assertRaises(SystemExit) as cm:
            get_player_option()
        self.assertEqual(cm.exception.code, None)
        self.assertEqual(mock_output.getvalue(), expected)
