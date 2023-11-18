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
Black = (0,0,0)
#Classes

class Player :
    def __init__(self) :
        self.fortune = 0
        self.ownedLands = []
        self.items = []
        self.pos = [0,0]

#Defines
def distance(pos1,pos2):
    result = math.sqrt( math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))
    return result
def isClickButton(BtnPos1,BtnPos2,ClickPos) :
    if BtnPos1[0] <= ClickPos[0] <= BtnPos2[0] and BtnPos1[1] <= ClickPos[1] <= BtnPos2[1] :
        return True
    else :
        return False
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
#Menu,GameRule,Game,EndGame
#Menu Images
GameMenuBoard = pygame.image.load("images/UI/GameMenu.png").convert()
GameMenuBoard_pos = (0,0)
MenuStartButton = pygame.image.load("images/buttons/StartButton.png").convert()
MenuStartButton = pygame.transform.scale(MenuStartButton,(400,150))
MenuStartButton.set_colorkey(White)
MenuStartButton_pos1 = (500, 347)
MenuStartButton_pos2 = (1100, 466)
GameRuleButton = pygame.image.load("images/buttons/GameRuleButton.png").convert()
GameRuleButton = pygame.transform.scale(GameRuleButton,(400,150))
GameRuleButton_pos1 = (500,468)
GameRuleButton_pos2 = (1100,586)
MenuExitButton = pygame.image.load("images/buttons/MenuExit.png").convert()
MenuExitButton = pygame.transform.scale(MenuExitButton,(400,150))
MenuExitButton_pos1 = (500,588)
MenuExitButton_pos2 = (1100,707)
#GameRule Images
RuleNotePage1 = pygame.image.load("images/UI/RuleNotePage1.png").convert()
RuleNotePage2 = pygame.image.load("images/UI/RuleNotePage2.png").convert() 
RuleNotePage3 = pygame.image.load("images/UI/RuleNotePage3.png").convert()
RuleNotePage4 = pygame.image.load("images/UI/RuleNotePage4.png").convert()
NextPageButton = pygame.image.load("images/buttons/NextPageButton.png").convert()
NextPageButton = pygame.transform.scale(NextPageButton,(80,80))
NextPageButton.set_colorkey(White)
NextPageButton_pos1 = (1150,height/2 - 40)
NextPageButton_Cpos1 = (1190,height/2)
NextPageButton_pos2 = (1350,height/2 - 40)
NextPageButton_Cpos2 = (1390,height/2)
BackMenuButton_pos1 = (525, 365)
BackMenuButton_pos2 = (1074, 468)
BackPage1Button_pos1 = (525, 498)
BackPage1Button_pos2 = (1073, 599)

#GameLoop
MenuWorking = True
Eventype = 1
while MenuWorking :
    MenuCase1Working = True
    MenuCase2Working = True
    MenuCase3Working = True
    MenuCase4Working = True
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
                        #RuleButton
                        if isClickButton(GameRuleButton_pos1,GameRuleButton_pos2,Click_pos):
                            MenuCase1Working = False
                            Eventype = 2 #->GameRule
                            print('Menu to GameRule')
                        #StartButton
                        if isClickButton(MenuStartButton_pos1,MenuStartButton_pos2,Click_pos):
                            MenuCase1Working = False
                            Eventype = 3 #->Game
                            print('Menu to Game')
                        #GameExitButton
                        if isClickButton(MenuExitButton_pos1,MenuExitButton_pos2,Click_pos):
                            sys.exit() #-> GameExit
                screen.fill(White)
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
                                if distance(NextPageButton_Cpos2,Click_pos) <= 40 :
                                    page += 1
                            case 4 :
                                if isClickButton(BackPage1Button_pos1,BackPage1Button_pos2,Click_pos):
                                    page = 1
                                if isClickButton(BackMenuButton_pos1,BackMenuButton_pos2,Click_pos) :
                                    Eventype = 1
                                    MenuCase2Working = False
                match page :
                    case 1:
                        screen.blit(RuleNotePage1,(0,0))
                        screen.blit(NextPageButton,NextPageButton_pos1)
                    case 2:
                        screen.blit(RuleNotePage2,(0,0))
                        screen.blit(NextPageButton,NextPageButton_pos2)
                    case 3:
                        screen.blit(RuleNotePage3,(0,0))
                        screen.blit(NextPageButton,NextPageButton_pos2)
                    case 4:
                        screen.blit(RuleNotePage4,(0,0))
                pygame.display.update()
        #Game
        case 3 :
            while MenuCase3Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                screen.fill(White)
                pygame.display.update()
        #EndGame
        case 4 :
            while MenuCase4Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
