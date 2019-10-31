from cards import *
deck = Deck(4) 
deck = deck.shuffles()
for x in range(0,len(deck.deck)):
    deck.deck[x].suit=suitdict[str(deck.deck[x].suit)]
    deck.deck[x].val=carddict[str(deck.deck[x].val)]
class player:
    def __init__ (self):
        self.hand=[deck.draw(),deck.draw()]
    def playerHit(self):
        self.hand.append(deck.draw())
        return self
    def printHand(self):
        for x in range(len(self.hand)):
            print(self.hand[x].displaycardinfo())
    def handVal(self):
        val = 0
        for x in range(len(self.hand)):
            val = val + self.hand[x].returnVal()
        return val    
            

class dealer:
    def __init__(self):
        self.hand=[deck.draw(),deck.draw()]
    def playerHit(self):
        self.hand.append(deck.draw())
        return self
    def printHand(self):
        for x in range(len(self.hand)):
            print(self.hand[x].displaycardinfo())
    def handVal(self):
        val= 0
        for x in range(len(self.hand)):
            val = val + self.hand[x].returnVal()
        return val          
erik=player()
erik.handVal()       