import pygame, sys, random, math
from pygame.locals import *
#General Setting
pygame.display.set_caption("BlueMarble")
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
####################
#######Colors#######
####################
White = (255,255,255)
WoodBGColor = (235,178,126)
BackGroundColor = (125,178,73)
Black = (0,0,0)
DarkGray = (89,89,89)
####################
#######Images#######
####################
##Dice images##
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
####################
#######Classes######
####################
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
######        ######
