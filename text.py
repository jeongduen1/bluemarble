import pygame, sys, random, math
from pygame.locals import *
pygame.display.set_caption("BlueMarble")
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.init()
selectGameNumber2 = pygame.image.load("images/3.SelectGameNumberImages/SelectGameNumber2.png").convert()
selectGameNumber3 = pygame.image.load("images/3.SelectGameNumberImages/SelectGameNumber3.png").convert()
selectGameNumber4 = pygame.image.load("images/3.SelectGameNumberImages/SelectGameNumber4.png").convert()
gameNumberMinusButton_pos1 = (34, 527)
gameNumberMinusButton_pos2 = (91, 584)
gameNumberPlusButton_pos1 = (588, 526)
gameNumberPlusButton_pos2 = (644, 582)
gameNumberCheckButton_Cpos = (622, 303)
gameNumberInGameMenuButton_Cpos = (60,120)
mapBoard = pygame.image.load("images/4.GameImages/board/mapimage.png").convert()
gameUI2 = pygame.image.load("images/4.GameImages/UI/FortuneUI2.png").convert()
gameUI3 = pygame.image.load("images/4.GameImages/UI/FortuneUI3.png").convert()
gameUI4 = pygame.image.load("images/4.GameImages/UI/FortuneUI4.png").convert()
myTurnMarker = pygame.image.load("images/4.GameImages/markers/MTM.png").convert()
myTurnMarker.set_colorkey((0,95,65))
diceButton = pygame.image.load("images/4.GameImages/buttons/DiceButton.png").convert()
diceButton = pygame.transform.scale(diceButton,(200,200))
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
gameInGameMenuButton_Cpos = (1880, 40)
myTurnMarker_Redpos = (1130,10)
myTurnMarker_Bluepos = (1130,295)
myTurnMarker_Greenpos = (1510,10)
myTurnMarker_Yellowpos = (1515,295)
diceButton_pos = (1400,750)
diceButton_Cpos = (1500,850)
dice_pos1 = (1350,750)
dice_pos2 = (1500,750)
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
class Player :
    def __init__(self) :
        self.fortune = 500000
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
class Block :
    def __init__(self) :
        self.name = ''
        self.type = 0
        self.price = 0
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
blockNames = ['시작','타이베이','베이징','마닐라','찬스카드','싱가포르','카이로','이스탄불','무인도','아테네','코펜하겐','스톡콜롬','찬스카드','베른','베를린','오타와','올림픽','부에노스아이레스','상파울로','시드니','찬스카드','하와이','리스본','마드리드','세계여행','도쿄','파리','로마','찬스카드','런던','뉴욕','서울']
blocks = [[ Block() for j in range(4)] for i in range(8)]
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
for i in range(4) :
    for j in range(8) :
        blocks[j][i].name = blockNames[k]
        k+=1
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
isGameLogicRunning = True
event_type = 3
mevent_type = 1
fromInGameMenu = False
while isGameLogicRunning :
    isGameNumberRunning = True
    isGameRunning = True
    match event_type :
        case 3 :
            gameNumber = 2
            totalTurn = 60
            while isGameNumberRunning :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click_pos = pygame.mouse.get_pos()
                        print(click_pos)
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
        case 4 :
            isloading = 0
            gameTurn = 0
            phase = 1
            turn = 0
            haveRaido = False
            haveCYticket = False
            haveComplimentaryTicket = False
            players = []
            setPlayers(players,gameNumber)
            failed_players = []
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
            dice = []
            tempDice = 0
            tempCard = 0
            cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
            chanceCard_phase = 1
            playerMove = False
            for i in range(30) :
                cardsSwap(cards,random.randint(0,20),random.randint(0,20))
            while isGameRunning :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click_pos = pygame.mouse.get_pos()
                        print(click_pos)
                        screen.blit(mapBoard,(0,0))
                        drawGameUI(gameNumber)
                        drawTurnMarker(turn)
                        match phase :
                            case 1 :
                                if players[turn].fortune <= 0 :
                                    turn+=1
                                else :
                                    phase = 2
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
                            case 7 :
                                if isDouble(dice) :
                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                        phase = 4
                                else :
                                    phase = 8
                            case 8 :
                                if before_pos[1] != 0 and after_pos[1] == 0 :
                                    players[turn].getMoney(200000)
                                    players[turn].lap+=1
                                    if clickButton(phaseMenuNextButton_pos1,phaseMenuNextButton_pos2,click_pos) :
                                        phase = 9
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
                            case 11 :
                                phase = 16
                            case 12 :
                                phase = 16
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
                            case 14 :
                                phase = 16
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
                            case 16 :
                                for i in range(gameNumber) :
                                    players[i].fortune <= 0
                                    failed_players.append(i)
                            case 17 :
                                if len(failed_players) >= gameNumber - 1 or gameTurn >= totalTurn :
                                    isGameRunning = False
                                    event_type = 5
                                else :
                                    phase = 18
                            case 18 :
                                for i in range(gameNumber) :
                                    if blocks[players[i].pos[0]][players[i].pos[1]].type == 2 :
                                        players[i].inUnIsTurn+=1
                                    if blocks[players[i].pos[0]][players[i].pos[1]].owned == i :
                                        blocks[players[i].pos[0]][players[i].pos[1]].visit+=1
                            case 19 :
                                haveRaido = False
                                haveCYticket = False
                                haveComplimentaryTicket = False
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
                                chanceCard_phase = 1
                                playerMove = False
                                turn+=1
                                if turn >= gameNumber :
                                    turn = 0
                match phase :
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
                                worldTourBlockName_text = normal_font.render(text,True,(0,0,0))
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
                                buyBlock_text = normal_font.render(text,True,(0,0,0))
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
                        olympicBlockName_text = normal_font.render(text,True,(0,0,0))
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