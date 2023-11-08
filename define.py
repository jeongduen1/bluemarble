import random

class Player :
    def __init__(self) :
        self.fortune = 500000
        self.ownedBlocks = []
        self.items = []
        self.uninhabitedIsland = 0
class Block :
    def __init__(self) :
        self.price = 0
        self.buildings = []
        self.belong = 0
        self.tall = 0
        self.type = 0
    def set_price(self,price) :
        self.price = price
    def set_type(self,type) :
        self.type = type
    def notice(self,a) :
        a = 0

maps = []
def MapSet(map) :
    price = 100000
    i = 0
    num = 1
    for k in range(4) :
        map.append(Block())
        map[i].set_type(num)
        i += 1
        num += 1
        for j in range(3) :
            map.append(Block())
            map[j+i].set_price(price)
            map[j+i].set_type(0)
        i += 3
        map.append(Block())
        map[i].set_type(5)
        i += 1
        for j in range(3) :
            map.append(Block())
            map[j+i].set_price(price)
            map[j+i].set_type(0)
        i += 3
    
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