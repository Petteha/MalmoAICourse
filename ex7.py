#create, shuffle and deal cards
import random

class cards():
    cards=[]
    hands = {}

    def create (self):
        self.cards=[]

        for suit in "scdh":
            for a in range(10):
                if a == 0:
                    self.cards.append("A"+suit)
                else:
                    self.cards.append(str((a+1))+suit)

            for face in "JQK":
                self.cards.append(face+suit   )
        print(self.cards)

        #Your program goes here
        #Construct the deck here


    def shuffle (self):
        for x in range(0, 52):
            y = random.randrange(52)
            
            while (x == y):
                 y = random.randrange(52)

            temp = self.cards[x]
            self.cards[x] = self.cards[y]
            self.cards[y] = temp

        print(self.cards)
        #Your program goes here
        #use constructed card deck by using "self.cards" and shuffle them

    def deal (self,hands_num,card_num):
        for h in range(hands_num):
            key = "Hand " + str(h+1)
            self.hands[key] = []

        for c in range(card_num):
            for h in range(hands_num):
                key = "Hand " + str(h+1)
                self.hands[key].append(self.cards.pop(len(self.cards)-1))


        print(self.hands)
                    
                    

        #Your program goes here
        #use constructed card deck by using "self.cards" and deal based on the number of hands, "hands", and number of cards in each hand, "num-cards", that are recevied from the user


#initialte your programs with this functions
#card_01 = cards
#card_01.create()
#card_01.shuffle()
#card_01.deal(X,Y) #Change X and Y