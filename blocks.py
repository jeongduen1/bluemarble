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