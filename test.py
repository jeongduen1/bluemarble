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

#######Images#######

######GameMenu######
##images##
#gameMenu
gameMenu = pygame.image.load("images/1.GameMenuImages/GameMenu.png").convert()
#positions#
gameMenu_pos = (0,0)
#startButton pos
menuStartButton_pos1 = (882, 469)
menuStartButton_pos2 = (1358, 581)
#gameRuelButton pos
gameRuleButton_pos1 = (882, 612)
gameRuleButton_pos2 = (1358, 725)
#gameExitButton pos
menuExitButton_pos1 = (882,746)
menuExitButton_pos2 = (1358,871)
######GameRule######
#images
ruleNotePage1 = pygame.image.load("images/2.GameRuleImages/RuleNotePage1.png").convert()
ruleNotePage2 = pygame.image.load("images/2.GameRuleImages/RuleNotePage2.png").convert()
ruleNotePage3 = pygame.image.load("images/2.GameRuleImages/RuleNotePage3.png").convert()
#postions
nextPageButton_Cpos1 = (1507-160,950-90)
nextPageButton_Cpos2 = (1830-160, 980-90)
backPageButton_Cpos = (413-160, 980-90)
backtoMenuButton_Cpos = (1640, 202)
#####GameNumber#####
#images
selectGameNumber2 = pygame.image.load("images/3.SelectGameNumberImages/SelectGameNumber2.png").convert()
selectGameNumber3 = pygame.image.load("images/3.SelectGameNumberImages/SelectGameNumber3.png").convert()
selectGameNumber4 = pygame.image.load("images/3.SelectGameNumberImages/SelectGameNumber4.png").convert()
#positions
gameNumberMinusButton_pos1 = (34, 527)
gameNumberMinusButton_pos2 = (91, 584)
gameNumberPlusButton_pos1 = (588, 526)
gameNumberPlusButton_pos2 = (644, 582)
gameNumberCheckButton_Cpos = (622, 303)
gameNumberInGameMenuButton_Cpos = (60,120)
########Game########
#images
#Map
mapBoard = pygame.image.load("images/4.GameImages/board/mapimage.png").convert()
#GameUI
gameUI2 = pygame.image.load("images/4.GameImages/UI/FortuneUI2.png").convert()
gameUI3 = pygame.image.load("images/4.GameImages/UI/FortuneUI3.png").convert()
gameUI4 = pygame.image.load("images/4.GameImages/UI/FortuneUI4.png").convert()
#TurnMarker
myTurnMarker = pygame.image.load("images/4.GameImages/markers/MTM.png").convert()
myTurnMarker.set_colorkey((0,95,65))
#Dice Button
diceButton = pygame.image.load("images/4.GameImages/buttons/DiceButton.png").convert()
diceButton = pygame.transform.scale(diceButton,(200,200))
#Dice
dice1 = pygame.image.load("images/4.GameImages/dices/d1.png").convert()
dice1 = pygame.transform.scale(dice1,(150,150))
dice1.set_colorkey(darkGray)
#one
dice2 = pygame.image.load("images/4.GameImages/dices/d2.png").convert()
dice2 = pygame.transform.scale(dice2,(150,150))
dice2.set_colorkey(darkGray)
#two
dice3 = pygame.image.load("images/4.GameImages/dices/d3.png").convert()
dice3 = pygame.transform.scale(dice3,(150,150))
dice3.set_colorkey(darkGray)
#four
dice4 = pygame.image.load("images/4.GameImages/dices/d4.png").convert()
dice4 = pygame.transform.scale(dice4,(150,150))
dice4.set_colorkey(darkGray)
#five
dice5 = pygame.image.load("images/4.GameImages/dices/d5.png").convert()
dice5 = pygame.transform.scale(dice5,(150,150))
dice5.set_colorkey(darkGray)
#six
dice6 = pygame.image.load("images/4.GameImages/dices/d6.png").convert()
dice6 = pygame.transform.scale(dice6,(150,150))
dice6.set_colorkey(darkGray)
#PhaseMenu
buyMenu = pygame.image.load("images/4.GameImages/UI/BuyPhase.png").convert()
buybuilding = pygame.image.load("images/4.GameImages/UI/buybuilding.png").convert()
salebuilding = pygame.image.load("images/4.GameImages/UI/salebuiding.png").convert()
startMenu = pygame.image.load("images/4.GameImages/UI/startblockPhase.png").convert()
uninhabitedIslandMenu = pygame.image.load("images/4.GameImages/UI/muindoblockmenu.png").convert()
olympicMenu = pygame.image.load("images/4.GameImages/UI/olympicblockphase.png").convert()
selectOlympicTour_pos = pygame.image.load("images/4.GameImages/UI/selectolympic.png").convert()
worldTourMenu = pygame.image.load("images/4.GameImages/UI/worldtourblockmenu.png").convert()
selectWorldTour_pos = pygame.image.load("images/4.GameImages/UI/selectworldtour.png").convert()
chanceCardMenu = pygame.image.load("images/4.GameImages/UI/chancecardblockmenu.png").convert()
double = pygame.image.load("images/4.GameImages/UI/double.png").convert()
#cards Images
card1I = pygame.image.load("images/4.GameImages/cards/card1.png")
card2I = pygame.image.load("images/4.GameImages/cards/card2.png")
card3I = pygame.image.load("images/4.GameImages/cards/card3.png")
card4I = pygame.image.load("images/4.GameImages/cards/card4.png")
card4YorNI = pygame.image.load("images/4.GameImages/cards/card4YorN.png")
card5I = pygame.image.load("images/4.GameImages/cards/card5.png")
card5YorNI = pygame.image.load("images/4.GameImages/cards/card5YorN.png")
card6I = pygame.image.load("images/4.GameImages/cards/card6.png")
card7I = pygame.image.load("images/4.GameImages/cards/card7.png")
card8I = pygame.image.load("images/4.GameImages/cards/card8.png")
card9I = pygame.image.load("images/4.GameImages/cards/card9.png")
card10I = pygame.image.load("images/4.GameImages/cards/card10.png")
card11I = pygame.image.load("images/4.GameImages/cards/card11.png")
card12I = pygame.image.load("images/4.GameImages/cards/card12.png")
card13I = pygame.image.load("images/4.GameImages/cards/card13.png")
card14I = pygame.image.load("images/4.GameImages/cards/card14.png")
card15I = pygame.image.load("images/4.GameImages/cards/card15.png")
card16I = pygame.image.load("images/4.GameImages/cards/card16.png")
card17I = pygame.image.load("images/4.GameImages/cards/card17.png")
card18I = pygame.image.load("images/4.GameImages/cards/card18.png")
card19I = pygame.image.load("images/4.GameImages/cards/card19.png")
card20I = pygame.image.load("images/4.GameImages/cards/card20.png")
#positons
gameInGameMenuButton_Cpos = (1880, 40)
#Map
mapBoard_pos = (0,0)
#TurnMaker
myTurnMarker_Redpos = (1130,10)
myTurnMarker_Bluepos = (1130,295)
myTurnMarker_Greenpos = (1510,10)
myTurnMarker_Yellowpos = (1515,295)
#Dice Button
diceButton_pos = (1400,750)
diceButton_Cpos = (1500,850)
#Dice
dice_pos1 = (1350,750)
dice_pos2 = (1500,750)
#PhaseMenu
villaButton_Cpos = (339, 597)
buildingButton_Cpos = (536, 597)
hotelButton_Cpos = (737, 597)

