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
#def CardEvent(num) :
#    match num :
#        case 1 :
#
#        case 2 :
#
#        case 3 :
#
#        case 4 :
#
#        case 5 :
#
#        case 6 :
#
#        case 7 :
#
#        case 8 :
#
#        case 9 :
#
#        case 10 :
#
#        case 11 :
#
#        case 12 :
#
#        case 13 :
#
#        case 14 :
#
#        case 15 :
#
#        case 16 :
#
#        case 17 :
#
#        case 18 :
#
#        case 19 :
#
#        case 20 :
#
#        case 21 :
#
#        case 22 :
#
#        case 23 :
#
#        case 24 :
#
#        case 25 :
#