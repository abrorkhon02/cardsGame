__author__ = "7639047, Azimov"

import random

COLORS = ["GREEN", "YELLOW", "BLUE", "RED"]


def create_card_list(number_of_cards: int) -> [(int, str)]:
    """
    Creates a cards list
    :param number_of_cards: int
        Number of cards to be distributed into colors
    :return: list
        Returns list of cards (int, str) based on colors and number of cards
    """
    list_of_cards = [
        (card_number, card_color)
        for card_color in COLORS
        for card_number in range(1, number_of_cards + 1)
    ]
    random.shuffle(list_of_cards)
    return list_of_cards
