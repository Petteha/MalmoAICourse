import random

deck = []

def createDeck():
    tempdeck = []

    for suit in "scdh":
        for a in range(10):
            if a == 0:
                tempdeck.append("A"+suit)
            else:
                tempdeck.append(str((a+1))+suit)

        for face in "JQK":
            tempdeck.append(face+suit)
    print(tempdeck)
    return tempdeck        

            
def shuffleDeck(tempdeck):
    for x in range(0, 52):
            y = random.randrange(52)
            
            while (x == y):
                 y = random.randrange(52)

            temp = tempdeck[x]
            tempdeck[x] = tempdeck[y]
            tempdeck[y] = temp

    return deck