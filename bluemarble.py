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

#Defines
def distance(pos1,pos2):
    result = math.sqrt( math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))
    return result
def isClickButton(BtnPos1,BtnPos2,ClickPos) :
    if BtnPos1[0] <= ClickPos[0] <= BtnPos2[0] and BtnPos1[1] <= ClickPos[1] <= BtnPos2[1] :
        return True
    else :
        return False

#Menu,GameRule,Game,EndGame
#Menu Images
GameMenuBoard = pygame.image.load("images/UI/GameMenu.png").convert()
GameMenuBoard_pos = (0,0)
MenuStartButton = pygame.image.load("images/buttons/StartButton.png").convert()
MenuStartButton = pygame.transform.scale(MenuStartButton,(400,150))
MenuStartButton.set_colorkey(White)
MenuStartButton_pos1 = (width/2-200,height/2-150)
MenuStartButton_pos2 = (width/2+200,height/2)
GameRuleButton = pygame.image.load("images/buttons/GameRuleButton.png").convert()
GameRuleButton = pygame.transform.scale(GameRuleButton,(400,150))
GameRuleButton_pos1 = (width/2-200,height/2+25)
GameRuleButton_pos2 = (width/2+200,height/2+175)
MenuExitButton = pygame.image.load("images/buttons/MenuExit.png").convert()
MenuExitButton = pygame.transform.scale(MenuExitButton,(400,150))
MenuExitButton_pos1 = (width/2-200,height/2+200)
MenuExitButton_pos2 = (width/2+200,height/2+350)
#GameRule Images
RuleNotePage1 = pygame.image.load("images/UI/RuleNotePage1.png").convert()
RuleNotePage2 = pygame.image.load("images/UI/RuleNotePage2.png").convert() 
RuleNotePage3 = pygame.image.load("images/UI/RuleNotePage3.png").convert()
RuleNotePage3 = pygame.image.load("images/UI/RuleNotePage4.png").convert() 
#GameLoop
MenuWorking = True
MenuEventType = 1
while MenuWorking :
    MenuCase1Working = True
    MenuCase2Working = True
    MenuCase3Working = True
    MenuCase4Working = True
    match MenuEventType :
        #Menu
        case 1:
            while MenuCase1Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
                        #RuleButton
                        if isClickButton(GameRuleButton_pos1,GameRuleButton_pos2,Click_pos):
                            MenuCase1Working = False
                            MenuEventType = 2 #->GameRule
                            print('Menu to GameRule')
                        #StartButton
                        if isClickButton(MenuStartButton_pos1,MenuStartButton_pos2,Click_pos):
                            MenuCase1Working = False
                            MenuEventType = 3 #->Game
                            print('Menu to Game')
                        if isClickButton(MenuExitButton_pos1,MenuExitButton_pos2,Click_pos):
                            sys.exit()
                screen.fill(White)
                screen.blit(GameMenuBoard,GameMenuBoard_pos)
                screen.blit(MenuStartButton,MenuStartButton_pos1)
                screen.blit(GameRuleButton,GameRuleButton_pos1)
                screen.blit(MenuExitButton,MenuExitButton_pos1)
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
                
                screen.fill(Black)
                match page :
                    case 1:
                        screen.blit(RuleNotePage1,(0,0))
                    case 2:
                        screen.blit(RuleNotePage2,(0,0))
                    case 3:
                        screen.blit(RuleNotePage3,(0,0))
                    case 4:
                        screen.blit(RuleNotePage4,(0,0))
                pygame.display.update()
        #Game
        case 3 :
            while MenuCase3Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                screen.fill(while)
                pygame.display.update()
        #EndGame
        case 4 :
            while MenuCase4Working :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        Click_pos = pygame.mouse.get_pos()
