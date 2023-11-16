import pygame, sys, random, math
import players, blocks, cards, systems
from pygame.locals import *
pygame.init()
width = 1600
height = 900
pygame.display.set_caption("BlueMarble")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def roll(arr) :
    arr[0] = random.randint(1,6)
    arr[1] = random.randint(1,6)

def distance(x1, y1, x2, y2):
    result = math.sqrt( math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return result

def teamUIBlit() :
    screen.blit(RedTeamUI,(0,10))
    screen.blit(BlueTeamUI,(0,220))
    screen.blit(GreenTeamUI,(0,430))
    screen.blit(YellowTeamUI,(0,640))
    screen.blit(TurnMarker,TurnMarker_RedUIpos)
    screen.blit(TurnMarker,TurnMarker_BlueUIpos)
    screen.blit(TurnMarker,TurnMarker_GreenUIpos)
    screen.blit(TurnMarker,TurnMarker_YellowUIpos)

White = (255,255,255)
Black = (0,0,0)

#시작 메뉴
GameMenu = pygame.image.load("images/UI/GameMenu.png").convert()
#시작 버튼
StartButton = pygame.image.load("images/buttons/StartButton.png").convert()
StartButton = pygame.transform.scale(StartButton,(200,200))
#게임 규칙 버튼
RuleButton = pygame.image.load("images/buttons/GameRuleButton.png").convert()
RuleButton = pygame.transform.scale(RuleButton,(400,130))
#게임 규칙 UI
GameRuleP1 = pygame.image.load("images/UI/GameRulePage1.png").convert()
GameRuleP2 = pygame.image.load("images/UI/GameRulePage2.png").convert()
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
#나가기 버튼
GameRuleExitBtn = pygame.image.load("images/buttons/ExitButton.png").convert()
GameRuleExitBtn = pygame.transform.scale(GameRuleExitBtn,(100,100))
GameRuleExitBtn_pos =()
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
Player2Image = pygame.image.load("images/players/p1.png").convert()
Player2Image = pygame.transform.scale(Player1Image,(100,100))
Player3Image = pygame.image.load("images/players/p1.png").convert()
Player3Image = pygame.transform.scale(Player1Image,(100,100))
Player4Image = pygame.image.load("images/players/p1.png").convert()
Player5Image = pygame.transform.scale(Player1Image,(100,100))
#말판 이미지
mapImage = pygame.image.load("images/board/mapimage.png")
mapImage = pygame.transform.scale(mapImage,(height,height))
#레드팀 상태 UI
#screen.blit(Player1Image,(1110,800))
#Player1Image.set_colorkey(Black)
RedTeamUI = pygame.image.load("images/UI/RedTeamUI.png").convert()
RedTeamUI = pygame.transform.scale(RedTeamUI,(350,200))
#블루팀 상태 UI
BlueTeamUI = pygame.image.load("images/UI/BlueTeamUI.png").convert()
BlueTeamUI = pygame.transform.scale(BlueTeamUI,(350,200))
#그린팀 상태 UI
GreenTeamUI = pygame.image.load("images/UI/GreenTeamUI.png").convert()
GreenTeamUI = pygame.transform.scale(GreenTeamUI,(350,200))
#옐로팀 상태 UI
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

cards.CardShuffle(cards.cards)
blocks.MapSet(blocks.maps)

def Menu() :
    isRun = True
    type = 1
    while isRun :
        clock.tick(60)
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
                            if distance(RuleMenuBtn_pos[0],RuleMenuBtn_pos[1],NextPageBtn_Pos[0],NextPageBtn_Pos[1]) <= 25 :
                                RulePage += 1
                            if distance(RuleMenuBtn_pos[0],RuleMenuBtn_pos[1],BackPageBtn_Pos[0],BackPageBtn_Pos[1]) <= 25 :
                                if RulePage == 1 :
                                    RulePage = 1
                                else :
                                    RulePage -= 1
                            #if distance() <= :
                            #    isRunTwo = False
                            #    Type = 1
                    screen.fill((125,178,73))
                    match RulePage :
                        case 1:
                            screen.blit(GameRuleP1,(width/2-400,0))
                        case 2:
                            screen.blit(GameRuleP2,(width/2-400,0))
                    if RulePage == 1 :
                        screen.blit(GameRuleMenuNextPageBtn,NextPageBtn_spawnPos)
                        screen.blit
                    else :
                        screen.blit(GameRuleMenuNextPageBtn,NextPageBtn_spawnPos)
                        screen.blit(GameRuleMenuBackPageBtn,BackPageBtn_spawnPos)
                    pygame.display.update()
            #case 3:


Menu()

isChoose = True
PlayresNum = 1
while isChoose :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            PNBtnPos = pygame.mouse.get_pos()
            if PNBtnPos[0] >= width / 3 - 200 and PNBtnPos[0] <= width / 3 and PNBtnPos[1] >= 300 and PNBtnPos[1] <= 550 :
                PlayresNum = 2
                isChoose = False
            if PNBtnPos[0] >= width / 2 - 100 and PNBtnPos[0] <= width / 2 + 100 and PNBtnPos[1] >= 300 and PNBtnPos[1] <= 550 :
                PlayresNum = 3
                isChoose = False
            if PNBtnPos[0] >= width / 3 * 2 and PNBtnPos[0] <= width / 3 * 2 + 200 and PNBtnPos[1] >= 300 and PNBtnPos[1] <= 550 :
                PlayresNum = 4
                isChoose = False
    screen.fill(White)
    screen.blit(GameNumtext,(width / 2-400, 100))
    screen.blit(GameNumButton2,(width / 3 - 200, 300))
    screen.blit(GameNumButton3,(width / 2 - 100, 300))
    screen.blit(GameNumButton4,(width / 3 * 2, 300))
    pygame.display.update()
for i in range(PlayresNum) :
    players.players.append(players.Player())

dice = [0,0]
isRuleInfoBtnPushed = True
while 1 :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            btnClick_pos = pygame.mouse.get_pos()
            
    screen.fill((125,178,73))
    #게임오브젝트
    screen.blit(mapImage,(350,0))
    screen.blit(RollButton,(1300,410))
    #UI
    teamUIBlit()
    screen.blit(MyTurnMarker,TurnMarker_RedUIpos)
    pygame.display.update()