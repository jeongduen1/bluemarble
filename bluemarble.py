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
#block
class Block :
    def __init__(self) :
        self.type = 0
        self.price = 0
        self.pos = [0,0]
        self.owned = 0
        self.building = 0
blocks1 = [] #시작+7
blocks2 = [] #무인도+7
blocks3 = [] #올림픽+7
blocks4 = [] #세계 여행+7
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
def blockSet(arr1,arr2,arr3,arr4) :
    price = 100000
    type = 1
    y = 1
    PixelPos = [1005,1005]
    match y :
        case 1 : 
            arr1.append(Block())
            arr1[0].type = type
            arr1[0].pos = PixelPos
            PixelPos[0] -= 150
            PixelPos[1] += 55
            type += 1
            for i in range(3) :
                arr1.append(Block())
                arr1[i].type = 0
                arr1[i].price = price
                arr1[i].pos = PixelPos
                PixelPos[0] -= 110
                price += 10000
            arr1.append(Block())
            arr1[4].type = 5
            PixelPos[1] += 55
            arr1[4].pos = PixelPos
            PixelPos[0] -= 150
            PixelPos[1] -= 55
            for i in range(3) :
                arr1.append(Block())
                arr1[i].type = 0
                arr1[i].price = price
                arr1[i].pos = PixelPos
                PixelPos[0] -= 110
                price += 10000
        case 2 :
            arr2.append(Block())
            arr2[0].type = type
            type += 1
            for i in range(3) :
                arr2.append(Block())
                arr2[i].type = 0
                arr2[i].price = price
                price += 10000
            arr2.append(Block())
            arr2[4].type = 5
            for i in range(3) :
                arr2.append(Block())
                arr2[i].type = 0
                arr2[i].price = price
                price += 10000
        case 3 :
            arr3.append(Block())
            arr3[0].type = type
            type += 1
            for i in range(3) :
                arr3.append(Block())
                arr3[i].type = 0
                arr3[i].price = price
                price += 10000
            arr3.append(Block())
            arr3[4].type = 5
            for i in range(3) :
                arr3.append(Block())
                arr3[i].type = 0
                arr3[i].price = price
                price += 10000
        case 4 :
            arr4.append(Block())
            arr4[0].type = type
            type += 1
            for i in range(3) :
                arr4.append(Block())
                arr4[i].type = 0
                arr4[i].price = price
                price += 10000
            arr4.append(Block())
            arr4[4].type = 5
            for i in range(3) :
                arr4.append(Block())
                arr4[i].type = 0
                arr4[i].price = price
                price += 10000
def CheckBlockPos(pos) :
    if pos <= 7 :
        match pos :
            case 0 :
                return blocks1[0].pos
            case 1 :
                return blocks1[1].pos
            case 2 :
                return blocks1[2].pos
            case 3 :
                return blocks1[3].pos
            case 4 :
                return blocks1[4].pos
            case 5 :
                return blocks1[5].pos
            case 6 :
                return blocks1[6].pos
            case 7 :
                return blocks1[7].pos
    elif pos <= 15 :
        match pos :
            case 8 :
                return blocks2[0].pos
            case 9 :
                return blocks2[1].pos
            case 10 :
                return blocks2[2].pos
            case 11 :
                return blocks2[3].pos
            case 12 :
                return blocks2[4].pos
            case 13 :
                return blocks2[5].pos
            case 14 :
                return blocks2[6].pos
            case 15 :
                return blocks2[7].pos
    elif pos <= 23 :
        match pos :
            case 16 :
                return blocks3[0].pos
            case 17 :
                return blocks3[1].pos
            case 18 :
                return blocks3[2].pos
            case 19 :
                return blocks3[3].pos
            case 20 :
                return blocks3[4].pos
            case 21 :
                return blocks3[5].pos
            case 22 :
                return blocks3[6].pos
            case 23 :
                return blocks3[7].pos
    else :
        match pos :
            case 24 :
                return blocks4[0].pos
            case 25 :
                return blocks4[1].pos
            case 26 :
                return blocks4[2].pos
            case 27 :
                return blocks4[3].pos
            case 28 :
                return blocks4[4].pos
            case 29 :
                return blocks4[5].pos
            case 30 :
                return blocks4[6].pos
            case 31 :
                return blocks4[7].pos
def CheckBlockType(pos) :
    if pos <= 7 :
        match pos :
            case 0 :
                return blocks1[0].type
            case 1 :
                return blocks1[1].type
            case 2 :
                return blocks1[2].type
            case 3 :
                return blocks1[3].type
            case 4 :
                return blocks1[4].type
            case 5 :
                return blocks1[5].type
            case 6 :
                return blocks1[6].type
            case 7 :
                return blocks1[7].type
    elif pos <= 15 :
        match pos :
            case 8 :
                return blocks2[0].type
            case 9 :
                return blocks2[1].type
            case 10 :
                return blocks2[2].type
            case 11 :
                return blocks2[3].type
            case 12 :
                return blocks2[4].type
            case 13 :
                return blocks2[5].type
            case 14 :
                return blocks2[6].type
            case 15 :
                return blocks2[7].type
    elif pos <= 23 :
        match pos :
            case 16 :
                return blocks3[0].type
            case 17 :
                return blocks3[1].type
            case 18 :
                return blocks3[2].type
            case 19 :
                return blocks3[3].type
            case 20 :
                return blocks3[4].type
            case 21 :
                return blocks3[5].type
            case 22 :
                return blocks3[6].type
            case 23 :
                return blocks3[7].type
    else :
        match pos :
            case 24 :
                return blocks4[0].type
            case 25 :
                return blocks4[1].type
            case 26 :
                return blocks4[2].type
            case 27 :
                return blocks4[3].type
            case 28 :
                return blocks4[4].type
            case 29 :
                return blocks4[5].type
            case 30 :
                return blocks4[6].type
            case 31 :
                return blocks4[7].type
#Menu,GameRule,GameNumber,Game,EndGame / InGameMenu
#Dice images
dice_pos1 = (1750,850)
dice_pos2 = (1830,850)
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
DiceButton_pos = (1250,750)
DiceButton_Cpos = (1325,825)
#GameUI Images
GameUI2 = pygame.image.load("images/UI/FortuneUI2.png").convert()
GameUI3 = pygame.image.load("images/UI/FortuneUI3.png").convert()
GameUI4 = pygame.image.load("images/UI/FortuneUI4.png").convert()
#Map Image
mapImage = pygame.image.load("images/board/mapimage.png").convert()
mapImage_pos = (0,0)
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
    MenuCase6Working = True
    InGameMenuIsWorking = False
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
        case 3:
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
                                            Eventype = 1
                                        if isClickButton(InGameMenuExitButton_pos1,InGameMenuExitButton_pos2,Click_pos) :
                                            sys.exit()
                                screen.blit(InGameMenu,(0,0))
                                pygame.display.update()
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
                pygame.display.update()
        #Game
        case 4 :
            dice = [0,0]
            Turn = 1
            phase = 1
            blockSet(blocks1,blocks2,blocks3,blocks4)
            while MenuCase4Working :
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
                            case 2 :
                                match dice[0] :
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
                                match dice[1] :
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
                                            MenuCase4Working = False
                                            Eventype = 1
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
                        print('phase 2')
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
        case 5 :
            while MenuCase5Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()