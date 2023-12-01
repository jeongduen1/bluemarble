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

########Logic#######
isGameLogicRunning = True
#1 - Menu / 2 - GameRule / 3 - SelectGameNumber / 4 - Game / 5 - Ending / 6 - InGameMenu
event_type = 1
mevent_type = 1
list = []
fromInGameMenu = False
while isGameLogicRunning :
    isMenuRunning = True
    isGameRuelRunning = True
    isGameNumberRunning = True
    isGameRunning = True
    isEndRunning = True
    isInGameMenuRunning = True
    match event_type :
        #Menu
        case 1 :
            while isMenuRunning :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click_pos = pygame.mouse.get_pos()
                        print(click_pos)
                        #StartButton
                        if clickButton(menuStartButton_pos1,menuStartButton_pos2,click_pos):
                            isMenuRunning = False
                            fromInGameMenu = True
                            event_type = 3 #->GameNumber
                            print('Menu to SelectGameNumber')
                        #RuleButton
                        if clickButton(gameRuleButton_pos1,gameRuleButton_pos2,click_pos):
                            isMenuRunning = False
                            event_type = 2 #->GameRule
                            print('Menu to GameRule')
                        #GameExitButton
                        if clickButton(menuExitButton_pos1,menuExitButton_pos2,click_pos):
                            sys.exit() #-> GameExit
                screen.blit(gameMenu,gameMenu_pos)
                pygame.display.update()
        #GameRule
        case 2 :
            page = 1
            while isGameRuelRunning :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click_pos = pygame.mouse.get_pos()
                        print(click_pos)
                        match page :
                            case 1 :
                                if distance(nextPageButton_Cpos1,click_pos) <= 40 :
                                    page += 1
                            case 2 :
                                if distance(nextPageButton_Cpos2,click_pos) <= 40 :
                                    page += 1
                            case 3 :
                                if distance(backPageButton_Cpos,click_pos) <= 40 :
                                    page -= 1
                                if distance(backtoMenuButton_Cpos,click_pos) <= 30:
                                    event_type = 1 #-> GameMenu
                                    isGameRuelRunning = False
                screen.fill(woodBGColor)   
                match page :
                    case 1:
                        screen.blit(ruleNotePage1,(160,90))
                    case 2:
                        screen.blit(ruleNotePage2,(160,90))
                    case 3:
                        screen.blit(ruleNotePage3,(160,90))
                pygame.display.update()
        #SelectGameNumber
        case 3 :
            if fromInGameMenu :
                gameNumber = 2
                totalTurn = 60
            while isGameNumberRunning :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click_pos = pygame.mouse.get_pos()
                        print(click_pos)
                        if distance(gameNumberInGameMenuButton_Cpos,click_pos) <= 40 :
                            event_type = 6 #-> InGameMenu
                            mevent_type = 3
                            isGameNumberRunning = False
                            isInGameMenuRunning = True
                        match gameNumber :
                            case 2 :
                                if clickButton(gameNumberPlusButton_pos1,gameNumberPlusButton_pos2,click_pos) :
                                    gameNumber += 1
                            case 3 :
                                if clickButton(gameNumberPlusButton_pos1,gameNumberPlusButton_pos2,click_pos) :
                                    gameNumber += 1
                                if clickButton(gameNumberMinusButton_pos1,gameNumberMinusButton_pos2,click_pos) :
                                    gameNumber -= 1
                            case 4 :
                                if clickButton(gameNumberMinusButton_pos1,gameNumberMinusButton_pos2,click_pos) :
                                    gameNumber -= 1
                        if distance(gameNumberCheckButton_Cpos,click_pos) <= 20 :
                            event_type = 4 #->Game
                            fromInGameMenu = True
                            isGameNumberRunning = False
                match gameNumber :
                    case 2 :
                        screen.blit(selectGameNumber2,(0,0))
                    case 3 :
                        screen.blit(selectGameNumber3,(0,0))
                    case 4 :
                        screen.blit(selectGameNumber4,(0,0))
                pygame.display.update()
        #Game
        case 4 :
            if fromInGameMenu :
                isloading = 0
                gameTurn = 0
                #general setting
                phase = 1
                turn = 0
                haveRaido = False
                haveCYticket = False
                haveComplimentaryTicket = False
                #players
                players = []
                setPlayers(players,gameNumber)
                failed_players = []
                #blocks
                normal_phase = 0
                normal2_phase = 1
                buyBlock_textX = 0
                unis_phase = 1
                worldTour_phase = 1
                worldTour_pos = [0,0]
                worldTour_textX = 0
                olympic_phase = 1
                olympic_pos = [0,0]
                olympic_textX = 0
                have_block = False
                #dice
                dice = [0,0]
                tempDice = 0
                #cards
                tempCard = 0
                cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
                chanceCard_phase = 1
                playerMove = False
                for i in range(30) :
                    cardsSwap(cards,random.randint(0,20),random.randint(0,20))
            while isGameRunning :
                #이미지 불러오기
                screen.blit(mapBoard,mapBoard_pos)
                drawGameUI(gameNumber)
                drawTurnMarker(turn)
                match phase :
                #[움직이기 전]
                    #<case 1> - 파산한 플레이어 확인
                    case 1 :
                        isloading += 1
                    case 2 :
                        isloading += 1
                    case 3 :
                        if haveRaido :
                            screen.blit(card4YorNI,gamePhaseMenu_pos)
                    case 4 :
                        screen.blit(diceButton,diceButton_pos)
                    case 5 :
                        match unis_phase :
                            case 1 :
                                screen.blit(diceButton,diceButton_pos)
                    case 6 :
                        screen.blit(selectWorldTour_pos,gamePhaseMenu_pos)
                        match worldTour_phase :
                            case 1 :
                                text = blocks[worldTour_pos[0]][worldTour_pos[1]].name
                                worldTourBlockName_text = normal_font.render(text,True,black)
                                if len(text) == 2 :
                                    worldTour_textX = 313
                                elif len(text) == 3 :
                                    worldTour_textX = 278
                                elif len(text) == 4 :
                                    worldTour_textX = 253
                                else :
                                    worldTour_textX = 128
                                screen.blit(worldTourBlockName_text,(gamePhaseMenu_pos[0]+worldTour_textX,gamePhaseMenu_pos[1]+100))
                    case 7 :
                        screen.blit(double,gamePhaseMenu_pos)
                    case 8 :
                        screen.blit(startMenu,gamePhaseMenu_pos)
                    case 9 :
                        isloading += 1
                    case 10 :
                        screen.blit(selectOlympicTour_pos,gamePhaseMenu_pos)
                        match normal_phase :
                            case 1 :
                                screen.blit(buybuilding,gamePhaseMenu_pos)
                            case 2 :
                                screen.blit(card5YorNI,gamePhaseMenu_pos)
                            case 3 :
                                text = blocks[x][y].name
                                buyBlock_text = normal_font.render(text,True,black)
                                if len(text) == 2 :
                                    buyBlock_textX = 313
                                elif len(text) == 3 :
                                    buyBlock_textX = 278
                                elif len(text) == 4 :
                                    buyBlock_textX = 253
                                else :
                                    buyBlock_textX = 128
                                screen.blit(buyBlock_text,(gamePhaseMenu_pos[0]+buyBlock_textX,gamePhaseMenu_pos[1]+100))
                    case 11 :
                        screen.blit(startMenu,gamePhaseMenu_pos)
                    case 12 :
                        screen.blit(uninhabitedIslandMenu,gamePhaseMenu_pos)
                    case 13 :
                        screen.blit(worldTourMenu,gamePhaseMenu_pos)
                        text = blocks[olympic_pos[0]][olympic_pos[1]].name
                        olympicBlockName_text = normal_font.render(text,True,black)
                        if len(text) == 2 :
                            olympic_textX = 313
                        elif len(text) == 3 :
                            olympic_textX = 278
                        elif len(text) == 4 :
                            olympic_textX = 253
                        else :
                            olympic_textX = 128
                        screen.blit(olympicBlockName_text,(gamePhaseMenu_pos[0]+olympic_textX,gamePhaseMenu_pos[1]+100))
                    case 14 :
                        screen.blit(worldTourMenu,gamePhaseMenu_pos)
                    case 15 :
                        isloading += 1
                    case 16 :
                        isloading += 1
                    case 17 :
                        isloading += 1
                    case 19 :
                        isloading += 1
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click_pos = pygame.mouse.get_pos()
                        print(click_pos)
                        if distance(gameInGameMenuButton_Cpos,click_pos) <= 40 :
                            event_type = 6 #-> inGameMenu
                            mevent_type = 4
                            isGameRunning = False
                            isInGameMenuRunning = True
                        match phase :
                        #[움직이기 전]
                            #<case 1> - 파산한 플레이어 확인
                            case 1 :
                                if players[turn].fortune <= 0 :
                                    turn+=1
                                else :
                                    phase = 2
                                #-차례인 플레이어가 파산했다면 턴 증가
                                #-아니라면 <2>로 이동
                            #<case 2> - 현위치의 블록이 무인도, 세계여행인 경우 확인
                            case 2 :
                                x = players[turn].pos[0]
                                y = players[turn].pos[1]
                                current_block_type = blocks[x][y].type
                                if current_block_type == 2 :
                                    phase = 3
                                elif current_block_type == 4 :
                                    phase = 6
                                else :
                                    phase = 4
                                #-현위치의 블록이 무인도이면 <3>으로 이동
                                #-현위치의 블록이 세계여행이라면 <6>으로 이동
                            #<case 3> - 무인도인 경우 아이템 유무를 확인 / 아이템 사용 여부를 확인 / 무인도에서 3턴이 지난 경우를 확인
                            case 3 :
                                if players[turn].inUnIsTurn <= 3 :
                                    for i in range(players[turn].item) :
                                        if i == 4 :
                                            haveRaido = True
                                    if haveRaido :
                                        screen.blit(card4YorNI,gamePhaseMenu_pos)
                                        if distance(phaseMenuYesButton_Cpos,click_pos) <= 65 :
                                            phase = 4
                                        if distance(phaseMenuNoButton_Cpos,click_pos) <= 65 :
                                            phase = 5
                                    else :
                                        phase = 5
                                else :
                                    phse = 5
                                #-(1-라디오가 있다면)
                                #-사용 여부 확인
                                #-(2-사용한다면-O을 클릭한다면)
                                #-<4>로 이동
                                #-(2-사용하지 않는다면-X를 클릭한다면)
                                #-<5>로 이동
                                #-(1-라디오가 없다면)
                                #-<5>로 이동
                            #[움직이기]
                            #<case 4> - 주사위를 굴리고 움직이기
                            case 4 :
                                if distance(diceButton_Cpos,click_pos) <= 100:
                                    dice[0] = random.randint(1,6)
                                    dice[1] = random.randint(1,6)
                                    before_pos = players[turn].pos
                                    print('before :',players[turn].pos)
                                    players[turn].move(dice[0]+dice[1])
                                    after_pos = players[turn].pos
                                    print('after :',players[turn].pos)
                                    phase = 7
                                #-(1-주사위 버튼을 누르면)
                                #-주사위 굴리기
                                #-플레이어 이동
                                #-<7>로 이동
                            #<case 5> - 움직이기 전 위치가 무인도인 경우 움직이기
                            case 5 :
                                match unis_phase :
                                    case 1 :
                                        screen.blit(diceButton,diceButton_pos)
                                        if distance(diceButton_Cpos,click_pos) <= 100 :
                                            dice[0] = random.randint(1,6)
                                            dice[1] = random.randint(1,6)
                                            before_pos = players[turn].pos
                                            print('before :',players[turn].pos)
                                            unis_phase = 2
                                    case 2 :
                                        if isDouble(dice) or players[turn].inUnIsTurn:
                                            players[turn].move(dice[0]+dice[1])
                                            after_pos = players[turn].pos
                                            print('after :',players[turn].pos)
                                            phase = 8
                                        else :
                                            phase = 16
                                #-(1-주사위 버튼을 누르면)
                                #-주사위 굴리기
                                #-(2-더블이라면 or 무인도에서 3턴 이상 지났다면)
                                #-플레이어 이동
                                #-<8>로 이동
                                #-아니면 <15>로 이동
                            #<case 6> - 세계여행인 경우 블록 선택 후 움직이기
                            case 6 :
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
                                #-(블록선택) 개발중
                                #-선택한 곳으로 이동
                                #-<9>로 이동
                                #[움직인 후]
                            #<case 7> - 더블인 경우 다시 굴리기
                            case 7 :
                                if isDouble(dice) :
                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                        phase = 4
                                else :
                                    phase = 8
                                #-(1-더블이면)
                                #-<4>로 이동
                                #-(1-아니면)
                                #-<8>로 이동
                            #<case 8> - 출발지를 지났는지 확인 후 월급 지급
                            case 8 :
                                if before_pos[1] != 0 and after_pos[1] == 0 :
                                    players[turn].getMoney(200000)
                                    players[turn].lap+=1
                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                        phase = 9
                                #-(1-출발지를 지났다면)
                                #-월급 지급
                                #-<9>로 이동
                            #<case 9> - 블록 종류 확인 종류에 따라 실행
                            case 9 :
                                x = players[turn].pos[0]
                                y = players[turn].pos[1]
                                current_block_type = blocks[x][y].type
                                match current_block_type :
                                    case 0 :
                                        phase = 10
                                    case 1 :
                                        phase = 11
                                    case 2 :
                                        phase = 12
                                    case 3 :
                                        phase = 13
                                    case 4 :
                                        phase = 14
                                    case 5 :
                                        phase = 15
                                #-(1-일반블록이면)
                                #-<10>으로 이동
                                #-(1-시작이면)
                                #-<11>로 이동
                                #-(1-무인도이면)
                                #-<12>로 이동
                                #-(1-올림픽이면)
                                #-<13>로 이동
                                #-(1-세게여행이면)
                                #-<14>으로 이동
                                #-(1-찬스카드이면)
                                #-<15>로 이동
                            #<case 10> - 일반 블록인 경우
                            case 10 :
                                if blocks[x][y].owned == turn :
                                    normal_phase = 1
                                elif blocks[x][y].owned == 5 :
                                    normal_phase = 3
                                else :
                                    normal_phase = 2
                                match normal_phase :
                                    case 1 :
                                        if blocks[x][y].visit >= 2 and len(blocks[x][y].building) <= 1 and players[turn].fortune > blocks[x][y].bdPrice[0]:
                                            if distance(villaButton_Cpos,click_pos) <= 75 :
                                                players[turn].pay(blocks[x][y].bdPrice[0])
                                                blocks[x][y].build(0)
                                                phase = 16
                                            if distance(buildingButton_Cpos,click_pos) <= 75 and players[turn].fortune <= blocks[x][y].bdPrice[1] :
                                                players[turn].pay(blocks[x][y].bdPrice[1])
                                                blocks[x][y].build(1)
                                                phase = 16
                                            if distance(hotelButton_Cpos,click_pos) <= 75 and players[turn].fortune <= blocks[x][y].bdPrice[2] :
                                                players[turn].pay(blocks[x][y].bdPrice[2])
                                                blocks[x][y].build(2)
                                                phase = 16
                                        else :
                                            phase = 16
                                    case 2 :
                                        for i in range(players[turn].item) :
                                            if i == 5 :
                                                haveCYticket = True
                                        if haveCYticket :
                                            if distance(phaseMenuYesButton_Cpos,click_pos) <= 65 :
                                                phase = 16
                                            if distance(phaseMenuNoButton_Cpos,click_pos) <= 65 :
                                                players[turn].pay(blocks[x][y].tall)
                                                if blocks[x][y].olympic :
                                                    players[blocks[x][y].owned].getMoney(blocks[x][y].tall*2)
                                                else :
                                                    players[blocks[x][y].owned].getMoney(blocks[x][y].tall)
                                                phase = 16
                                        else :
                                            players[turn].pay(blocks[x][y].tall)
                                            if blocks[x][y].olympic :
                                                players[blocks[x][y].owned].getMoney(blocks[x][y].tall*2)
                                            else :
                                                players[blocks[x][y].owned].getMoney(blocks[x][y].tall)
                                            phase = 16
                                    case 3 :
                                        if players[turn].fortune <= blocks[x][y].price :
                                            if distance(phaseMenuYesButton_Cpos,click_pos) <= 65 :
                                                players[turn].pay(blocks[x][y].price)
                                                blocks[x][y].buy(turn)
                                            if distance(phaseMenuNoButton_Cpos,click_pos) <= 65 :
                                                phase = 16
                                        else :
                                            phase = 16
                                #-(1-자신이 소유한 블록이면)
                                #-(2-현재 위치 블록의 방문 횟수가 2번 이상이면 and 현재 위치 블록의 건물의 수가 1개 이하이면)
                                #-(버튼을 클릭하여 종류 선택)
                                #-현재 위치에 건물 종류 받기
                                ##현재 보유한 돈으로 지을 수 있는 건물 버튼만 출력
                                #-(3-별장이면)
                                #-현재 위치 블록의 별장 짓기
                                #-(3-빌딩이면)
                                #-현재 위치 블록의 빌딩 짓기
                                #-(3-호텔이면)
                                #-현재 위치 블록의 호텔 짓기
                                #-(1-상대가 소유한 블록이면)
                                #-(2-우대권이 있다면)
                                #-사용 여부 확인
                                #-(3-사용한다면-O을 클릭한다면)
                                #-<16>로 이동
                                #-(3-사용하지 않는다면-X를 클릭한다면)
                                #-통행료 지불
                                #-<16>로 이동
                                #-(2-우대권이 없다면)
                                #-통행료 지불
                                #-<16>로 이동
                                #-(1-아무도 소유하지 않은 블록이면)
                                #-(2-보유한 재산으로 구매 할 수 있다면)
                                #-(2-구매한다면-O를 클릭한다면)
                                #-블록을 구매
                                #-(3-구매한다면-X를 클릭한다면)
                                #-<16>로 이동
                            #<case 11> - 시작인 경우
                            case 11 :
                                phase = 16
                            #<case 12> - 무인도인 경우
                            case 12 :
                                phase = 16
                                #-<16>로 이동
                            #<case 13> - 올림픽인 경우
                            case 13 :
                                for i in range(4) :
                                    for j in range(8) :
                                        blocks[j][i].owned == turn
                                        have_block = True
                                if have_block :
                                    match olympic_phase :
                                        case 1 :
                                            if distance(phaseMenuPlustButton_Cpos,click_pos) <= 60 :
                                                olympic_pos[0]+=1
                                                while olympic_pos[0] > 7 :
                                                    olympic_pos[1]+=1
                                                    olympic_pos[0]-=8
                                                    while olympic_pos[1] > 3 :
                                                        olympic_pos[1]-=4
                                            if distance(phaseMenuMinusButton_Cpos,click_pos) <= 60 :
                                                olympic_pos[0]-=1
                                                while olympic_pos[0] < 0 :
                                                    olympic_pos[1]-=1
                                                    olympic_pos[0]=7
                                                    while olympic_pos[1] < 0 :
                                                        olympic_pos[1]=3
                                            if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                olympic_phase = 2
                                        case 2 :
                                            if blocks[olympic_pos[0]][olympic_pos[1]].owned == turn :
                                                blocks[olympic_pos[0]][olympic_pos[1]].buff()
                                            else :
                                                olympic_phase = 1
                                else :
                                    phase = 16
                                #-(1-자신이 소유한 블록이 있다면)
                                #-(블록선택) 개발중
                                #-(2-선택한 블록이 자신의 소유이면)
                                #-버프주기
                                #-(2-자신의 소유가 아니라면)
                                #-다시 선택
                                #-(1-없다면)
                                #-<16>로 이동
                            #<case 14> - 세계여행인 경우
                            case 14 :
                                phase = 16
                                #-<16>로 이동
                            #<case 15> - 찬스카드인 경우
                            case 15 :
                                tempCard = 0
                                match chanceCard_phase :
                                    case 1 :
                                        if 1 <= cards[0] <= 3 : #효과가 건물 유지비 지불인 경우
                                            building_type1 = 0
                                            building_type2 = 0
                                            building_type3 = 0
                                            for i in range(4) :
                                                for j in range(5) :
                                                    if blocks[j][i].owned == turn :
                                                        for k in range(2) :
                                                            match blocks[j][i].building[k] :
                                                                case 1 :
                                                                    building_type1+=1
                                                                case 2 :
                                                                    building_type2+=1
                                                                case 3 :
                                                                    building_type3+=1
                                            match cards[0] :
                                                case 1 : #1.정기종합소득세
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].pay(building_type1*30000 + building_type2*100000 + building_type3*150000)
                                                        chanceCard_phase = 2
                                                case 2 : #2.건물수리비 지불
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].pay(building_type1*30000 + building_type2*60000 + building_type3*100000)
                                                        chanceCard_phase = 2
                                                case 3 : #3.방범비
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].pay(building_type1*10000 + building_type2*30000 + building_type3*50000)
                                                        chanceCard_phase = 2
                                        elif 2 <= cards[0] <= 3 : #효과가 획득인 경우
                                            match cards[0] :
                                                case 2 : #4.무인도 탈출권(무전기)
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].items.append(4)
                                                        cards.remove(4)
                                                        chanceCard_phase = 2
                                                case 2 : #5.우대권
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].items.append(5)
                                                        cards.remove(5)
                                                        chanceCard_phase = 2
                                        elif 6 <= cards[0] <= 11 : #효과가 이동인 경우
                                            playerMove = True
                                            match cards[0] :
                                                case 6 : #6.앞으로 이동
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        dice[0] = random.randint(1,6)
                                                        dice[1] = random.randint(1,6)
                                                        beforeYpos = players[turn].pos[1]
                                                        print('before :',players[turn].pos)
                                                        players[turn].move(2)
                                                        afterYpos = players[turn].pos[1]
                                                        print('after :',players[turn].pos)
                                                        chanceCard_phase = 2
                                                case 7 : #7.무인도
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        unIs_pos = (0,1)
                                                        players[turn].tp(unIs_pos)
                                                        chanceCard_phase = 2
                                                case 8 : #8.올림픽 관람 초대권
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        olympic_pos = (0,2)
                                                        players[turn].tp(olympic_pos)
                                                        chanceCard_phase = 2
                                                case 9 : #9.세계여행 초대권
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        olympic_pos = (0,3)
                                                        players[turn].tp(olympic_pos)
                                                        chanceCard_phase = 2
                                                case 10 : #10.세계일주 초대권
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        start_pos = (0,0)
                                                        players[turn].tp(start_pos)
                                                        players[turn].getMoney(200000)
                                                        chanceCard_phase = 2
                                                case 11 : #11.고속도로
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].getMoney(200000)
                                                        chanceCard_phase = 2
                                        else : #상금 지불 기타
                                            match cards[0] :
                                                #상금
                                                case 12 : #12.노벨평화상 수상
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].getMoney(300000)
                                                        chanceCard_phase = 2
                                                case 13 : #13.복권 당첨
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].getMoney(200000)
                                                        chanceCard_phase = 2
                                                case 14 : #14.자동차 경주에서의 우승
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].getMoney(100000)
                                                        chanceCard_phase = 2
                                                case 15 : #15.장학금 혜택
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].getMoney(100000)
                                                        chanceCard_phase = 2
                                                case 16 : #16.연금 혜택
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].getMoney(50000)
                                                        chanceCard_phase = 2
                                                #지불
                                                case 17 : #17.해외유학
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].pay(100000)
                                                        chanceCard_phase = 2
                                                case 18 : #18.병원비
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].pay(50000)
                                                        chanceCard_phase = 2
                                                case 19 : #19.과속운전 벌금
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        players[turn].pay(50000)
                                                        chanceCard_phase = 2
                                                #기타
                                                case 20 : #20.생일축하
                                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                                        for i in range(gameNumber) :
                                                            players[i].pay(10000)
                                                        players[turn].getMoney(gameNumber*10000)
                                                        chanceCard_phase = 2
                                    case 2 :
                                        if playerMove :
                                            phase = 9
                                        else :
                                            phase = 16
                                #-효과 발동
                                #-다음 버튼을 누르면
                                #-<16>로 이동
                            #[턴 종료]
                            #<case 16> - 파산 조건 확인
                            case 16 :
                                for i in range(gameNumber) :
                                    players[i].fortune <= 0
                                    failed_players.append(i)
                            #<case 17> - 승리 조건 확인
                            case 17 :
                                if len(failed_players) >= gameNumber - 1 or gameTurn >= totalTurn :
                                    isGameRunning = False
                                    event_type = 5
                                else :
                                    phase = 18
                            #<case 18> - 방문 횟수 증가
                            case 18 :
                                for i in range(gameNumber) :
                                    if blocks[players[i].pos[0]][players[i].pos[1]].type == 2 :
                                        players[i].inUnIsTurn+=1
                                    if blocks[players[i].pos[0]][players[i].pos[1]].owned == i :
                                        blocks[players[i].pos[0]][players[i].pos[1]].visit+=1
                            #<case 19> - 턴 증가
                            case 19 :
                                #general setting
                                haveRaido = False
                                haveCYticket = False
                                haveComplimentaryTicket = False
                                #blocks
                                normal_phase = 0
                                normal2_phase = 1
                                unis_phase = 1
                                worldTour_phase = 1
                                worldTour_pos = [0,0]
                                worldTour_textX = 0
                                olympic_phase = 1
                                olympic_pos = [0,0]
                                olympic_textX = 0
                                have_block = False
                                #dice
                                chanceCard_phase = 1
                                playerMove = False
                                turn+=1
                                if turn >= gameNumber :
                                    turn = 0
        #Ending 
        case 5 :
            while isEndRunning :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                screen.blit(endingPhase,(0,0))
                #for i in range(len(players)) :
                #    if players[i].fortune < players[i+1] :
                #        
                pygame.display.update()
        #InGameMenu
        case 6 :
            while isInGameMenuRunning :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click_pos = pygame.mouse.get_pos()
                        print(click_pos)
                        if clickButton(inGameMenuContinueButton_pos1,inGameMenuContinueButton_pos2,click_pos) :
                            isInGameMenuRunning = False
                            fromInGameMenu = False
                            event_type = mevent_type
                        if clickButton(inGameMenuBackToMenuButton_pos1,inGameMenuBackToMenuButton_pos2,click_pos) :
                            isInGameMenuRunning = False
                            event_type = 1
                        if clickButton(inGameMenuExitButton_pos1,inGameMenuExitButton_pos2,click_pos) :
                            isInGameMenuRunning = False
                            sys.exit()
                screen.blit(inGameMenu,(0,0))
                pygame.display.update()
########Logic#######