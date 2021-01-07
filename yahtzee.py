"""
Final Exam

Create a simple text-based Yahtzee game for 2 players
Sean Yue
A01228440
"""
import random
import doctest
import re
from statistics import mode


def menu() -> None:
    """Print a menu with some instructions for the user.

    This function will be the first thing called when the game runs. It will give the user some instructions to use
    the program.

    :param: None
    :precondition: None
    :postcondition: None
    :return: string with program instructions

    >>> menu() # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    WELCOME TO MY MINI YAHTZEE!!! I hope you'll enjoy your time here!
    Let me just go over some ground rules on how you'll use this program. :)
    <BLANKLINE>
    So, when you start the game you'll roll some dice. They'll be displayed in the format:
    <BLANKLINE>
    [3, 2, 4, 1, 6]
    <BLANKLINE>
    You may want to reroll some of those dice.
    To do this, select which dice you want to change by picking their position in the list!
    For example if I want to reroll 3, 4, and 6, then I would type in 1 3 5 corresponding to their positions!
    <BLANKLINE>
    Make sure to separate the dice you want to reroll with a space, or I'll have to ask you to do it again.
    Oh and you only get a total of 3 rolls! So choose carefully!
    <BLANKLINE>
    Then you'll select a category to score! Your options will be numbered from 1 to 13.
    <BLANKLINE>
    The object of the game for both players is to end the game with the highest score!
    Good luck, have fun, and may the best YAHTZEE'er win!
    <BLANKLINE>
    <BLANKLINE>
    """
    print("\nWELCOME TO MY MINI YAHTZEE!!! I hope you'll enjoy your time here!\n"
          "Let me just go over some ground rules on how you'll use this program. :)\n\n"
          "So, when you start the game you'll roll some dice. They'll be displayed in the format: "
          "\n\n[3, 2, 4, 1, 6]\n\n"
          "You may want to reroll some of those dice.\nTo do this, select which dice you want to change by "
          "picking their position in the list!\n"
          "For example if I want to reroll 3, 4, and 6, then I would type in 1 3 5 corresponding to their positions!\n"
          "\nMake sure to separate the dice you want to reroll with a space, or I'll have to ask you to do it again.\n"
          "Oh and you only get a total of 3 rolls! So choose carefully!\n\n"
          "Then you'll select a category to score! Your options will be numbered from 1 to 13.\n"
          "\nThe object of the game for both players is to end the game with the highest score!\n"
          "Good luck, have fun, and may the best YAHTZEE'er win!\n\n")


def create_scorecard() -> dict:
    """Create a dictionary representing the scores for player one.

    This function creates a dictionary with keys representing Yahtzee points categories. These keys have
    empty strings as values to be used for the player 1 scorecard. Another function will
    modify the values in this dictionary when the player scores a category.

    Note: Hi Chris, I decided to keep these string values since I figured it would be easier to check this empty string
    since there are no other instances where it is used. It will also make it easier to print a pretty scorecard!

    :param: None
    :precondition: None
    :postcondition: None
    :return: dictionary of keys representing categories to score with empty strings as values
    >>> create_scorecard()
    {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '', 'Fives': '', 'Sixes': '', 'Total': 0, 'Bonus': 0, \
'Three of a kind': '', 'Four of a kind': '', 'Full house': '', 'Small straight': '', \
'Large straight': '', 'Chance': '', 'YAHTZEE': ''}
    """
    scores_diction = {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '', 'Fives': '', 'Sixes': '', 'Total': 0,
                      'Bonus': 0, 'Three of a kind': '', 'Four of a kind': '', 'Full house': '',
                      'Small straight': '', 'Large straight': '', 'Chance': '', 'YAHTZEE': ''}
    return scores_diction


