#flip 3 in a row
import random

def flip():
    flag = False
    count = 0
    flips = ""
    
    while (flag == False):
        if(random.randrange(2) == 0): #tails
            flips = flips + "T "
            count = count + 1

        else: #heads
            flips = flips + "H "
            count = count + 1

        if "T T T" in flips or "H H H" in flips:
            flag = True

    print("{0}({1} flips)".format(flips, count))
