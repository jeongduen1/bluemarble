import pygame, sys, random, math
from pygame.locals import *
pygame.init()
width = 1600
height = 900
pygame.display.set_caption("BlueMarble")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

###################################클래스###################################

#플레이어#
class Player :
    def __init__(self) :
        self.fortune = 500000
        self.ownedBlocks = []
        self.items = []
        self.uninhabitedIsland = 0
        self.pos = 0
        self.type = 0
    def move(self,num) :
        self.pos += num
players = []
#말판#
class Block :
    def __init__(self) :
        self.price = 0
        self.buildings = []
        self.belong = 0
        self.tall = 0
        self.pos = []
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

###################################색###################################

White = (255,255,255)
DarkGray = (89,89,89)
Black = (0,0,0)

###################################이미지,텍스트###################################

#시작 메뉴
GameMenu = pygame.image.load("images/UI/GameMenu.png").convert()
#시작 버튼
StartButton = pygame.image.load("images/buttons/StartButton.png").convert()
StartButton = pygame.transform.scale(StartButton,(200,200))
#게임 규칙 버튼
RuleButton = pygame.image.load("images/buttons/GameRuleButton.png").convert()
RuleButton = pygame.transform.scale(RuleButton,(400,130))
#게임규칙메뉴판
GameRuleMenuBoard = pygame.image.load("images/UI/GameRuleMenuBoard.png").convert()
GameRuleMenuBoard = pygame.transform.scale(GameRuleMenuBoard,(800,800))

RuleMenuButton1 = pygame.image.load("images/buttons/howcaniwin.png").convert()
RuleMenuButton2 = pygame.image.load("images/buttons/howplay.png").convert()
RuleMenuButton3 = pygame.image.load("images/buttons/GameRuleExitButton.png").convert()
#게임 규칙 메뉴 버튼
#다음페이지
GameRuleMenuNextPageBtn = pygame.image.load("images/buttons/NextPageButton.png").convert()
GameRuleMenuNextPageBtn = pygame.transform.scale(GameRuleMenuNextPageBtn,(50,50))
NextPageBtn_spawnPos = (width/2+250,height-100)
NextPageBtn_Pos = (width/2+275,height-75)
GameRuleMenuNextPageBtn.set_colorkey(White)
#이전페이지
GameRuleMenuBackPageBtn = pygame.image.load("images/buttons/BackPageButton.png").convert()
GameRuleMenuBackPageBtn = pygame.transform.scale(GameRuleMenuBackPageBtn,(50,50))
GameRuleMenuBackPageBtn.set_colorkey(White)
BackPageBtn_spawnPos = (width/2-300,height-100)
BackPageBtn_Pos = (width/2-275,height-75)
GameRuleExitBtn_pos = (0,0)
#게임 인원수 선택 버튼
GameNumButton2 = pygame.image.load("images/buttons/Two.png").convert()
GameNumButton2 = pygame.transform.scale(GameNumButton2,(200,250))
GameNumButton3 = pygame.image.load("images/buttons/Three.png").convert()
GameNumButton3 = pygame.transform.scale(GameNumButton3,(200,250))
GameNumButton4 = pygame.image.load("images/buttons/Four.png").convert()
GameNumButton4 = pygame.transform.scale(GameNumButton4,(200,250))
#게임 인원수 선택 텍스트
GameNumfont = pygame.font.Font("fonts/CookieRun Regular.ttf", 30)
GameNumtext = GameNumfont.render("플레이할 인원수를 선택하세요.", False, Black)
GameNumtext = pygame.transform.scale(GameNumtext,(800,100))
#플레이어 이미지
Player1Image = pygame.image.load("images/players/p1.png").convert()
Player1Image = pygame.transform.scale(Player1Image,(100,100))
Player1Image.set_colorkey(Black)
Player2Image = pygame.image.load("images/players/p1.png").convert()
Player2Image = pygame.transform.scale(Player1Image,(100,100))
Player2Image.set_colorkey(Black)
Player3Image = pygame.image.load("images/players/p1.png").convert()
Player3Image = pygame.transform.scale(Player1Image,(100,100))
Player3Image.set_colorkey(Black)
Player4Image = pygame.image.load("images/players/p1.png").convert()
Player4Image = pygame.transform.scale(Player1Image,(100,100))
Player4Image.set_colorkey(Black)
#말판 이미지
mapImage = pygame.image.load("images/board/mapimage.png").convert()
mapImage = pygame.transform.scale(mapImage,(height,height))


