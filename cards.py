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
suitdict={ '0': '♥', '1':'♦', '2':'♠', '3': '♣'}
carddict={'1':'2','2':'3','3':'4','4':'5','5':'6','6':'7','7':'8','8':'9', '9':'10', '10':'jack', '11':'queen','12':'king','13':'ace'}

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
    
    def draw(self):
        card = self.deck.pop()
        return card

deckOne = Deck(4)                   
# for d in range(0,208,1):
#             for x in range(4):
#                 deckOne.suit=suitdict[x]
#                 for y in range(13):
#                     deckOne.val=carddict[y]

for x in range(0,len(deckOne.deck)):
    deckOne.deck[x].suit=suitdict[str(deckOne.deck[x].suit)]
    deckOne.deck[x].val=carddict[str(deckOne.deck[x].val)]

deckOne.shuffles().draw().displaycardinfo()

deckOne.draw().displaycardinfo()
