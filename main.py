import pygame, sys, random, players, blocks, cards, systems
from pygame.locals import *
pygame.init()
width = 1600
heigth = 900
pygame.display.set_caption("BlueMarble")
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()

White = (255,255,255)
Black = (0,0,0)

StartButton = pygame.image.load("images/StartButton.png").convert()
StartButton = pygame.transform.scale(StartButton,(600,240))
GameNumButton2 = pygame.image.load("images/Two.png").convert()
GameNumButton2 = pygame.transform.scale(GameNumButton2,(200,250))
GameNumButton3 = pygame.image.load("images/Three.png").convert()
GameNumButton3 = pygame.transform.scale(GameNumButton3,(200,250))
GameNumButton4 = pygame.image.load("images/Four.png").convert()
GameNumButton4 = pygame.transform.scale(GameNumButton4,(200,250))

GameNumfont = pygame.font.Font("fonts/CookieRun Regular.ttf", 30)
GameNumtext = GameNumfont.render("플레이할 인원수를 선택하세요.", False, Black)
GameNumtext = pygame.transform.scale(GameNumtext,(800,100))

cards.CardShuffle(cards.cards)
blocks.MapSet(blocks.maps)

isStart = True
while isStart :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            stbtn_pos = pygame.mouse.get_pos()
            print(stbtn_pos)
            if stbtn_pos[0] >= width / 2 - 300 and stbtn_pos[0] <= width / 2 + 300 and stbtn_pos[1] >= heigth / 2 - 130 and stbtn_pos[1] <= heigth / 2 + 130 :
                isStart = False

    screen.fill(White)
    screen.blit(StartButton,(width / 2 - 300, heigth / 2 - 130))
    pygame.display.update()

while 1 :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(White)
    screen.blit(GameNumtext,(width / 2-400, 100))
    screen.blit(GameNumButton2,(width / 3 - 200, 300))
    screen.blit(GameNumButton3,(width / 2 - 100, 300))
    screen.blit(GameNumButton4,(width / 3 * 2, 300))
    pygame.display.update()