def create_scorecard_player_two() -> dict:
    """Create a dictionary representing the scores for player two.

    This function creates a dictionary with keys representing Yahtzee points categories. These keys have
    empty strings as values to be used for the player 2 scorecard. Another function will
    modify the values in this dictionary when the player scores a category.

    :param: None
    :precondition: None
    :postcondition: None
    :return: dictionary of keys representing categories to score with empty strings as values

    >>> create_scorecard_player_two()
    {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '', 'Fives': '', 'Sixes': '', 'Total': 0, 'Bonus': 0, \
'Three of a kind': '', 'Four of a kind': '', 'Full house': '', 'Small straight': '', \
'Large straight': '', 'Chance': '', 'YAHTZEE': ''}
    """
    scores_diction_player_two = {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '', 'Fives': '', 'Sixes': '',
                                 'Total': 0, 'Bonus': 0, 'Three of a kind': '', 'Four of a kind': '',
                                 'Full house': '', 'Small straight': '', 'Large straight': '',
                                 'Chance': '', 'YAHTZEE': ''}
    return scores_diction_player_two


def make_scorecard_pretty(scores_diction: dict, scores_diction_player_two: dict):
    """Print a pretty scorecard using scores of player one and two.

    Uses f-strings and the player dictionaries to print a scorecard-format string that resembles the actual
    Yahtzee scorecard. Will likely implement a for loop which formats and prints of every key,value pair in the scores
    dictionary.

    :param scores_diction: a dictionary with the scores of player one
    :param scores_diction_player_two: a dictionary with the scores of player two
    :return: f-string with the updated scores of both players

    >>> scores_diction = {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '', 'Fives': '', 'Sixes': '',\
                                 'Total': 0, 'Bonus': 0, 'Three of a kind': '', 'Four of a kind': '',\
                                 'Full house': '', 'Small straight': '', 'Large straight': '',\
                                 'Chance': '', 'YAHTZEE': ''}
    >>> scores_diction_player_two = {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '', 'Fives': '', 'Sixes': '',\
                                 'Total': 0, 'Bonus': 0, 'Three of a kind': '', 'Four of a kind': '',\
                                 'Full house': '', 'Small straight': '', 'Large straight': '',\
                                 'Chance': '', 'YAHTZEE': ''}
    >>> make_scorecard_pretty(scores_diction, scores_diction_player_two) # doctest: +NORMALIZE_WHITESPACE
        *Yahtzee Scorecard*
    |     Top Half Scores     |
    |-------------------------|
    | Player One | Player Two |
    |-------------------------|
    | Ones:     | Ones:
    | Twos:     | Twos:
    | Threes:   | Threes:
    | Fours:    | Fours:
    | Fives:    | Fives:
    | Sixes:    | Sixes:
    |-------------------------|
    | Bonus: 0  | Bonus: 0
    |-------------------------|
    |           Lower Half Scores             |
    |-----------------------------------------|
    | Three of a kind:  | Three of a kind:
    | Four of a kind:   | Four of a kind:
    | Full house:       | Full house:
    | Small straight:   | Small straight:
    | Large straight:   | Large straight:
    | Chance:           | Chance:
    | YAHTZEE:          | YAHTZEE:
    |-----------------------------------------|
    """
    print(f"    *Yahtzee Scorecard*\n"
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
          f"|-----------------------------------------|\n")


def get_player_option() -> int:
    """Ask the player every round if they want to continue playing or quit.

    Asks the user for input every round on whether they want to keep playing. If the user enters 1
    the turns will continue progressing. If the player enters 2, quit_game will be called. If they enter anything
    else this function will ask again, until a valid entry is provided.

    :param: None
    :precondition: User must enter either 1 or 2
    :postcondition: Continues turns or quits game
    :return: a integer representing the player choice
    """
    try:
        player_choice = int(input("Press 1 to continue game, press 2 to quit.\n").strip())
    except ValueError:
        print("That's not a valid input! Please enter either 1 or 2!")
        return get_player_option()
    else:
        while player_choice != 1 or player_choice != 2:
            if player_choice == 2:
                quit_game()
            elif player_choice == 1:
                return player_choice
            else:
                print("Please enter either a 1 or 2.")
                return get_player_option()


