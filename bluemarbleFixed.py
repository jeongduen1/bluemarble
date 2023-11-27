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
#images
gameMenuBoard = pygame.image.load("images/1.GameMenuImages/GameMenu.png").convert()
#positions
gameMenuBoard_pos = (0,0)
menuStartButton_pos1 = (882, 469)
menuStartButton_pos2 = (1358, 581)
gameRuleButton_pos1 = (882, 612)
gameRuleButton_pos2 = (1358, 725)
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
normalMenu = pygame.image.load("images/4.GameImages/UI/BuyPhase.png").convert()
startMenu = pygame.image.load("images/4.GameImages/UI/startblockPhase.png").convert()
uninhabitedIslandMenu = pygame.image.load("images/4.GameImages/UI/muindoblockmenu.png").convert()
olympicMenu = pygame.image.load("images/4.GameImages/UI/olympicblockphase.png").convert()
worldTourMenu = pygame.image.load("images/4.GameImages/UI/worldtourblockmenu.png").convert()
chanceCardMenu = pygame.image.load("images/4.GameImages/UI/chancecardblockmenu.png").convert()
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
gamePhaseMenu_pos = (163,163)
phaseMenuYesButton_Cpos = (388,763)
phaseMenuNoButton_Cpos = (688,763)
phaseMenuNextButton_pos1 = (366,750)
phaseMenuNextButton_pos2 = (879,840)
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

