from cards import Deck, card
deck = Deck(4) 
deck = deck.shuffles()
class player:
    def __init__ (self):
        self.hand=[deck.draw(),deck.draw()]

    
    def playerHit(self):
        self.hand.append(deck.draw())
erik=player()        
print(erik.hand[0].displaycardinfo())