def calculate_bonus(scores_diction: dict, scores_diction_player_two: dict) -> bool:
    """Calculate the sum of the top scorecard to determine whether a bonus is scored.

    Called once all categories for both players are filled out then sums the total of the top half of the scorecard.
    If the total of the top half is greater than 63, then it will modify the value for bonus in the scores dictionaries
    to 35.

    :param scores_diction: a dictionary with the scores of player one
    :param scores_diction_player_two: a dictionary with the scores of player two
    :precondition: must be passed full dictionaries of scores from player one and two (not including bonus)
    :postcondition: calculates if the top half is greater than 63 and modifies the bonus based on calculation
    :return: updated dictionaries with/without bonus scores

    >>> scores_diction = {'Ones': 5, 'Twos': 10, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 30, 'Total': 0,\
                         'Bonus': 0, 'Three of a kind': 25, 'Four of a kind': 25, 'Full house': 25,\
                         'Small straight': 30, 'Large straight': 40, 'Chance': 21, 'YAHTZEE': 0}
    >>> scores_diction_player_two = {'Ones': 5, 'Twos': 10, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 30, \
                            'Total': 0,'Bonus': 0, 'Three of a kind': 25, 'Four of a kind': 25, 'Full house': 25,\
                            'Small straight': 30, 'Large straight': 40, 'Chance': 21, 'YAHTZEE': 0}
    >>> calculate_bonus(scores_diction, scores_diction_player_two)
    True

    >>> scores_diction = {'Ones': '', 'Twos': 10, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 30, 'Total': 0,\
                         'Bonus': 0, 'Three of a kind': 25, 'Four of a kind': 25, 'Full house': 25,\
                         'Small straight': 30, 'Large straight': 40, 'Chance': 21, 'YAHTZEE': 0}
    >>> scores_diction_player_two = {'Ones': 5, 'Twos': 10, 'Threes': 9, 'Fours': 16, 'Fives': 25, 'Sixes': 30, \
                            'Total': 0,'Bonus': 0, 'Three of a kind': 25, 'Four of a kind': 25, 'Full house': 25,\
                            'Small straight': 30, 'Large straight': 40, 'Chance': 21, 'YAHTZEE': 0}
    >>> calculate_bonus(scores_diction, scores_diction_player_two)
    False
    """
    if '' in scores_diction.values() or '' in scores_diction_player_two.values():
        return False
    else:
        scores_diction['Total'] = sum(list(scores_diction.values())[:6])
        scores_diction_player_two['Total'] = sum(list(scores_diction_player_two.values())[:6])

        if scores_diction['Total'] >= 63:
            scores_diction['Bonus'] = 35
        if scores_diction['Total'] < 63:
            scores_diction['Bonus'] = 0

        if scores_diction_player_two['Total'] >= 63:
            scores_diction_player_two['Bonus'] = 35
        if scores_diction_player_two['Total'] < 63:
            scores_diction_player_two['Bonus'] = 0
        return True


def declare_winner(scores_diction: dict, scores_diction_player_two: dict) -> None:
    """Called if all categories for both players are filled out.

    Function is called after all categories have been scored. It will add up the values in the dictionary and determine
    which player has the higher score. It will then print out who wins to the user.

    :param scores_diction: a dictionary with the scores of player one
    :param scores_diction_player_two: a dictionary with the scores of player two
    :precondition: must be passed full dictionaries of scores from player one and two
    :postcondition: sums up values in both dictionaries
    :return: string telling players who won
    """
    grand_total_p1 = sum(scores_diction.values()) - scores_diction['Total']
    grand_total_p2 = sum(scores_diction_player_two.values()) - scores_diction_player_two['Total']
    print(f'THE FINAL SCORE IS: {grand_total_p1} FOR PLAYER ONE! AND {grand_total_p2} FOR PLAYER TWO!\n')
    if grand_total_p2 > grand_total_p1:
        print('PLAYER TWO WINS! BETTER LUCK NEXT TIME PLAYER ONE!\n')
        print('Game Over!\n')
        quit_game()
    elif grand_total_p2 < grand_total_p1:
        print('PLAYER ONE WINS! BETTER LUCK NEXT TIME PLAYER TWO!\n')
        print('Game Over!\n')
        quit_game()
    else:
        print('\nIts a draw! Sorry you had to go out like this...\n')
        quit_game()