#Start텍스트
StartText = pygame.image.load("images/UI/StartText.png").convert()
StartText.set_colorkey(White)
#레드팀 상태 UI
RedTeamTurnText = pygame.image.load("images/UI/RedTeamTurnText.png").convert()
RedTeamTurnText.set_colorkey(White)
RedTeamUI = pygame.image.load("images/UI/RedTeamUI.png").convert()
RedTeamUI = pygame.transform.scale(RedTeamUI,(350,200))
#블루팀 상태 UI
BlueTeamTurnText = pygame.image.load("images/UI/BlueTeamTurnText.png").convert()
BlueTeamTurnText.set_colorkey(White)
BlueTeamUI = pygame.image.load("images/UI/BlueTeamUI.png").convert()
BlueTeamUI = pygame.transform.scale(BlueTeamUI,(350,200))
#그린팀 상태 UI
GreenTeamTurnText = pygame.image.load("images/UI/GreenTeamTurnText.png").convert()
GreenTeamTurnText.set_colorkey(White)
GreenTeamUI = pygame.image.load("images/UI/GreenTeamUI.png").convert()
GreenTeamUI = pygame.transform.scale(GreenTeamUI,(350,200))
#옐로팀 상태 UI
YellowTeamTurnText = pygame.image.load("images/UI/YellowTeamTurnText.png").convert()
YellowTeamTurnText.set_colorkey(White)
YellowTeamUI = pygame.image.load("images/UI/YellowTeamUI.png").convert()
YellowTeamUI = pygame.transform.scale(YellowTeamUI,(350,200))
#차례표식
TurnMarker = pygame.image.load("images/markers/TurnMarker.png").convert()
TurnMarker = pygame.transform.scale(TurnMarker,(65,65))
MyTurnMarker = pygame.image.load("images/markers/MyTurnMarker.png").convert()
MyTurnMarker = pygame.transform.scale(MyTurnMarker,(65,65))
TurnMarker_RedUIpos = (73,15)
TurnMarker_BlueUIpos = (73,225)
TurnMarker_GreenUIpos = (73,435)
TurnMarker_YellowUIpos = (73,645)
#주사위 버튼
RollButton = pygame.image.load("images/buttons/RollButton.png").convert()
RollButton = pygame.transform.scale(RollButton,(300,90))
RollButton_pos = (1300,750)
#주사위
dice_pos1 = (1350,height/2-32)
dice_pos2 = (1430,height/2-32)

dice1 = pygame.image.load("images/UI/d1.png").convert()
dice1 = pygame.transform.scale(dice1,(75,75))
dice1.set_colorkey(DarkGray)

dice2 = pygame.image.load("images/UI/d2.png").convert()
dice2 = pygame.transform.scale(dice2,(75,75))
dice2.set_colorkey(DarkGray)

dice3 = pygame.image.load("images/UI/d3.png").convert()
dice3 = pygame.transform.scale(dice3,(75,75))
dice3.set_colorkey(DarkGray)

dice4 = pygame.image.load("images/UI/d4.png").convert()
dice4 = pygame.transform.scale(dice4,(75,75))
dice4.set_colorkey(DarkGray)

dice5 = pygame.image.load("images/UI/d5.png").convert()
dice5 = pygame.transform.scale(dice5,(75,75))
dice5.set_colorkey(DarkGray)

dice6 = pygame.image.load("images/UI/d6.png").convert()
dice6 = pygame.transform.scale(dice6,(75,75))
dice6.set_colorkey(DarkGray)

###################################함수###################################

#카드#
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

#주사위#
def roll(arr) :
    arr[0] = random.randint(1,6)
    arr[1] = random.randint(1,6)

