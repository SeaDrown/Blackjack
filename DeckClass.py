# For grouping functionality regarding decks. Fairly simple.
import random

class Deck():
    seperator = "/"
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    specialRankValues = {
        "Queen": 10,
        "King": 10,
        "Jack": 10,
        "Ace": 11 # we will handle the other scenario in the HandClass
    }

    def __init__(self):
        self.Organise()

    def Organise(self):
        self.Deck = []

        for currentSuit in Deck.suits:
            for rank in Deck.ranks:
                card = f"{rank}{Deck.seperator}{currentSuit}"
                self.Deck.append(card)
    
    def Shuffle(self): # Shuffle the deck
        newDeck = self.Deck[:]
        random.shuffle(newDeck)

        self.Deck = newDeck

    def PickCard(self):
        return self.Deck.pop()
        