import pygame, sys, random, math
from pygame.locals import *
###GeneralSetting###
pygame.display.set_caption("BlueMarble")
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
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
#buyPhaseMenu
buyPhaseMenu = pygame.image.load("images/4.GameImages/UI/BuyPhase.png").convert()
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
#BuyPhaseMenu
gamePhaseMenu_pos = (163,163)
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
        case 1 :
            screen.blit(myTurnMarker,myTurnMarker_Redpos)
        case 2 :
            screen.blit(myTurnMarker,myTurnMarker_Bluepos)
        case 3 :
            screen.blit(myTurnMarker,myTurnMarker_Greenpos)
        case 4 :
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
gameNumber = 2
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
                        Click_pos = pygame.mouse.get_pos()
                        print(Click_pos)
                        #StartButton
                        if clickButton(menuStartButton_pos1,menuStartButton_pos2,Click_pos):
                            isMenuRunning = False
                            fromInGameMenu = True
                            event_type = 3 #->GameNumber
                            print('Menu to SelectGameNumber')
                        #RuleButton
                        if clickButton(gameRuleButton_pos1,gameRuleButton_pos2,Click_pos):
                            isMenuRunning = False
                            event_type = 2 #->GameRule
                            print('Menu to GameRule')
                        #GameExitButton
                        if clickButton(menuExitButton_pos1,menuExitButton_pos2,Click_pos):
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
                        Click_pos = pygame.mouse.get_pos()
                        print(Click_pos)
                        match page :
                            case 1 :
                                if distance(nextPageButton_Cpos1,Click_pos) <= 40 :
                                    page += 1
                            case 2 :
                                if distance(nextPageButton_Cpos2,Click_pos) <= 40 :
                                    page += 1
                            case 3 :
                                if distance(backPageButton_Cpos,Click_pos) <= 40 :
                                    page -= 1
                                if distance(backtoMenuButton_Cpos,Click_pos) <= 30:
                                    event_type = 1
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
            while isGameNumberRunning :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
                        print(Click_pos)
                        if distance(gameNumberInGameMenuButton_Cpos,Click_pos) <= 40 :
                            event_type = 6
                            mevent_type = 3
                            isGameNumberRunning = False
                            isInGameMenuRunning = True
                        match gameNumber :
                            case 2 :
                                if clickButton(gameNumberPlusButton_pos1,gameNumberPlusButton_pos2,Click_pos) :
                                    gameNumber += 1
                            case 3 :
                                if clickButton(gameNumberPlusButton_pos1,gameNumberPlusButton_pos2,Click_pos) :
                                    gameNumber += 1
                                if clickButton(gameNumberMinusButton_pos1,gameNumberMinusButton_pos2,Click_pos) :
                                    gameNumber -= 1
                            case 4 :
                                if clickButton(gameNumberMinusButton_pos1,gameNumberMinusButton_pos2,Click_pos) :
                                    gameNumber -= 1
                        if distance(gameNumberCheckButton_Cpos,Click_pos) < 20 :
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
                isDiceRolled = False
                phase = 1
                turn = 1
                players.clear()
                setPlayers(players,gameNumber)
                dice = [0,0]
            while isGameRunning :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
                        print(Click_pos)
                        if distance(gameInGameMenuButton_Cpos,Click_pos) <= 40 :
                            event_type = 6
                            mevent_type = 4
                            isGameRunning = False
                            isInGameMenuRunning = True
                        match phase :
                            case 1 :
                                if distance(diceButton_Cpos,Click_pos) <= 100:
                                    dice[0] = random.randint(1,6)
                                    dice[1] = random.randint(1,6)
                                    print('before :',players[turn].pos)
                                    players[turn].move(dice[0]+dice[1])
                                    print('after :',players[turn].pos)
                                    isDiceRolled = True
                                    phase = 2
                screen.blit(mapBoard,mapBoard_pos)
                drawGameUI(gameNumber)
                drawTurnMarker(turn)
                if isDiceRolled :
                    drawDice(dice)
                match phase :
                    case 1 :
                        screen.blit(diceButton,diceButton_pos)
                    case 2 :
                        screen.blit(buyPhaseMenu,gamePhaseMenu_pos)
                pygame.display.update()
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
                        Click_pos = pygame.mouse.get_pos()
                        print(Click_pos)
                        if clickButton(inGameMenuContinueButton_pos1,inGameMenuContinueButton_pos2,Click_pos) :
                            isInGameMenuRunning = False
                            fromInGameMenu = False
                            event_type = mevent_type
                        if clickButton(inGameMenuBackToMenuButton_pos1,inGameMenuBackToMenuButton_pos2,Click_pos) :
                            isInGameMenuRunning = False
                            event_type = 1
                        if clickButton(inGameMenuExitButton_pos1,inGameMenuExitButton_pos2,Click_pos) :
                            sys.exit()
                screen.blit(inGameMenu,(0,0))
                pygame.display.update()
########Logic#######