#######Classes######
#player
class Player :
    def __init__(self) :
        self.fortune = 500000
        self.ownedLands = []
        self.items = []
        self.pos = [0,0]
        self.lap
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
        self.building = []
        self.bd1Price = 0
        self.bd1Tall = 0
        self.bd2Price = 0
        self.bd2Tall = 0
        self.bd3Price = 0
        self.bd3Tall = 0
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
def setPlayers(arr,num) :
    for i in range(num) :
        arr.append(Player())
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
                screen.blit(gameMenuBoard,gameMenuBoard_pos)
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
                        if distance(gameNumberCheckButton_Cpos,click_pos) < 20 :
                                    event_type = 4 #->Game
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
                phase = 0
                turn = 0
                gameTurn = 0
                dice = [0,0]
                double = False
                players = []
                players.clear()
                setPlayers(players,gameNumber)
                failedPlayers = []
                normalBlockPhase = 0
                ownedNormalBlockPhase = 0
                unIsPhase = 0
                worldTour_pos = []
                cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
            while isGameRunning :
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
                            case 0 : #파산 여부 확인
                                for i in range(gameNumber) :
                                    if turn == failedPlayers[i] :
                                        turn+=1
                                    else :
                                        phase = 1
                            case 1 : #주사위 사용 이전 시전 효과 블록 종류 확인
                                x = players[turn].pos[0]
                                y = players[turn].pos[1]
                                current_block_type = blocks[x][y].type
                                if current_block_type == 1 :
                                    phase = 2 #무인도인 경우
                                elif current_block_type == 2 :
                                    phase = 3 #세계 여행인 경우
                                else :
                                    phase = 4 #다른 블록인 경우
                            case 2 : #무인도인 경우
                                match unIsPhase :
                                    case 0 : #아이템 유무 확인
                                        if len(players[turn].item) != 0 :
                                            unIsPhase = 1 #o
                                        else :
                                            unIsPhase = 3 #x
                                    case 1 : #무전기 유무 확인
                                        for i in range(players[turn].item) :
                                            if i == 4 :
                                                unIsPhase = 2 #o
                                            else :
                                                unIsPhase = 3 #x
                                    case 2 : #무전기 사용 여부 확인
                                        if distance(phaseMenuYesButton_Cpos,click_pos) :
                                            players[turn].items.remove(4)
                                            cards.append(4)
                                            phase = 4 #사용o
                                        if distance(phaseMenuNoButton_Cpos,click_pos) :
                                            unIsPhase = 3 #사용x
                                    case 3 : #무전기를 사용하지 않은 경우의 이동
                                        if distance(diceButton_Cpos,click_pos) <= 80:
                                            dice[0] = random.randint(1,6)
                                            dice[1] = random.randint(1,6)
                                            if dice[0] == dice[1] or players[turn].inUnIsTurn > 3 :
                                                beforeYpos = players[turn].pos[1]
                                                print('before :',players[turn].pos)
                                                players[turn].move(dice[0]+dice[1])
                                                afterYpos = players[turn].pos[1]
                                                print('after :',players[turn].pos)
                                                phase = 6
                                            else :
                                                phase = 7
                            case 3 : #세계 여행인 경우
                                beforeYpos = players[turn].pos[1]
                                print('before :',players[turn].pos)
                                worldTour_pos =[0,0] #수정 세계 여행 위치 선택
                                players[turn].tp(worldTour_pos)
                                afterYpos = players[turn].pos[1]
                                print('after :',players[turn].pos)
                                phase = 6
                            case 4 : #무인도,세계 여행이 아닌 다른 블록인 경우의 이동
                                if distance(diceButton_Cpos,click_pos) <= 80:
                                    dice[0] = random.randint(1,6)
                                    dice[1] = random.randint(1,6)
                                    beforeYpos = players[turn].pos[1]
                                    print('before :',players[turn].pos)
                                    players[turn].move(dice[0]+dice[1])
                                    afterYpos = players[turn].pos[1]
                                    print('after :',players[turn].pos)
                                    if dice[0] == dice[1] :
                                        double = True
                                    phase = 5
                            case 5 : #출발지를 지났을 경우
                                if beforeYpos != 0 and beforeYpos == 0 :
                                    players[turn].getMoney(200000)
                                    players[turn].lap+=1
                                phase = 6
                            case 6 :
                                x = players[turn].pos[0]
                                y = players[turn].pos[1]
                                current_block_type = blocks[x][y].type
                                match current_block_type :
                                    case 0 : #일반 블록인 경우
                                        match normalBlockPhase :
                                            case 0 : #소유자가 없을 경우
                                                if blocks[x][y].owned == 5 :
                                                    if distance(phaseMenuYesButton_Cpos,click_pos) <= 65 :
                                                        blocks[x][y].buy(turn)
                                                        players[turn].pay(blocks[x][y].price)
                                                    if distance(phaseMenuNoButton_Cpos,click_pos) <= 65 :
                                                        phase = 7
                                                else : #소유자가 있는 경우
                                                    if blocks[x][y].owned == turn : #소유자가 자신인 경우
                                                        print('자신의 블록') #수정 자신의 블록인 경우 건물 건축
                                                        phase = 7
                                                    else : #소유자가 상대방인 경우
                                                        match ownedNormalBlockPhase :
                                                            case 0 : #아이템 유무 확인
                                                                if len(players[turn].item) != 0 :
                                                                    ownedNormalBlockPhase = 1 #o
                                                                else :
                                                                    ownedNormalBlockPhase = 3 #x
                                                            case 1 : #우대권 유무 확인
                                                                for i in range(players[turn].item) :
                                                                    if i == 5 :
                                                                        ownedNormalBlockPhase = 2 #o
                                                                    else :
                                                                        ownedNormalBlockPhase = 3 #x
                                                            case 2 : #우대권 사용 여부 확인
                                                                if distance(phaseMenuYesButton_Cpos,click_pos) :
                                                                    players[turn].items.remove(5)
                                                                    cards.append(5)
                                                                    phase = 7 #사용o
                                                                if distance(phaseMenuNoButton_Cpos,click_pos) :
                                                                    ownedNormalBlockPhase = 3 #사용x
                                                            case 3 : #우대권를 사용하지 않은 경우
                                                                players[turn].pay(blocks[x][y].tall)
                                                                players[blocks[x][y].owned].getMoney(blocks[x][y].tall)
                                    case 1 : #시작 블록인 경우
                                        phase = 7
                                    case 2 : #무인도인 경우
                                        phase = 7
                                    case 3 : #올림픽인 경우
                                        for i in range(4) :
                                            for j in range(8) :
                                                if blocks[j][i].owned == turn : #소유한 블록이 있는 경우
                                                    print('올림픽 사용')#수정 올림픽 버프 블록 선택
                                                else : #소유한 블록이 없는 경우
                                                    phase = 7
                                    case 4 : #세계 여행인 경우
                                        phase = 7
                                    case 5 : #황금열쇠 블록인 경우
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
                                                    players[turn].pay(building_type1*30000 + building_type2*100000 + building_type3*150000)
                                                case 2 : #2.건물수리비 지불
                                                    players[turn].pay(building_type1*30000 + building_type2*60000 + building_type3*100000)
                                                case 3 : #3.방범비
                                                    players[turn].pay(building_type1*10000 + building_type2*30000 + building_type3*50000)
                                        elif 2 <= cards[0] <= 3 : #효과가 획득인 경우
                                            match cards[0] :
                                                case 2 : #4.무인도 탈출권(무전기)
                                                    players[turn].items.append(4)
                                                case 2 : #5.우대권
                                                    players[turn].items.append(4)
                                        elif 6 <= cards[0] <= 11 : #효과가 이동인 경우
                                            match cards[0] :
                                                case 6 : #6.앞으로 이동
                                                    dice[0] = random.randint(1,6)
                                                    dice[1] = random.randint(1,6)
                                                    beforeYpos = players[turn].pos[1]
                                                    print('before :',players[turn].pos)
                                                    players[turn].move(2)
                                                    afterYpos = players[turn].pos[1]
                                                    print('after :',players[turn].pos)
                                                    phase = 5
                                                case 7 : #7.무인도
                                                    unIs_pos = (0,1)
                                                    players[turn].tp(unIs_pos)
                                                    phase = 7
                                                case 8 : #8.올림픽 관람 초대권
                                                    olympic_pos = (0,2)
                                                    players[turn].tp(olympic_pos)
                                                    phase = 6
                                                case 9 : #9.세계여행 초대권
                                                    olympic_pos = (0,3)
                                                    players[turn].tp(olympic_pos)
                                                    phase = 7
                                                case 10 : #10.세계일주 초대권
                                                    start_pos = (0,0)
                                                    players[turn].tp(start_pos)
                                                    players[turn].getMoney(200000)
                                                    phase = 7
                                                case 11 : #11.고속도로
                                                    players[turn].getMoney(200000)
                                                    phase = 7
                                        else : #상금 지불 기타
                                            match cards[0] :
                                                #상금
                                                case 12 : #12.노벨평화상 수상
                                                    players[turn].getMoney(300000)
                                                case 13 : #13.복권 당첨
                                                    players[turn].getMoney(200000)
                                                case 14 : #14.자동차 경주에서의 우승
                                                    players[turn].getMoney(100000)
                                                case 15 : #15.장학금 혜택
                                                    players[turn].getMoney(100000)
                                                case 16 : #16.연금 혜택
                                                    players[turn].getMoney(50000)
                                                #지불
                                                case 17 : #17.해외유학
                                                    players[turn].pay(100000)
                                                case 18 : #18.병원비
                                                    players[turn].pay(50000)
                                                case 19 : #19.과속운전 벌금
                                                    players[turn].pay(50000)
                                                #기타
                                                case 20 : #20.생일축하
                                                    for i in range(gameNumber) :
                                                        players[i].pay(10000)
                                                    players[turn].getMoney(gameNumber*10000)
                            case 7 :
                                gameTurn+=1
                                for i in range(gameNumber) :
                                    if players[i].fortune <= 0 :
                                        failedPlayers.append(i)
                                if len(failedPlayers) >= gameNumber-1 :
                                    isGameRunning = False
                                    event_type = 5
                                elif totalTurn <= gameTurn :
                                    isGameRunning = False
                                    event_type = 5
                                else :
                                    turn+=1
                                    if turn >= gameNumber :
                                        turn = 0
                                    phase = 0
                screen.blit(mapBoard,mapBoard_pos)
                drawGameUI(gameNumber)
                drawTurnMarker(turn)

                match phase :
                    case 1 :
                        screen.blit(diceButton,diceButton_pos)
                    case 2 :
                        match current_block_type :
                            case 0 :
                                screen.blit(normalMenu,gamePhaseMenu_pos)
                            case 1:
                                print('')
                            case 2 :
                                screen.blit(uninhabitedIslandMenu,gamePhaseMenu_pos)
                            case 3 :
                                screen.blit(olympicMenu,gamePhaseMenu_pos)
                            case 4 :
                                screen.blit(worldTourMenu,gamePhaseMenu_pos)
                            case 5 :
                                screen.blit(chanceCardMenu,gamePhaseMenu_pos)
        case 5 :
            while isEndRunning :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                pygame.display.update()
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