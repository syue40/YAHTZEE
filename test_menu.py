"""
Unittests for the function def menu
"""
import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import menu


class TestMenu(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_print(self, mock_stdout):
        expected = ("\nWELCOME TO MY MINI YAHTZEE!!! I hope you'll enjoy your time here!\n"
                    "Let me just go over some ground rules on how you'll use this program. :)\n\n"
                    "So, when you start the game you'll roll some dice. They'll be displayed in the format: "
                    "\n\n[3, 2, 4, 1, 6]\n\n"
                    "You may want to reroll some of those dice.\nTo do this, select which dice you want to change by "
                    "picking their position in the list!\n"
                    "For example if I want to reroll 3, 4, and 6, then I would type in 1 3 5 corresponding to their "
                    "positions!\n"
                    "\nMake sure to separate the dice you want to reroll with a space, or I'll have to ask you to do "
                    "it again.\n"
                    "Oh and you only get a total of 3 rolls! So choose carefully!\n\n"
                    "Then you'll select a category to score! Your options will be numbered from 1 to 13.\n"
                    "\nThe object of the game for both players is to end the game with the highest score!\n"
                    "Good luck, have fun, and may the best YAHTZEE'er win!\n\n\n")
        menu()
        self.assertEqual(mock_stdout.getvalue(), expected)
