import pygame, sys, random, math
from pygame.locals import *

#General Setting
pygame.display.set_caption("BlueMarble")
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
#Colors
White = (255,255,255)
BackGroundColor = (125,178,73)
Black = (0,0,0)
#Classes
#player
class Player :
    def __init__(self) :
        self.fortune = 500000
        self.ownedLands = []
        self.items = []
        self.pos = [0,0]
#block
class Block :
    def __init__(self) :
        self.type = 0
        self.price = 0
        self.pos = [0]
        self.owned = 0
        self.building = 0
#Defines
def SetPlayers(arr,num) :
    for i in range(num) :
        arr.append(Player())
def distance(pos1,pos2):
    result = math.sqrt( math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))
    return result
def isClickButton(BtnPos1,BtnPos2,ClickPos) :
    if BtnPos1[0] <= ClickPos[0] <= BtnPos2[0] and BtnPos1[1] <= ClickPos[1] <= BtnPos2[1] :
        return True
    else :
        return False
def blockSet(arr) :
    x = 0
    y = 0
    type = 1
    arr[x,y].append(Block())
    arr[x,y].type = type
    
def teamUIBlit(num) :
    pygame.draw.rect(screen,Black,[])
    match num :
        case 2:
            screen.blit(RedTeamUI,(910,10))
            screen.blit(BlueTeamUI,(910,220))
            screen.blit(TurnMarker,TurnMarker_RedUIpos)
            screen.blit(TurnMarker,TurnMarker_BlueUIpos)
        case 3:
            screen.blit(RedTeamUI,(910,10))
            screen.blit(BlueTeamUI,(910,220))
            screen.blit(GreenTeamUI,(910,430))
            screen.blit(TurnMarker,TurnMarker_RedUIpos)
            screen.blit(TurnMarker,TurnMarker_BlueUIpos)
            screen.blit(TurnMarker,TurnMarker_GreenUIpos)
        case 4:
            screen.blit(RedTeamUI,(910,10))
            screen.blit(BlueTeamUI,(910,220))
            screen.blit(GreenTeamUI,(910,430))
            screen.blit(YellowTeamUI,(910,640))
            screen.blit(TurnMarker,TurnMarker_RedUIpos)
            screen.blit(TurnMarker,TurnMarker_BlueUIpos)
            screen.blit(TurnMarker,TurnMarker_GreenUIpos)
            screen.blit(TurnMarker,TurnMarker_YellowUIpos)

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
#Menu,GameRule,GameNumber,Game,EndGame
#Menu Images
GameMenuBoard = pygame.image.load("images/UI/GameMenu.png").convert()
GameMenuBoard_pos = (0,0)
MenuStartButton_pos1 = (562, 289)
MenuStartButton_pos2 = (1038, 401)
GameRuleButton_pos1 = (562, 432)
GameRuleButton_pos2 = (1038, 545)
MenuExitButton_pos1 = (562,566)
MenuExitButton_pos2 = (1038,691)
#GameRule Images
RuleNotePage1 = pygame.image.load("images/UI/RuleNotePage1.png").convert()
RuleNotePage2 = pygame.image.load("images/UI/RuleNotePage2.png").convert()
RuleNotePage3 = pygame.image.load("images/UI/RuleNotePage3.png").convert()
NextPageButton_Cpos1 = (1187,770)
NextPageButton_Cpos2 = (1510, 800)
BackPageButton_Cpos = (93, 800)
BacktoMenuButton_Cpos = (1486, 113)
#GameNumber
GameNumbertoMenuButton = pygame.image.load("images/buttons/GameNumbertoMenuButton.png").convert()
GameNumbertoMenuButton = pygame.transform.scale(GameNumbertoMenuButton,(75,75))
GameNumbertoMenuButton.set_colorkey(White)
GameNumbertoMenuButton_pos1 = (1485,50)
GameNumbertoMenuButton_pos2 = (1585,150)
SelectGameNumber2 = pygame.image.load("images/UI/SelectGameNumber2.png").convert()
SelectGameNumber3 = pygame.image.load("images/UI/SelectGameNumber3.png").convert()
SelectGameNumber4 = pygame.image.load("images/UI/SelectGameNumber4.png").convert()
GameNumberMinusButton_pos1 = (28, 440)
GameNumberMinusButton_pos2 = (74, 485)
GameNumberPlusButton_pos1 = (489, 438)
GameNumberPlusButton_pos2 = (535, 483)
GameNumberCheckButton_Cpos = (521, 243)
#Game Images
#Map Image
mapImage = pygame.image.load("images/board/mapimage.png").convert()
mapImage = pygame.transform.scale(mapImage,(900,900))
mapImage_pos = (0,0)
#redteam UI
RedTeamTurnText = pygame.image.load("images/UI/RedTeamTurnText.png").convert()
RedTeamTurnText.set_colorkey(White)
RedTeamUI = pygame.image.load("images/UI/RedTeamUI.png").convert()
RedTeamUI = pygame.transform.scale(RedTeamUI,(350,200))
#blueteam UI
BlueTeamTurnText = pygame.image.load("images/UI/BlueTeamTurnText.png").convert()
BlueTeamTurnText.set_colorkey(White)
BlueTeamUI = pygame.image.load("images/UI/BlueTeamUI.png").convert()
BlueTeamUI = pygame.transform.scale(BlueTeamUI,(350,200))
#greenteam UI
GreenTeamTurnText = pygame.image.load("images/UI/GreenTeamTurnText.png").convert()
GreenTeamTurnText.set_colorkey(White)
GreenTeamUI = pygame.image.load("images/UI/GreenTeamUI.png").convert()
GreenTeamUI = pygame.transform.scale(GreenTeamUI,(350,200))
#yellowteam UI
YellowTeamTurnText = pygame.image.load("images/UI/YellowTeamTurnText.png").convert()
YellowTeamTurnText.set_colorkey(White)
YellowTeamUI = pygame.image.load("images/UI/YellowTeamUI.png").convert()
YellowTeamUI = pygame.transform.scale(YellowTeamUI,(350,200))
#TurnMarker
TurnMarker = pygame.image.load("images/markers/TurnMarker.png").convert()
TurnMarker = pygame.transform.scale(TurnMarker,(65,65))
MyTurnMarker = pygame.image.load("images/markers/MyTurnMarker.png").convert()
MyTurnMarker = pygame.transform.scale(MyTurnMarker,(65,65))
TurnMarker_RedUIpos = (73,15)
TurnMarker_BlueUIpos = (73,225)
TurnMarker_GreenUIpos = (73,435)
TurnMarker_YellowUIpos = (73,645)
p1 = pygame.image.load("images/players/p1.png").convert()
p1 = pygame.transform.scale(p1,(75,75))
p1.set_colorkey(Black)
#GameLoop
MenuWorking = True
Eventype = 1
while MenuWorking :
    MenuCase1Working = True
    MenuCase2Working = True
    MenuCase3Working = True
    MenuCase4Working = True
    MenuCase5Working = True
    match Eventype :
        #Menu
        case 1:
            while MenuCase1Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
                        print(Click_pos)
                        #StartButton
                        if isClickButton(MenuStartButton_pos1,MenuStartButton_pos2,Click_pos):
                            MenuCase1Working = False
                            Eventype = 3 #->Game
                            print('Menu to SelectGameNumber')
                        #RuleButton
                        if isClickButton(GameRuleButton_pos1,GameRuleButton_pos2,Click_pos):
                            MenuCase1Working = False
                            Eventype = 2 #->GameRule
                            print('Menu to GameRule')
                        #GameExitButton
                        if isClickButton(MenuExitButton_pos1,MenuExitButton_pos2,Click_pos):
                            sys.exit() #-> GameExit
                screen.blit(GameMenuBoard,GameMenuBoard_pos)
                pygame.display.update()
        #GameRule
        case 2 :
            page = 1
            while MenuCase2Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
                        print(Click_pos)
                        match page :
                            case 1 :
                                if distance(NextPageButton_Cpos1,Click_pos) <= 40 :
                                    page += 1
                            case 2 :
                                if distance(NextPageButton_Cpos2,Click_pos) <= 40 :
                                    page += 1
                            case 3 :
                                if distance(BackPageButton_Cpos,Click_pos) <= 40 :
                                    page -= 1
                                if distance(BacktoMenuButton_Cpos,Click_pos) <= 30:
                                    Eventype = 1
                                    MenuCase2Working = False      
                match page :
                    case 1:
                        screen.blit(RuleNotePage1,(0,0))
                    case 2:
                        screen.blit(RuleNotePage2,(0,0))
                    case 3:
                        screen.blit(RuleNotePage3,(0,0))
                pygame.display.update()
        #GameNumber
        case 3:
            GameNumber = 2
            while MenuCase3Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
                        print(Click_pos)
                        if isClickButton(GameNumbertoMenuButton_pos1,GameNumbertoMenuButton_pos2,Click_pos) :
                                    Eventype = 1
                                    MenuCase3Working = False
                        match GameNumber :
                            case 2 :
                                if isClickButton(GameNumberPlusButton_pos1,GameNumberPlusButton_pos2,Click_pos) :
                                    GameNumber += 1
                                if distance(GameNumberCheckButton_Cpos,Click_pos) < 20 :
                                    Eventype = 4
                                    MenuCase3Working = False
                            case 3 :
                                if isClickButton(GameNumberPlusButton_pos1,GameNumberPlusButton_pos2,Click_pos) :
                                    GameNumber += 1
                                if isClickButton(GameNumberMinusButton_pos1,GameNumberMinusButton_pos2,Click_pos) :
                                    GameNumber -= 1
                                if distance(GameNumberCheckButton_Cpos,Click_pos) < 20 :
                                    Eventype = 4
                                    MenuCase3Working = False
                            case 4 :
                                if isClickButton(GameNumberMinusButton_pos1,GameNumberMinusButton_pos2,Click_pos) :
                                    GameNumber -= 1
                                if distance(GameNumberCheckButton_Cpos,Click_pos) < 20 :
                                    Eventype = 4
                                    MenuCase3Working = False
                match GameNumber :
                    case 2 :
                        screen.blit(SelectGameNumber2,(0,0))
                    case 3 :
                        screen.blit(SelectGameNumber3,(0,0))
                    case 4 :
                        screen.blit(SelectGameNumber4,(0,0))
                screen.blit(GameNumbertoMenuButton,GameNumbertoMenuButton_pos1)
                pygame.display.update()
        #Game
        case 4 :
            Turn = 1
            while MenuCase4Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                for i in range(GameNumber) :
                    screen.fill(BackGroundColor)
                    screen.blit(mapImage,mapImage_pos)
                    teamUIBlit(GameNumber)
                    MyTurnMakerDraw(Turn)
                    screen.blit(p1,(1150,800))
                    pygame.display.update()
        #EndGame
        case 5 :
            while MenuCase5Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()