def roll_die() -> list:
    """Roll a six sided dice five times. Adds each random number to a list.

    Creates an empty list and appends five values representing five dice rolls to it.

    :param: None
    :precondition: None
    :postcondition: None
    :return: A list containing five random dice rolls
    """
    dice_list = []
    for number_of_dice in range(0, 5):
        roll_dice = random.randint(1, 6)
        dice_list.append(roll_dice)
    print(f"You rolled the following: {dice_list}")
    return dice_list


def keep_dice(dice_list: list) -> list:
    """Allow the user to pick up or reroll certain dice. Or give them the choice to score immediately.

    Gives the user two additional rolls (excluding original roll from roll_die). Will ask the user each roll
    whether they want to continue re-rolling or to score their current dice now. If user continues to roll
    they will type in ints which are used to represent the list positions of the dice they want to re-roll.
    These dice will then be re-rolled. After the user selects score or uses up their rolls this function will return
    a list: final_hand representing the hand the user must score.

    :param dice_list: a list of 5 random dice rolls
    :precondition: the dice_list must contain 5 integers representing the first dice roll
    :postcondition: will go through a while loop to determine the user's final hand to score
    :return: a list containing the dice the user wants to score
    """
    count = 2
    final_hand = dice_list

    while count != 0:
        try:
            reroll = input('Which dice do you want to reroll? Or press 9 to score').split()
            reroll = [int(items) - 1 for items in reroll]
        except ValueError:
            print("That doesn't work!")
        else:
            if reroll == [8]:
                print(f"You selected score! Your final hand is: {final_hand}")
                return final_hand
            else:
                try:
                    for index in reroll:
                        final_hand[index] = random.randint(1, 6)
                    print(f"Your hand is now {final_hand}")
                    count -= 1
                except IndexError:
                    print("Not a valid index")

    print(f"That was your last roll! your final hand is: {final_hand}\n")
    return final_hand


def select_score_category() -> int:
    """Ask user for an int for the category they want to score.

    Function prints a string to tell the user which categories are represented by which ints. Then it will ask the user
    to input a integer for the category and return this integer.

    :param: None
    :precondition: user must enter an integer
    :postcondition: check if the integer is in the range of options
    :return: returns the valid integer: score_to_update
    """
    try:
        score_to_update = int(input("Which box would you like to score?\n"
                                    "\nPress 1 for Ones, 2 for Twos, 3 for Threes\n"
                                    "4 for Fours, 5 for Fives, and 6 for Sixes\n"
                                    "Or press 7 for Three of a Kind\n"
                                    "8 for Four of a kind\n"
                                    "9 for Full house\n"
                                    "10 for Small Straight\n"
                                    "11 for Large Straight\n"
                                    "12 for Chance\n"
                                    "and 13 for YAHTZEE!\n").strip())
    except ValueError:
        print("That's not an acceptable value.")
    else:
        if score_to_update not in range(1, 14):
            print("Please assign the score to a value between 1 and 13!")
            return select_score_category()
        else:
            return score_to_update


