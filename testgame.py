import pygame, sys, random, math
from pygame.locals import *

###GeneralSetting###
pygame.display.set_caption("BlueMarble")
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.init()
###GeneralSetting###



#######Colors#######
white = (255,255,255)
woodBGColor = (235,178,126)
backGroundColor = (125,178,73)
black = (0,0,0)
darkGray = (89,89,89)
#######Colors#######

#block
class Block :
    def __init__(self) :
        self.name = ''
        self.type = 0
        self.price = 0
        self.pos = [0,0]
        self.tall = 0
        self.owned = 5
        self.visit = 0
        self.olympic = False
        self.building = []
        self.building = []
        self.bdPrice = [0,0,1,1,2,2]
        self.bdTall = [0,0,1,1,2,2]
    def buy(self,turn) :
        self.owned = turn
    def build(self,type) :
        self.building = type
        match type :
            case 1 :
                self.tall+=self.bd1Tall
            case 2 :
                self.tall+=self.bd2Tall
            case 3 :
                self.tall+=self.bd3Tall

####################
#y = 0 - 시작+7
#y = 1 - 무인도+7
#y = 2 - 올림픽+7
#y = 3 - 세계 여행+7
blockNames = ['시작','타이베이','베이징','마닐라','찬스카드','싱가포르','카이로','이스탄불','무인도','아테네','코펜하겐','스톡콜롬','찬스카드','베른','베를린','오타와','올림픽','부에노스아이레스','상파울로','시드니','찬스카드','하와이','리스본','마드리드','세계 여행','도쿄','파리','로마','찬스카드','런던','뉴욕','서울']
######BlockSet######
rows = 8
cols = 4
blocks = [[ Block() for j in range(cols)] for i in range(rows)]
price = 100000
sblocktype = 1
x = 0
y = 0
pixelPos = [1080,1080]
for j in range(4) :
    blocks[x][y].type = sblocktype
    sblocktype+=1
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
        print('Name : {} / Type : {} / Price : {}'.format(blocks[j][i].name,blocks[j][i].type,blocks[j][i].price))
x = 2
y = 0

def distance(pos1,pos2):
    result = math.sqrt( math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))
    return result

normal_font = pygame.font.Font("fonts/HakgyoansimSantteutdotumM.ttf", 70)
mapBoard = pygame.image.load("images/4.GameImages/board/mapimage.png").convert()
mapBoard_pos = (0,0)
selectWorldTour_pos = pygame.image.load("images/4.GameImages/UI/selectworldtour.png").convert()
gamePhaseMenu_pos = (163,163)
phaseMenuPlustButton_Cpos = (321, 765)
phaseMenuMinusButton_Cpos = (753, 765)
firstHalf_buybuilding = pygame.image.load("images/4.GameImages/UI/firsthalfbuybuilding.png").convert()


worldTour_pos = [0,0]

text = blocks[x][y].name
worldTourBlockName_text = normal_font.render(text,True,black)
while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
    screen.fill(white)
    screen.blit(mapBoard,mapBoard_pos)
    screen.blit(firstHalf_buybuilding,gamePhaseMenu_pos)
    pygame.display.update()