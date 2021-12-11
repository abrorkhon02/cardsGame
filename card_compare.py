__author__ = "7639047, Azimov"


def compare_values(card_one_value: int, card_two_value: int) -> int:
    """
    Compares two integer values
    :param card_one_value: int
        Value of the first card
    :param card_two_value: int
        Value of the second card
    :return: int
    """
    if card_one_value > card_two_value:
        return 2
    elif card_one_value == card_two_value:
        return 1
    else:
        return 0


def bigger_card(card_one: (int, str), card_two: (int, str), ace_card: str) -> int:
    """
    Compares two cards based on values and if it is ace card or not
    :param card_one: (int, str)
        Value of the card number one and its color
    :param card_two: (int, str)
        Value of the card number two and its color
    :param ace_card: str
        Ace Card
    :return:
        0 if Card One is smaller,
        1 if Card One is equal to Card two,
        2 if Card One is bigger
    """
    if ace_card in [card_one[1], card_two[1]]:
        if card_one[1] == card_two[1]:
            return compare_values(card_one[0], card_two[0])
        elif card_one[1] == ace_card:
            return 2
        else:
            return -2
    else:
        return compare_values(card_one[0], card_two[0])