def score_category_check(final_hand: list, score_to_update: int, scores_diction: dict) -> None:
    """Control which category function is called based on user input for player one

    Is called by the player_turns function every turn to determine which category the user wants to score. Will also be
    called by the category functions if the user tries to fill a category that is already filled out.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update in range(1, 7):
        update_score(final_hand, score_to_update, scores_diction)
    elif score_to_update == 7 or score_to_update == 8:
        update_score_threes_and_fours(final_hand, score_to_update, scores_diction)
    elif score_to_update == 9:
        update_score_full_house(final_hand, score_to_update, scores_diction)
    elif score_to_update == 10 or score_to_update == 11:
        update_score_straights(final_hand, score_to_update, scores_diction)
    else:
        update_scores_chance_and_yahtzee(final_hand, score_to_update, scores_diction)


def score_category_check_player_two(final_hand: list, score_to_update: int, scores_diction_player_two: dict) -> None:
    """Control which category function is called based on user input for player two

    Is called by the player_turns function every turn to determine which category the user wants to score. Will also be
    called by the category functions if the user tries to fill a category that is already filled out.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction_player_two: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update in range(1, 7):
        update_score_player_two(final_hand, score_to_update, scores_diction_player_two)
    elif score_to_update == 7 or score_to_update == 8:
        update_score_player_two_threes_and_fours(final_hand, score_to_update, scores_diction_player_two)
    elif score_to_update == 9:
        update_score_player_two_full_house(final_hand, score_to_update, scores_diction_player_two)
    elif score_to_update == 10 or score_to_update == 11:
        update_score_player_two_straights(final_hand, score_to_update, scores_diction_player_two)
    else:
        update_score_player_two_chance_and_yahtzee(final_hand, score_to_update, scores_diction_player_two)


def update_score(final_hand: list, score_to_update: int, scores_diction: dict) -> None:
    """Determine whether a category in player one's dictionary can be updated. Updates if possible.

    Called by the score_category_check function, if the user's input is an integer in range 1 to 6. This function takes
    that value and checks if the score is already filled. If filled, it will call the score_category_check
    again to determine a valid user input. Otherwise, it will update the category selected.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update == 1 and scores_diction['Ones'] == '':
        scores_diction['Ones'] = 1 * final_hand.count(1)
    elif score_to_update == 2 and scores_diction['Twos'] == '':
        scores_diction['Twos'] = 2 * final_hand.count(2)
    elif score_to_update == 3 and scores_diction['Threes'] == '':
        scores_diction['Threes'] = 3 * final_hand.count(3)
    elif score_to_update == 4 and scores_diction['Fours'] == '':
        scores_diction['Fours'] = 4 * final_hand.count(4)
    elif score_to_update == 5 and scores_diction['Fives'] == '':
        scores_diction['Fives'] = 5 * final_hand.count(5)
    elif score_to_update == 6 and scores_diction['Sixes'] == '':
        scores_diction['Sixes'] = 6 * final_hand.count(6)
    else:
        print("You can't score that!")
        score_to_update = select_score_category()
        score_category_check(final_hand, score_to_update, scores_diction)


def update_score_threes_and_fours(final_hand: list, score_to_update: int, scores_diction: dict) -> None:
    """Determine whether a category in player one's dictionary can be updated. Updates if possible.

    Called by the score_category_check function, if the user's input is 7 or 8. This function takes
    that value and checks if the score is already filled. If filled, it will call the score_category_check
    again to determine a valid user input. Otherwise, it will update the category selected.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update == 7 and scores_diction['Three of a kind'] == '':
        if final_hand.count(mode(final_hand)) >= 3:
            scores_diction['Three of a kind'] = sum(final_hand)
        else:
            scores_diction['Three of a kind'] = 0
    elif score_to_update == 8 and scores_diction['Four of a kind'] == '':
        if final_hand.count(mode(final_hand)) >= 4:
            scores_diction['Four of a kind'] = sum(final_hand)
        else:
            scores_diction['Four of a kind'] = 0
    else:
        print("You can't score that!")
        score_to_update = select_score_category()
        score_category_check(final_hand, score_to_update, scores_diction)


