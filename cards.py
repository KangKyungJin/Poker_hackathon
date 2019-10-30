import random
#class card to create card objects
class card:
    def __init__(self,suit, val, numericval):
        self.suit=suit
        self.val= val
        self.numericval=numericval
    def displaycardinfo(self):
        print(self.suit,self.val) 
        return self 

#ace class to apply unique property of Ace's bineg 1 or 11
class ace:
    def __init__(self,suit, val):
        self.suit=suit
        self.val= val
        self.numericval=None
    def acevalue(self,handval):
        if handval>10:
            self.numericval=1
        if handval<10:
            self.numericval=11

#hand class which 
class hand:
    def __init__(self,numofcards):
        self.totalval=0
        self.numofcards=numofcards
    def addcard(self):
        self.numofcards+=1
    def handtotal(self):
        self.totalval+=self.numofcards.numericval
suitdict={ '0': 'hearts', '1':'diamonds', '2':'spades', '3': 'clubs'}
carddict={'0':'2','1':'3','2':'4','3':'5','4':'6','5':'7','6':'8','7':'9', '8':'10', '9':'jack', '10':'queen','11':'king','12':'ace'}

#deck class for building a deck
class Deck:
    def __init__(self,deckAmmount=1):        
        self.deck = []
        for d in range(deckAmmount):
            for x in range(4):
                for y in range(13):
                    self.deck.append(card(x,y+1,y+1))
    def shuffles(self):
        length=len(self.deck)
        for i in range(length): 
            r = random.randint(0,length-1) 
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]
        return self