gamePhaseMenu_pos = (163,163)
phaseMenuYesButton_Cpos = (388,763)
phaseMenuNoButton_Cpos = (688,763)
phaseMenuPlustButton_Cpos = (321, 725)
phaseMenuMinusButton_Cpos = (753, 725)
phaseMenuNextButton_pos1 = (366,750)
phaseMenuNextButton_pos2 = (879,840)
#Ending
endingPhase = pygame.image.load("images/5.Ending/EndPhase.png").convert()
##InGameMenuImages##
#images
inGameMenu = pygame.image.load("images/6.InGameMenuImages/InGameMenu.png").convert()
#positions
inGameMenuContinueButton_pos1 = (642,354)
inGameMenuContinueButton_pos2 = (1279,520)
inGameMenuBackToMenuButton_pos1 = (642,540)
inGameMenuBackToMenuButton_pos2 = (1279,707)
inGameMenuExitButton_pos1 = (642,737)
inGameMenuExitButton_pos2 = (1279,888)
#######Images#######


########Font########
normal_font = pygame.font.Font("fonts/HakgyoansimSantteutdotumM.ttf", 50)
########Font########


#######Classes######
#player
class Player :
    def __init__(self) :
        self.fortune = 2000000
        self.items = []
        self.pos = [0,0]
        self.lap = 0
        self.inUnIsTurn = 0
    def move(self,num) :
        self.pos[0]+=num
        while self.pos[0] > 7 :
            self.pos[1]+= 1
            self.pos[0]-= 8
            while self.pos[1] > 3 :
                self.pos[1]-=4
    def tp(self,pos) :
        self.pos = pos
    def getMoney(self,num) :
        self.fortune+=num
    def pay(self,tall) :
        self.fortun -= tall
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
        self.bdPrice = [0,1,2]
        self.bdTall = [0,1,2]
    def buy(self,turn) :
        self.owned = turn
    def buff(self) :
        self.olympic = True
    def build(self,type) :
        self.building.append(type)
        match type :
            case 0 :
                self.tall+=self.bdTall[0]
            case 1 :
                self.tall+=self.bd2Tall[1]
            case 2 :
                self.tall+=self.bd3Tall[2]