def update_score_full_house(final_hand: list, score_to_update: int, scores_diction: dict) -> None:
    """Determine whether a category in player one's dictionary can be updated. Updates if possible.

    Called by the score_category_check function, if the user's input was 9. This function takes
    that value and checks if the score has already been filled. If filled, it will call the score_category_check
    again to determine a valid user input. Otherwise, it will update the category selected.

    Note: I really wanted to make this with a regex, I couldn't get it to work, and ran out of time.
    *I should have done the regex lab bonus problem for poker hands*

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update == 9 and scores_diction['Full house'] == '':
        values_div = (str(sorted(final_hand)).strip('[]').replace(', ', ''))
        if (values_div[0:1] == values_div[1:2] == values_div[2:3] and values_div[3:4] == values_div[4:5]) or \
                (values_div[0:1] == values_div[1:2] and values_div[2:3] == values_div[3:4] == values_div[4:5]):
            scores_diction['Full house'] = 25
        else:
            scores_diction['Full house'] = 0
    else:
        print("You can't score that!")
        score_to_update = select_score_category()
        score_category_check(final_hand, score_to_update, scores_diction)


def update_score_straights(final_hand: list, score_to_update: int, scores_diction: dict) -> None:
    """Determine whether a category in player one's dictionary can be updated. Updates if possible.

    Called by the score_category_check function, if the user's input was 10 or 11. This function takes
    that value and checks if the score has already been filled. If filled, it will call the score_category_check
    again to determine a valid user input. Otherwise, it will update the category selected.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    var_for_evaluating_straights = (str(set(sorted(final_hand))).strip('{}')).replace(', ', '')
    if score_to_update == 10 and scores_diction['Small straight'] == '':
        if re.match(r'1234|2345|3456', var_for_evaluating_straights):
            scores_diction['Small straight'] = 30
        else:
            scores_diction['Small straight'] = 0
    elif score_to_update == 11 and scores_diction['Large straight'] == '':
        if re.match(r'12345|23456', var_for_evaluating_straights):
            scores_diction['Large straight'] = 40
        else:
            scores_diction['Large straight'] = 0
    else:
        print("You can't score that!")
        score_to_update = select_score_category()
        score_category_check(final_hand, score_to_update, scores_diction)


def update_scores_chance_and_yahtzee(final_hand: list, score_to_update: int, scores_diction: dict) -> None:
    """Determine whether a category in player one's dictionary can be updated. Updates if possible.

    Called by the score_category_check function, if the user's input was 12 or 13. This function takes
    that value and checks if the score has already been filled. If filled, it will call the score_category_check
    again to determine a valid user input. Otherwise, it will update the category selected.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update == 12 and scores_diction['Chance'] == '':
        scores_diction['Chance'] = sum(final_hand)
    elif score_to_update == 13 and scores_diction['YAHTZEE'] == '':
        if final_hand.count(mode(final_hand)) == 5:
            if scores_diction['YAHTZEE'] == 50 or scores_diction['YAHTZEE'] == 150:
                scores_diction['YAHTZEE'] += 100
            elif scores_diction['YAHTZEE'] == '':
                scores_diction['YAHTZEE'] = 50
        else:
            scores_diction['YAHTZEE'] = 0
    else:
        print("You can't score that!")
        score_to_update = select_score_category()
        score_category_check(final_hand, score_to_update, scores_diction)


def update_score_player_two(final_hand: list, score_to_update: int, scores_diction_player_two: dict) -> None:
    """Determine whether a category can be updated in player two's score dictionary. Updates if possible.

    Called by the score_category_check_player_two function, if the user's input was an integer from 1 to 6.
    This function takes\that value and checks if the score has already been filled. If filled, it will call the
    score_category_check again to determine a valid user input. Otherwise, it will update the category selected.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction_player_two: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update == 1 and scores_diction_player_two['Ones'] == '':
        scores_diction_player_two['Ones'] = 1 * final_hand.count(1)
    elif score_to_update == 2 and scores_diction_player_two['Twos'] == '':
        scores_diction_player_two['Twos'] = 2 * final_hand.count(2)
    elif score_to_update == 3 and scores_diction_player_two['Threes'] == '':
        scores_diction_player_two['Threes'] = 3 * final_hand.count(3)
    elif score_to_update == 4 and scores_diction_player_two['Fours'] == '':
        scores_diction_player_two['Fours'] = 4 * final_hand.count(4)
    elif score_to_update == 5 and scores_diction_player_two['Fives'] == '':
        scores_diction_player_two['Fives'] = 5 * final_hand.count(5)
    elif score_to_update == 6 and scores_diction_player_two['Sixes'] == '':
        scores_diction_player_two['Sixes'] = 6 * final_hand.count(6)
    else:
        print("You can't score that!")
        score_to_update = select_score_category()
        score_category_check_player_two(final_hand, score_to_update, scores_diction_player_two)


