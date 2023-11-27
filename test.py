import pygame, sys, random, math
from pygame.locals import *

class Player :
    def __init__(self) :
        self.fortune = 500000
        self.ownedLands = []
        self.items = []
        self.pos = [0,0]
    def move(self,num) :
        if self.pos[0] + num <= 8 :
            self.pos[0] += num
        else :
            num -= 8 - self.pos[0]
            self.pos[0] = num
            if self.pos[1] + 1 <= 3 :
                self.pos[1] += 1
            else :
                self.pos[1] = 0

#block
class Block :
    def __init__(self) :
        self.name = ''
        self.type = 0
        self.price = 0
        self.pos = [0,0]
        self.tall = 0
        self.owned = 0
        self.building = 0
####################
#y = 0 - 시작+7
#y = 1 - 무인도+7
#y = 2 - 올림픽+7
#y = 3 - 세계 여행+7
blockNames = ['시작','타이베이','베이징','마닐라','찬스카드','싱가포르','카이로','이스탄불','무인도','아테네','코펜하겐','스톡콜롬','찬스카드','베른','베를린','오타와','올림픽','부에노스아이레스','상파울로','시드니','찬스카드','하와이','리스본','마드리드','세계 여행','도쿄','파리','로마','찬스카드','런던','뉴욕','서울']
######BlockSet######
players = []
def setPlayers(arr,num) :
    for i in range(num) :
        arr.append(Player())
asdf = 0
rows = 8
cols = 4
blocks = [[ Block() for j in range(cols)] for i in range(rows)]
price = 100000
blocktype = 1
x = 0
y = 0
turn = 1
for j in range(4) :
    blocks[x][y].type = blocktype
    blocktype+=1
    x+=1
    for i in range(3) :
        blocks[x][y].price = price
        price+=10000
        x+=1
    blocks[x][y].type = 5
    x+=1
    for i in range(3) :
        blocks[x][y].price = price
        price+=10000
        x+=1
    x = 0
    y += 1
k = 0
for i in range(cols) :
    for j in range(rows) :
        blocks[j][i].name = blockNames[k]
        k+=1
for i in range(cols) :
    for j in range(rows) :
        print('[{}][{}].Name : {} / Type : {} / Price : {}'.format(j,i,blocks[j][i].name,blocks[j][i].type,blocks[j][i].price))
        asdf+=1
setPlayers(players,4)
a = random.randint(0,7)
b = random.randint(0,3)
print('x : {} / y : {}'.format(a,b))
players[turn].pos = [a,b]
x = players[turn].pos[0]
y = players[turn].pos[1]
current_block_type = blocks[x][y].type
if current_block_type == 0:
    print('normal',players[turn].pos)
elif current_block_type == 1:
    print('start',players[turn].pos)
elif current_block_type == 2:
    print('muindo',players[turn].pos)
elif current_block_type == 3:
    print('olympic',players[turn].pos)
elif current_block_type == 4:
    print('worldtour',players[turn].pos)
elif current_block_type == 5:
    print('chancecard',players[turn].pos)