from blackjack import draw_card, calculate_hand, dealer_play

def play_hand(strategy):
    player = [draw_card(), draw_card()]
    dealer = [draw_card(), draw_card()]
    dealer_upcard = dealer[0]

    # Player turn
    while True:
        action = strategy(player, dealer_upcard)

        if action == "hit":
            player.append(draw_card())
            if calculate_hand(player) > 21:
                return -1
        else:
            break

    # Dealer turn
    dealer_final = dealer_play()

    player_total = calculate_hand(player)
    dealer_total = calculate_hand(dealer_final)

    if dealer_total > 21 or player_total > dealer_total:
        return 1
    elif player_total < dealer_total:
        return -1
    else:
        return 0