def update_score_player_two_threes_and_fours(final_hand: list, score_to_update: int,
                                             scores_diction_player_two: dict) -> None:
    """Determine whether a category can be updated in player two's score dictionary. Updates if possible.

    Called by the score_category_check_player_two function, if the user's input was 7 or 8. This function takes
    that value and checks if the score has already been filled. If filled, it will call the score_category_check
    again to determine a valid user input. Otherwise, it will update the category selected.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction_player_two: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update == 7 and scores_diction_player_two['Three of a kind'] == '':
        if final_hand.count(mode(final_hand)) >= 3:
            scores_diction_player_two['Three of a kind'] = sum(final_hand)
        else:
            scores_diction_player_two['Three of a kind'] = 0
    elif score_to_update == 8 and scores_diction_player_two['Four of a kind'] == '':
        if final_hand.count(mode(final_hand)) >= 4:
            scores_diction_player_two['Four of a kind'] = sum(final_hand)
        else:
            scores_diction_player_two['Four of a kind'] = 0
    else:
        print("You can't score that!")
        score_to_update = select_score_category()
        score_category_check_player_two(final_hand, score_to_update, scores_diction_player_two)


def update_score_player_two_full_house(final_hand: list, score_to_update: int, scores_diction_player_two: dict) -> None:
    """Determine whether a category can be updated in player two's score dictionary. Updates if possible.

    Called by the score_category_check_player_two function, if the user's input was 9. This function takes
    that value and checks if the score has already been filled. If filled, it will call the score_category_check
    again to determine a valid user input. Otherwise, it will update the category selected.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction_player_two: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update == 9 and scores_diction_player_two['Full house'] == '':
        values_div = (str(sorted(final_hand)).strip('[]').replace(', ', ''))
        if (values_div[0:1] == values_div[1:2] == values_div[2:3] and values_div[3:4] == values_div[4:5]) or \
                (values_div[0:1] == values_div[1:2] and values_div[2:3] == values_div[3:4] == values_div[4:5]):
            scores_diction_player_two['Full house'] = 25
        else:
            scores_diction_player_two['Full house'] = 0
    else:
        print("You can't score that!")
        score_to_update = select_score_category()
        score_category_check_player_two(final_hand, score_to_update, scores_diction_player_two)