####################
#y = 0 - 시작+7
#y = 1 - 무인도+7
#y = 2 - 올림픽+7
#y = 3 - 세계 여행+7
blockNames = ['시작','타이베이','베이징','마닐라','찬스카드','싱가포르','카이로','이스탄불','무인도','아테네','코펜하겐','스톡콜롬','찬스카드','베른','베를린','오타와','올림픽','부에노스아이레스','상파울로','시드니','찬스카드','하와이','리스본','마드리드','세계여행','도쿄','파리','로마','찬스카드','런던','뉴욕','서울']
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
#######Classes######

#######Defines######
def distance(pos1,pos2):
    result = math.sqrt( math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))
    return result
def clickButton(BtnPos1,BtnPos2,ClickPos) :
    if BtnPos1[0] <= ClickPos[0] <= BtnPos2[0] and BtnPos1[1] <= ClickPos[1] <= BtnPos2[1] :
        return True
    else :
        return False
def isDouble(array) :
    if array[0] == array[1] :
        return True
    else :
        return False
def passStart(pos1,pos2) :
    if pos1[1] != 0 and pos2[1] == 0 :
        return True
    else :
        return False
def setPlayers(arr,num) :
    for i in range(num) :
        arr.append(Player())
def cardsSwap(arr,num1,num2) :
    temp = arr[num1]
    arr[num1] = arr[num2]
    arr[num2] = temp
def drawDice(arr):
    match arr[0] :
        case 1 :
            screen.blit(dice1,dice_pos1)
        case 2 :
            screen.blit(dice2,dice_pos1)
        case 3 :
            screen.blit(dice3,dice_pos1)
        case 4 :
            screen.blit(dice4,dice_pos1)
        case 5 :
            screen.blit(dice5,dice_pos1)
        case 6 :
            screen.blit(dice6,dice_pos1)
    match arr[1] :
        case 1 :
            screen.blit(dice1,dice_pos2)
        case 2 :
            screen.blit(dice2,dice_pos2)
        case 3 :
            screen.blit(dice3,dice_pos2)
        case 4 :
            screen.blit(dice4,dice_pos2)
        case 5 :
            screen.blit(dice5,dice_pos2)
        case 6 :
            screen.blit(dice6,dice_pos2)
def drawGameUI(num) :
    match num :
        case 2 :
            screen.blit(gameUI2,(1080,0))
        case 3 :
            screen.blit(gameUI3,(1080,0))
        case 4 :
            screen.blit(gameUI4,(1080,0))
def drawTurnMarker(num) :
    match num :
        case 0 :
            screen.blit(myTurnMarker,myTurnMarker_Redpos)
        case 1 :
            screen.blit(myTurnMarker,myTurnMarker_Bluepos)
        case 2 :
            screen.blit(myTurnMarker,myTurnMarker_Greenpos)
        case 3 :
            screen.blit(myTurnMarker,myTurnMarker_Yellowpos)
#Menu
#GameRule
#GameNumber
#Game
#Ending
#InGameMenu
#######Defines######
worldTour_phase = 1
worldTour_pos = [0,0]
########Logic#######
while isEndRunning :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        match worldTour_phase :
            case 1 :
                if distance(phaseMenuPlustButton_Cpos,click_pos) <= 60 :
                    worldTour_pos[0]+=1
                    while worldTour_pos[0] > 7 :
                        worldTour_pos[1]+=1
                        worldTour_pos[0]-=8
                        while worldTour_pos[1] > 3 :
                            worldTour_pos[1]-=4
                if distance(phaseMenuMinusButton_Cpos,click_pos) <= 60 :
                    worldTour_pos[0]-=1
                    while worldTour_pos[0] < 0 :
                        worldTour_pos[1]-=1
                        worldTour_pos[0]=7
                        while worldTour_pos[1] < 0 :
                            worldTour_pos[1]=3
                if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                    worldTour_phase = 2
            case 2 :
                players[turn].tp(worldTour_pos)
                phase = 9