#계산#
def distance(x1, y1, x2, y2):
    result = math.sqrt( math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return result
#def playerPos(num) :
    #match num :
        #case 0:
        #case 1:
#출력#
def teamUIBlit(num) :
    match num :
        case 2:
            screen.blit(RedTeamUI,(0,10))
            screen.blit(BlueTeamUI,(0,220))
            screen.blit(TurnMarker,TurnMarker_RedUIpos)
            screen.blit(TurnMarker,TurnMarker_BlueUIpos)
        case 3:
            screen.blit(RedTeamUI,(0,10))
            screen.blit(BlueTeamUI,(0,220))
            screen.blit(GreenTeamUI,(0,430))
            screen.blit(TurnMarker,TurnMarker_RedUIpos)
            screen.blit(TurnMarker,TurnMarker_BlueUIpos)
            screen.blit(TurnMarker,TurnMarker_GreenUIpos)
        case 4:
            screen.blit(RedTeamUI,(0,10))
            screen.blit(BlueTeamUI,(0,220))
            screen.blit(GreenTeamUI,(0,430))
            screen.blit(YellowTeamUI,(0,640))
            screen.blit(TurnMarker,TurnMarker_RedUIpos)
            screen.blit(TurnMarker,TurnMarker_BlueUIpos)
            screen.blit(TurnMarker,TurnMarker_GreenUIpos)
            screen.blit(TurnMarker,TurnMarker_YellowUIpos)

def DrawDice(a,b) :
    match a :
        case 1:
            screen.blit(dice1,dice_pos1)
        case 2:
            screen.blit(dice2,dice_pos1)
        case 3:
            screen.blit(dice3,dice_pos1)
        case 4:
            screen.blit(dice4,dice_pos1)
        case 5:
            screen.blit(dice5,dice_pos1)
        case 6:
            screen.blit(dice6,dice_pos1)
    match b :
        case 1:
            screen.blit(dice1,dice_pos2)
        case 2:
            screen.blit(dice2,dice_pos2)
        case 3:
            screen.blit(dice3,dice_pos2)
        case 4:
            screen.blit(dice4,dice_pos2)
        case 5:
            screen.blit(dice5,dice_pos2)
        case 6:
            screen.blit(dice6,dice_pos2)

def MyTurnMakerDraw(num):
    match num :
            case 1 :
                screen.blit(MyTurnMarker,TurnMarker_RedUIpos)
            case 2 :
                screen.blit(MyTurnMarker,TurnMarker_BlueUIpos)
            case 3 :
                screen.blit(MyTurnMarker,TurnMarker_GreenUIpos)
            case 4 :
                screen.blit(MyTurnMarker,TurnMarker_YellowUIpos)

def PlayersDraw(num) :
    match num :
        case 1 :
            screen.blit(Player1Image,)

###################################로직###################################
CardShuffle(cards)
MapSet(maps)
for i in range(32) :
    print(maps[i].pos)
isRun = True
type = 1
while isRun :
    match type :
        case 1:
            isRunOne = True
            while isRunOne :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        StartMenuBtn_pos = pygame.mouse.get_pos()
                        if distance(StartMenuBtn_pos[0],StartMenuBtn_pos[1],width/2,height/2-50) <= 100:
                            type = 3
                            isRunOne = False
                        if width/2+200 >= StartMenuBtn_pos[0] >= width/2-200 and height/2+280 >= StartMenuBtn_pos[1] >= height/2+150:
                            type = 2
                            isRunOne = False
                screen.fill(White)
                screen.blit(GameMenu,(0,0))
                screen.blit(StartButton,(width/2-100,height/2-150))
                screen.blit(RuleButton,(width/2-200,height/2+150))
                pygame.display.update()
        case 2:
            isRunTwo = True
            RulePage = 1
            while isRunTwo :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        RuleMenuBtn_pos = pygame.mouse.get_pos()
                        if 560 >= RuleMenuBtn_pos[0] >= 175 and 720 >= RuleMenuBtn_pos[1] >= 580 :
                            type = 1
                            isRunTwo = False
                screen.fill((125,178,73))
                screen.blit(GameRuleMenuBoard,(52,75))
                screen.blit(RuleMenuButton1,(175,230))
                screen.blit(RuleMenuButton2,(175,405))
                screen.blit(RuleMenuButton3,(175,580))
                pygame.display.update()
        case 3:
            isRun = False

PlayresNum = 1
isRunOne = True
while isRunOne :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            PNBtnPos = pygame.mouse.get_pos()
            if PNBtnPos[0] >= width / 3 - 200 and PNBtnPos[0] <= width / 3 and PNBtnPos[1] >= 300 and PNBtnPos[1] <= 550 :
                PlayresNum = 2
                isRunOne = False
            if PNBtnPos[0] >= width / 2 - 100 and PNBtnPos[0] <= width / 2 + 100 and PNBtnPos[1] >= 300 and PNBtnPos[1] <= 550 :
                PlayresNum = 3
                isRunOne = False
            if PNBtnPos[0] >= width / 3 * 2 and PNBtnPos[0] <= width / 3 * 2 + 200 and PNBtnPos[1] >= 300 and PNBtnPos[1] <= 550 :
                PlayresNum = 4
                isRunOne = False
    screen.fill(White)
    screen.blit(GameNumtext,(width / 2-400, 100))
    screen.blit(GameNumButton2,(width / 3 - 200, 300))
    screen.blit(GameNumButton3,(width / 2 - 100, 300))
    screen.blit(GameNumButton4,(width / 3 * 2, 300))
    pygame.display.update()
for i in range(PlayresNum) :
    players.append(Player())
isRunTwo = True
Turn = 1
EventType = 1
dice = [0,0]
isRoll = False
isDouble = False
while isRunTwo :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        match EventType :
            case 1:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                    btnClick_pos = pygame.mouse.get_pos()
                    print(btnClick_pos[0],btnClick_pos[1])
                    if 1600 >= btnClick_pos[0] >= 1300 and 840 >= btnClick_pos[1] >= 750 :
                        dice[0] = random.randint(1,6)
                        dice[1] = random.randint(1,6)
                        Total = dice[0] + dice[1]
                        match Turn :
                            case 1 :
                                players[0].move(Total)
                                print(players[0].pos)
                            case 2 :
                                players[1].move(Total)
                                print(players[1].pos)
                            case 3 :
                                players[2].move(Total)
                                print(players[2].pos)
                            case 4 :
                                players[3].move(Total)
                                print(players[3].pos)
                        if dice[0] == dice[1] :
                            isDouble = True
                        isRoll = True
                        EventType = 2
    screen.fill((125,178,73))
    #게임오브젝트
    screen.blit(mapImage,(350,0))
    #UI
    teamUIBlit(PlayresNum)
    MyTurnMakerDraw(Turn)

    if isRoll:
        DrawDice(dice[0],dice[1])
    match EventType :
        case 1 :
            screen.blit(RollButton,RollButton_pos)
    pygame.display.update()