def update_score_player_two_straights(final_hand: list, score_to_update: int, scores_diction_player_two: dict) -> None:
    """Determine whether a category can be updated in player two's score dictionary. Updates if possible.

    Called by the score_category_check_player_two function, if the user's input was 10 or 11. This function takes
    that value and checks if the score has already been filled. If filled, it will call the score_category_check
    again to determine a valid user input. Otherwise, it will update the category selected.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction_player_two: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update == 10 and scores_diction_player_two['Small straight'] == '':
        values_p2_2 = (str(set(sorted(final_hand))).strip('{}')).replace(', ', '')
        if re.match(r'1234|2345|3456', values_p2_2):
            scores_diction_player_two['Small straight'] = 30
        else:
            scores_diction_player_two['Small straight'] = 0
    elif score_to_update == 11 and scores_diction_player_two['Large straight'] == '':
        values_p2_3 = (str(set(sorted(final_hand))).strip('{}')).replace(', ', '')
        if re.match(r'12345|23456', values_p2_3):
            scores_diction_player_two['Large straight'] = 40
        else:
            scores_diction_player_two['Large straight'] = 0
    else:
        print("You can't score that!")
        score_to_update = select_score_category()
        score_category_check_player_two(final_hand, score_to_update, scores_diction_player_two)


def update_score_player_two_chance_and_yahtzee(final_hand: list, score_to_update: int,
                                               scores_diction_player_two: dict) -> None:
    """Determine whether a category can be updated in player two's score dictionary. Updates if possible.

    Called by the score_category_check_player_two function, if the user's input was 12 or 13. This function takes
    that value and checks if the score has already been filled. If filled, it will call the score_category_check
    again to determine a valid user input. Otherwise, it will update the category selected.

    :param final_hand: a list of final dice the user kept
    :param score_to_update: an integer for the category the user wants to update
    :param scores_diction_player_two: the player's dictionary containing their scores.
    :return: None, updates the dictionary
    """
    if score_to_update == 12 and scores_diction_player_two['Chance'] == '':
        scores_diction_player_two['Chance'] = sum(final_hand)
    elif score_to_update == 13 and scores_diction_player_two['YAHTZEE'] == '':
        if final_hand.count(mode(final_hand)) == 5:
            if scores_diction_player_two['YAHTZEE'] == 50 or scores_diction_player_two['YAHTZEE'] == 150:
                scores_diction_player_two['YAHTZEE'] += 100
            elif scores_diction_player_two['YAHTZEE'] == '':
                scores_diction_player_two['YAHTZEE'] = 50
        else:
            scores_diction_player_two['YAHTZEE'] = 0

    else:
        print("You can't score that!")
        score_to_update = select_score_category()
        score_category_check_player_two(final_hand, score_to_update, scores_diction_player_two)


def quit_game() -> None:
    """Quit the program.

    Called when a player is declared winner or if a player enters 2 when prompted to quit the game.

    :param: None
    :precondition: None
    :postcondition: Calls the main function, restarting the game
    :return: None
    """
    quit()


def player_turns(player_choice: int, scores_diction: dict, scores_diction_player_two: dict) -> None:
    """Use a while loop to alternate between player turns.

    The flow of the game is controlled by this function. Each round, during player two's turn it will check
    whether or not all fields are filled out. If they are then it will calculate bonuses and declare a winner.
    This function is responsible for calling dice rolls, keeping dice, and updating scores. The only ways to exit
    this controller are to press 2 during the get_player_option call or when a winner is declared.

    :param player_choice: an integer representing the player's choice (must be 1)
    :param scores_diction: a dictionary with the scores of player one
    :param scores_diction_player_two: a dictionary with the scores of player two
    :return: None
    """
    count = 0
    while player_choice == 1:
        if count == 0:
            print("Player One rolls using the Vegas Roller technique! Looks like Player One is nothing to mess with!\n")
            final_hand = keep_dice(roll_die())
            scores_to_update = select_score_category()
            score_category_check(final_hand, scores_to_update, scores_diction)
            count += 1
            make_scorecard_pretty(scores_diction, scores_diction_player_two)
            get_player_option()
        if count == 1:
            print("Player Two rolls using the Off-Hand High Drop!!! Such finesse!\n")
            final_hand = keep_dice(roll_die())
            scores_to_update = select_score_category()
            score_category_check_player_two(final_hand, scores_to_update, scores_diction_player_two)
            make_scorecard_pretty(scores_diction, scores_diction_player_two)
            if calculate_bonus(scores_diction, scores_diction_player_two) is True:
                declare_winner(scores_diction, scores_diction_player_two)
            else:
                count -= 1
                get_player_option()


def main():
    """
    Drives the program.
    """
    scores_diction = create_scorecard_player_two()
    scores_diction_player_two = create_scorecard()
    menu()
    player_choice = get_player_option()
    player_turns(player_choice, scores_diction, scores_diction_player_two)


if __name__ == '__main__':
    main()
    doctest.testmod()
