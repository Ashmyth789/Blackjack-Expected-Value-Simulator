import random
from blackjack import calculate_hand

def random_strategy(player_hand, dealer_card):
    return random.choice(["hit", "stand"])

def basic_strategy(player_hand, dealer_card):
    total = calculate_hand(player_hand)

    if total <= 11:
        return "hit"
    elif 12 <= total <= 16:
        if dealer_card in [2,3,4,5,6]:
            return "stand"
        else:
            return "hit"
    else:
        return "stand"
