# Made by Marvin Omoruyi, distributed with the MIT Licence

# A simple game of blackjack, against the dealer.
# In this version, the dealer will hit until their cards' value totals 17 or more

import GameClass

def main():
    game = GameClass.Game()

    # How Blackjack works:

    # Player recieves card, Dealer recieves card, both face up (public information)
    # Player recieves a second card, Dealer recieves a second card, but the dealer's card is private (face down)
    # Player chooses to hit or stand
    # Player keeps hitting or standing until either they go bust or they stand
    # Dealer hits until their cards value totals 17 or more.
    # If dealer goes bust, Player wins
    # If player goes bust, Dealer wins
    # If player has a higher card than dealer, player wins
    # Else dealer wins

    game.Start()

main()