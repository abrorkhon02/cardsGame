__author__ = "7639047, Azimov"

from collections import defaultdict

from card_create import create_card_list
from card_distribute import deal_cards
from card_compare import bigger_card

NUMBER_OF_CARDS = 13


def get_cards_in_the_deck(current_player_deck: list):
    return [f"{player_index + 1}) {value} {color}"
            for player_index, (value, color) in enumerate(current_player_deck)]


def calculate_winner(current_total_deck: list, current_ace_card: str) -> [int]:
    cards = defaultdict(int)
    for first_card_index in range(len(current_total_deck)):
        for second_card_index in range(len(current_total_deck)):
            result = bigger_card(
                card_one=current_total_deck[first_card_index],
                card_two=current_total_deck[second_card_index],
                ace_card=current_ace_card,
            )
            if result == 2:
                cards[first_card_index] += result
            elif result == 1:
                cards[first_card_index] += result
                cards[second_card_index] += result
            else:
                cards[first_card_index] += result
    return [k for k, v in cards.items() if v == max(cards.values())]


game = input("\t\t\tHello! Do you want to play the game? (y - yes, n - no)\t\t\t")
while game == "y":
    players = int(input("### Please input the number of players: "))

    if not 2 <= players <= 4:
        raise ValueError("!!! Wrong number of players!")

    list_cards = create_card_list(number_of_cards=NUMBER_OF_CARDS)
    rounds = round((len(list_cards) - 1) / players)

    print(f"*** Every player will receive {rounds} cards ***")

    decks_of_players = deal_cards(
        list_cards=list_cards,
        players=players,
        number_of_cards=rounds,
    )
    ace_card = list_cards[-1]
    print(f"*** Ace Card is {ace_card[0]} {ace_card[1]} ***")
    print("*** Starting the game... ***")
    overall_winners = defaultdict(int)
    for i in range(rounds):
        total_deck = []
        print(f"*** ROUND {i + 1} ***")
        for index, player_deck in enumerate(decks_of_players):
            print(f"*** PLAYER #{index + 1}. YOUR TURN! ***")
            print("*** YOUR DECK: ***")
            print("\n".join(get_cards_in_the_deck(player_deck)))
            card_index = int(input(
                "### Please input the index of the card that you want to put on the deck: "
            ))
            total_deck.append(player_deck[card_index - 1])
            player_deck.pop(card_index - 1)
            print("*** DECK OF THE ROUND ***")
            print("\n".join(get_cards_in_the_deck(total_deck)))
        winners = calculate_winner(total_deck, ace_card[1])
        for winner in winners:
            overall_winners[winner] += 1
        if len(winners) > 1:
            print(f"*** ROUND {i + 1} TIE BETWEEN PLAYERS {','.join([str(winner + 1) for winner in winners])} ***")
        else:
            print(f"*** ROUND {i + 1} WON BY PLAYER {winners[0] + 1} ***")

    print("*** OVERALL POINTS FOR EACH PLAYER: ***")
    print("\n".join([f"{key + 1}. {overall_winners[key]}" for key in overall_winners]))

    game = input("\t\t\tDo you want to play again? (y - yes, n - no)\t\t\t")
