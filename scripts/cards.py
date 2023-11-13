import random

cards = [1,2,3,4,4,5,5,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
def CardShuffle(cards) :
    for i in range(30) :
        a = random.randint(0,19)
        b = random.randint(0,19)
        c = cards[a]
        cards[a] = cards[b]
        cards[b] = c
def CardSwap(cards) :
    a = cards[0]
    cards[0] = cards[len(cards)]
    cards[len(cards)] = a