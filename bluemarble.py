import pygame, sys, random, math
from pygame.locals import *
#General Setting
pygame.display.set_caption("BlueMarble")
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
#Colors
White = (255,255,255)
WoodBGColor = (235,178,126)
BackGroundColor = (125,178,73)
Black = (0,0,0)
DarkGray = (89,89,89)
#Classes
#player
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
            if self.pos[1] + 1 <= 4 :
                self.pos[1] += 1
            else :
                self.pos[1] = 0
players = []
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

#Menu,GameRule,GameNumber,Game,EndGame / InGameMenu
#Dice images
dice_pos1 = (1350,750)
dice_pos2 = (1500,750)
dice1 = pygame.image.load("images/UI/d1.png").convert()
dice1 = pygame.transform.scale(dice1,(150,150))
dice1.set_colorkey(DarkGray)

dice2 = pygame.image.load("images/UI/d2.png").convert()
dice2 = pygame.transform.scale(dice2,(150,150))
dice2.set_colorkey(DarkGray)

dice3 = pygame.image.load("images/UI/d3.png").convert()
dice3 = pygame.transform.scale(dice3,(150,150))
dice3.set_colorkey(DarkGray)

dice4 = pygame.image.load("images/UI/d4.png").convert()
dice4 = pygame.transform.scale(dice4,(150,150))
dice4.set_colorkey(DarkGray)

dice5 = pygame.image.load("images/UI/d5.png").convert()
dice5 = pygame.transform.scale(dice5,(150,150))
dice5.set_colorkey(DarkGray)

dice6 = pygame.image.load("images/UI/d6.png").convert()
dice6 = pygame.transform.scale(dice6,(150,150))
dice6.set_colorkey(DarkGray)
#InGameMenu Images
InGameMenu = pygame.image.load("images/UI/InGameMenu.png").convert()
InGameMenuContinueButton_pos1 = (642,354)
InGameMenuContinueButton_pos2 = (1279,520)
InGameMenuBackToMenuButton_pos1 = (642,540)
InGameMenuBackToMenuButton_pos2 = (1279,707)
InGameMenuExitButton_pos1 = (642,737)
InGameMenuExitButton_pos2 = (1279,888)
#Menu Images
GameMenuBoard = pygame.image.load("images/UI/GameMenu.png").convert()
GameMenuBoard_pos = (0,0)
MenuStartButton_pos1 = (882, 469)
MenuStartButton_pos2 = (1358, 581)
GameRuleButton_pos1 = (882, 612)
GameRuleButton_pos2 = (1358, 725)
MenuExitButton_pos1 = (882,746)
MenuExitButton_pos2 = (1358,871)
#GameRule Images
RuleNotePage1 = pygame.image.load("images/UI/RuleNotePage1.png").convert()
RuleNotePage2 = pygame.image.load("images/UI/RuleNotePage2.png").convert()
RuleNotePage3 = pygame.image.load("images/UI/RuleNotePage3.png").convert()
NextPageButton_Cpos1 = (1507-160,950-90)
NextPageButton_Cpos2 = (1830-160, 980-90)
BackPageButton_Cpos = (413-160, 980-90)
BacktoMenuButton_Cpos = (1640, 202)
#GameNumber
SelectGameNumber2 = pygame.image.load("images/UI/SelectGameNumber2.png").convert()
SelectGameNumber3 = pygame.image.load("images/UI/SelectGameNumber3.png").convert()
SelectGameNumber4 = pygame.image.load("images/UI/SelectGameNumber4.png").convert()
GameNumberMinusButton_pos1 = (34, 527)
GameNumberMinusButton_pos2 = (91, 584)
GameNumberPlusButton_pos1 = (588, 526)
GameNumberPlusButton_pos2 = (644, 582)
GameNumberCheckButton_Cpos = (622, 303)
GNInGameMenuButton_Cpos = (60,120)
#Game Images
GInGameMenuButton_Cpos = (1880, 40)
#TurnMaker
MTM = pygame.image.load("images/markers/MTM.png").convert()
MTM.set_colorkey((0,95,65))
MTM_Redpos = (1130,10)
MTM_Bluepos = (1130,295)
MTM_Greenpos = (1510,10)
MTM_Yellowpos = (1515,295)
#Dice Button Images
DiceButton = pygame.image.load("images/buttons/DiceButton.png").convert()
DiceButton = pygame.transform.scale(DiceButton,(200,200))
DiceButton_pos = (1400,750)
DiceButton_Cpos = (1500,850)
#GameUI Images
GameUI2 = pygame.image.load("images/UI/FortuneUI2.png").convert()
GameUI3 = pygame.image.load("images/UI/FortuneUI3.png").convert()
GameUI4 = pygame.image.load("images/UI/FortuneUI4.png").convert()
#buyPhase Images
buyPhaseMenu = pygame.image.load("images/UI/BuyPhase.png").convert()
GamePhaseMenu_pos = (163,163)
#Map Image
mapImage = pygame.image.load("images/board/mapimage.png").convert()
mapImage_pos = (0,0)

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
def printDice(arr):
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
def addTime(now,num) :
    if now + num <=60 :
        now += num
    else :
        num -= (60 - now)
        now += num
