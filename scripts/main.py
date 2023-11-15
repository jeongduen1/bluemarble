import pygame, sys, random, players, blocks, cards, systems
from pygame.locals import *
pygame.init()
width = 1600
heigth = 900
pygame.display.set_caption("BlueMarble")
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()

def roll(arr) :
    arr[0] = random.randint(1,6)
    arr[1] = random.randint(1,6)

White = (255,255,255)
Black = (0,0,0)

#시작 버튼
StartButton = pygame.image.load("images/StartButton.png").convert()
StartButton = pygame.transform.scale(StartButton,(600,240))
#게임 인원수 선택 버튼
GameNumButton2 = pygame.image.load("images/Two.png").convert()
GameNumButton2 = pygame.transform.scale(GameNumButton2,(200,250))
GameNumButton3 = pygame.image.load("images/Three.png").convert()
GameNumButton3 = pygame.transform.scale(GameNumButton3,(200,250))
GameNumButton4 = pygame.image.load("images/Four.png").convert()
GameNumButton4 = pygame.transform.scale(GameNumButton4,(200,250))
#게임 인원수 선택 텍스트
GameNumfont = pygame.font.Font("fonts/CookieRun Regular.ttf", 30)
GameNumtext = GameNumfont.render("플레이할 인원수를 선택하세요.", False, Black)
GameNumtext = pygame.transform.scale(GameNumtext,(800,100))
#플레이어 이미지
Player1Image = pygame.image.load("images/p1.png").convert()
#말판 이미지
mapImage = pygame.image.load("images/mapimage.png").convert()
mapImage = pygame.transform.scale(mapImage,(heigth,heigth))
#레드팀 상태 UI
RedTeamUI = pygame.image.load("images/RedPlayerUI.png").convert()
RedTeamUI = pygame.transform.scale(RedTeamUI,(350,200))


cards.CardShuffle(cards.cards)
blocks.MapSet(blocks.maps)

isStartDown = True
while isStartDown :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            stbtn_pos = pygame.mouse.get_pos()
            if stbtn_pos[0] >= width / 2 - 300 and stbtn_pos[0] <= width / 2 + 300 and stbtn_pos[1] >= heigth / 2 - 130 and stbtn_pos[1] <= heigth / 2 + 130 :
                isStartDown = False

    screen.fill(White)
    screen.blit(StartButton,(width / 2 - 300, heigth / 2 - 130))
    pygame.display.update()

isChoose = True
PlayresNum = 1
while isChoose :
    clock.tick(60)
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
while 1 :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((125,178,73))
    screen.blit(mapImage,(350,0))
    screen.blit(RedTeamUI,(0,0))
    #screen.blit(noticeTurntext,(width/2,heigth/2))
    pygame.display.update()