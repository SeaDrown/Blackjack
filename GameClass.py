# Defines the behaviour of how the game will work. Since blackjack has some niche rules, a class will be used
# to abstract it's implementation

# Cards will be formatted like this: (rank)(seperator)(suit)

import DeckClass
import HandClass
import os

def ClearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Game():
    def __init__(self):
        self.Deck = DeckClass.Deck() # is sorted at instantiation
        self.Playing = False

    def HitOrStand(self):
        print(self.PlayerHand)
        print(self.DealerHand)

        print()

        print("Would you like to hit, or stand? \n 1: Hit\n 2: Stand")

        hitInputs = ["1", "hit"]
        standInputs = ["2", "stand"]

        choice = None

        while choice == None:
            currentInput = input("> ").lower().rstrip()
            print()

            if currentInput in hitInputs:
                choice = "hit"
                self.PlayerHand.GiveCard(self.Deck.PickCard())

            elif currentInput in standInputs:
                choice = "stand"
                self.Playing = False

            else:
                print("Please make a valid choice.")
        
        return choice

    def Start(self):
        ClearTerminal()

        self.DealerHand = HandClass.Hand("Dealer")
        self.PlayerHand = HandClass.Hand("Player") # the hands are created

        self.Deck.Shuffle()

        print("Blackjack begins.")
        print()

        for i in range(2): # 2 cards each given to the player and the computer
            self.PlayerHand.GiveCard(self.Deck.PickCard())
            self.DealerHand.GiveCard(self.Deck.PickCard())

        if self.PlayerHand.GetTotal() == 21:
            self.DeclareWinner()

        choice = "hit"

        while choice == "hit" and self.PlayerHand.GetTotal() < 21:
            choice = self.HitOrStand()
        
        if self.PlayerHand.GetTotal() >= 21:
            self.DeclareWinner()
        else:
            while self.DealerHand.GetTotal() < 17:
                self.DealerHand.GiveCard(self.Deck.PickCard())

            self.DeclareWinner() 
    
    def DeclareWinner(self):
        message = ""

        plrTotal = self.PlayerHand.GetTotal()
        dealerTotal = self.DealerHand.GetTotal()

        print(self.PlayerHand.ShowAllCards())
        print(self.DealerHand.ShowAllCards())

        print()

        if plrTotal > 21: # player goes bust
            message = "You went bust! Dealer wins"
        elif dealerTotal > 21: # dealer goes bust
            message = "Dealer went bust! You win"
        elif plrTotal == dealerTotal: # they have the same amount of points
            message = f"You both have {plrTotal} points! Dealer wins, how unlucky..."
        else:
            message = f"You have {plrTotal} points, Dealer has {dealerTotal} points. "

            if dealerTotal > plrTotal:
                message += "Dealer wins!"
            else:
                message += "Player wins!"
        
        print(message)

        self.Playing = False


            
        