def reset() :
    print('reset')
#GameLoop
MenuWorking = True
eventType = 1
while MenuWorking :
    MenuCase1Working = True
    MenuCase2Working = True
    MenuCase3Working = True
    MenuCase5Working = True
    MenuCase6Working = True
    InGameMenuIsWorking = False
    match eventType :
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
                            eventType = 3 #->Game
                            print('Menu to SelectGameNumber')
                        #RuleButton
                        if isClickButton(GameRuleButton_pos1,GameRuleButton_pos2,Click_pos):
                            MenuCase1Working = False
                            eventType = 2 #->GameRule
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
                                    eventType = 1
                                    MenuCase2Working = False   
                screen.fill(WoodBGColor)   
                match page :
                    case 1:
                        screen.blit(RuleNotePage1,(160,90))
                    case 2:
                        screen.blit(RuleNotePage2,(160,90))
                    case 3:
                        screen.blit(RuleNotePage3,(160,90))
                pygame.display.update()
        #GameNumber
        case 3 :
            GameNumber = 2
            while MenuCase3Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
                        print(Click_pos)
                        if distance(GNInGameMenuButton_Cpos,Click_pos) <= 40 :
                            InGameMenuIsWorking = True
                            while InGameMenuIsWorking :
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                                        Click_pos = pygame.mouse.get_pos()
                                        print(Click_pos)
                                        if isClickButton(InGameMenuContinueButton_pos1,InGameMenuContinueButton_pos2,Click_pos) :
                                            InGameMenuIsWorking = False
                                        if isClickButton(InGameMenuBackToMenuButton_pos1,InGameMenuBackToMenuButton_pos2,Click_pos) :
                                            InGameMenuIsWorking = False
                                            MenuCase3Working = False
                                            eventType = 1
                                        if isClickButton(InGameMenuExitButton_pos1,InGameMenuExitButton_pos2,Click_pos) :
                                            sys.exit()
                                screen.blit(InGameMenu,(0,0))
                                pygame.display.update()
                        match GameNumber :
                            case 2 :
                                if isClickButton(GameNumberPlusButton_pos1,GameNumberPlusButton_pos2,Click_pos) :
                                    GameNumber += 1
                                if distance(GameNumberCheckButton_Cpos,Click_pos) < 20 :
                                    eventType = 4
                                    MenuCase3Working = False
                            case 3 :
                                if isClickButton(GameNumberPlusButton_pos1,GameNumberPlusButton_pos2,Click_pos) :
                                    GameNumber += 1
                                if isClickButton(GameNumberMinusButton_pos1,GameNumberMinusButton_pos2,Click_pos) :
                                    GameNumber -= 1
                                if distance(GameNumberCheckButton_Cpos,Click_pos) < 20 :
                                    eventType = 4
                                    MenuCase3Working = False
                            case 4 :
                                if isClickButton(GameNumberMinusButton_pos1,GameNumberMinusButton_pos2,Click_pos) :
                                    GameNumber -= 1
                                if distance(GameNumberCheckButton_Cpos,Click_pos) < 20 :
                                    eventType = 4
                                    MenuCase3Working = False
                match GameNumber :
                    case 2 :
                        screen.blit(SelectGameNumber2,(0,0))
                    case 3 :
                        screen.blit(SelectGameNumber3,(0,0))
                    case 4 :
                        screen.blit(SelectGameNumber4,(0,0))
                pygame.display.update()
        #Load
        case 4 :
            ######PlayerSet#####
            SetPlayers(players,GameNumber)
            ####################
            #y = 0 - 시작+7
            #y = 1 - 무인도+7
            #y = 2 - 올림픽+7
            #y = 3 - 세계 여행+7
            ######BlockSet######
            rows = 8
            cols = 4
            blocks = [[ Block() for j in range(cols)] for i in range(rows)]
            price = 100000
            blocktype = 1
            x = 0
            y = 0
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
            ####################
            dice = [0,0]
            Turn = 1
            phase = 1
            eventType = 5
        #Game
        case 5 :
            while MenuCase5Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
                        print(Click_pos)
                        match phase :
                            case 1 :
                                if distance(DiceButton_Cpos,Click_pos) <= 75:
                                    dice[0] = random.randint(1,6)
                                    dice[1] = random.randint(1,6)
                                    phase = 2
                        if distance(GInGameMenuButton_Cpos,Click_pos) <= 40 :
                            InGameMenuIsWorking = True
                            #인게임메뉴
                            while InGameMenuIsWorking :
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                                        Click_pos = pygame.mouse.get_pos()
                                        print(Click_pos)
                                        if isClickButton(InGameMenuContinueButton_pos1,InGameMenuContinueButton_pos2,Click_pos) :
                                            InGameMenuIsWorking = False
                                        if isClickButton(InGameMenuBackToMenuButton_pos1,InGameMenuBackToMenuButton_pos2,Click_pos) :
                                            InGameMenuIsWorking = False
                                            MenuCase5Working = False
                                            eventType = 1
                                        if isClickButton(InGameMenuExitButton_pos1,InGameMenuExitButton_pos2,Click_pos) :
                                            sys.exit()
                                screen.blit(InGameMenu,(0,0))
                                pygame.display.update()
                
                screen.fill(BackGroundColor)
                screen.blit(mapImage,mapImage_pos)
                match GameNumber :
                    case 2 :
                        screen.blit(GameUI2,(1080,0))
                    case 3 :
                        screen.blit(GameUI3,(1080,0))
                    case 4 :
                        screen.blit(GameUI4,(1080,0))
                match Turn :
                    case 1 :
                        screen.blit(MTM,MTM_Redpos)
                    case 2 :
                        screen.blit(MTM,MTM_Bluepos)
                    case 3 :
                        screen.blit(MTM,MTM_Greenpos)
                    case 4 :
                        screen.blit(MTM,MTM_Yellowpos)
                match phase :
                    case 1 :
                        screen.blit(DiceButton,DiceButton_pos)
                    case 2 :
                        printDice(dice)
                        screen.blit(buyPhaseMenu,GamePhaseMenu_pos)
                    #if click it
                    #dice roll
                    #player move
                
                #1-2.buying phase
                #check block type
                #match case.2(block type)
                #2-1.normal block
                #if it belong to someone
                #pay tall who have that normal block
                #player can take over the block
                #else if nobody has that
                #player can buy the block or not
                #build structure on the block
                #
                #
                #1-3
                #turn + 1
                #if turn < gamenumber
                #turn = 1
                #if win condition == true
                #close game
                #wvwnt type = 5
                pygame.display.update()
        #EndGame
        case 6 :
            while MenuCase6Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
                MenuWorking = False