class card:
    def __init__(self,suit, val, numericval):
        self.suit=suit
        self.val= val
        self.numericval=numericval
    def displaycardinfo(self):
        print(self.suit,self.val) 

      
        return self 
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
# class hand:

    
    
# for x in range(2,11,1):
#     heartsuit=[]
#     heartsuit.append(x=card("heart",x,x))
hearts3=card('hearts','3',3)
hearts2=card("hearts","2",2)
hearts4=card("hearts","4",4)
hearts5=card("hearts","5",5)
hearts6=card("hearts","6",6)
hearts7=card("hearts","7",7)
hearts8=card("hearts","8",8)
hearts9=card("hearts","9",9)
hearts10=card("hearts","10",10)
hearts_jack=card("hearts","jack",10)
hearts_queen=card("hearts","queen",10)
hearts_king=card("hearts","king",10)
spades3=card('spades','3',3)
spades2=card("spades","2",2)
spades4=card("spades","4",4)
spades5=card("spades","5",5)
spades6=card("spades","6",6)
spades7=card("spades","7",7)
spades8=card("spades","8",8)
spades9=card("spades","9",9)
spades10=card("spades","10",10)
spades_jack=card("spades","jack",10)
spades_queen=card("spades","queen",10)
spades_king=card("spades","king",10)
clubs2=card("clubs","2",2)
clubs3=card('clubs','3',3)
clubs4=card("clubs","4",4)
clubs5=card("clubs","5",5)
clubs6=card("clubs","6",6)
clubs7=card("clubs","7",7)
clubs8=card("clubs","8",8)
clubss9=card("clubs","9",9)
clubs10=card("clubs","10",10)
clubs_jack=card("clubs","jack",10)
clubs_queen=card("clubs","queen",10)
clubs_king=card("clubs","king",10)
diamonds2=card("diamonds","2",2)
diamonds3=card('diamonds','3',3)
diamonds4=card("diamonds","4",4)
diamonds5=card("diamonds","5",5)
diamonds6=card("diamonds","6",6)
diamonds7=card("diamonds","7",7)
diamonds8=card("diamonds","8",8)
diamonds9=card("diamonds","9",9)
diamonds10=card("diamonds","10",10)
diamonds_jack=card("diamonds","jack",10)
diamonds_queen=card("diamonds","queen",10)
diamonds_king=card("diamonds","king",10)


print(hearts4.displaycardinfo())