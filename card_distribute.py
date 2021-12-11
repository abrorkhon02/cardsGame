__author__ = "7639047, Azimov"


def deal_cards(
    list_cards: [(int, str)], players: int, number_of_cards: int
) -> [[(int, str)]]:
    """
    Appends list of cards of every player to one array
    :param list_cards: (int, str)
        List of cards (int, str)
    :param players: int
        Number of players
    :param number_of_cards: int
        Number of cards played in each round
    :return: list
        Deck of each player in one list
    """
    decks = []
    for i in range(players):
        decks.append(list_cards[i * number_of_cards: (i + 1) * number_of_cards])
    return decks
