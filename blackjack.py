import random

def draw_card():
    deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]  # 11 = Ace
    return random.choice(deck)

def calculate_hand(hand):
    total = sum(hand)
    aces = hand.count(11)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

def dealer_play():
    hand = [draw_card(), draw_card()]
    while calculate_hand(hand) < 17:
        hand.append(draw_card())
    return hand
