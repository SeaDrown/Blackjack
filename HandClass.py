# Contains the functionality for hands: player and computer alike
from DeckClass import Deck

class Hand():
    def __init__(self, name):
        self.Hand : list[str] = []
        self.Name = name

    def __str__(self):
        hand = self.Hand

        if self.Name == "Dealer":
            hand = [self.Hand[i] if i == 0 else "???/???" for i in range(len(self.Hand))]
        
        string = f"{self.Name}'s hand: "
        seperator = " | "

        string += seperator.join(hand)

        return string
    
    def ShowAllCards(self):
        hand = self.Hand
        
        string = f"{self.Name}'s hand: "
        seperator = " | "

        string += seperator.join(hand)

        return string
    
    def GetTotal(self):
        total = 0
        aceCount = 0

        for card in self.Hand:
            rank = card.split(Deck.seperator)[0] # gets the rank of the current card in the loop
            
            if rank.isnumeric() == True: # the rank is a regular number
                total += int(rank)
            else:
                total += Deck.specialRankValues[rank]

                if rank == "Ace":
                    aceCount += 1

        while total > 21 and aceCount > 0: # ensure that the aces do not make the player bust
            aceCount -= 1
            total -= 10
        
        return total
    
    def GiveCard(self, card):
        self.Hand.append(card)




