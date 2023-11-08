import pygame, sys, random, define
from pygame.locals import *
pygame.init()
width = 1600
heigth = 900
pygame.display.set_caption("BlueMarble")
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()

StartButton = pygame.image.load("images/StartButton.png").convert()
StartButton = pygame.transform.scale(StartButton,(600,240))

define.CardShuffle(define.cards)
define.MapSet(define.maps)

while 1 :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255,255,255))
    screen.blit(StartButton,(width / 2 - 300, heigth / 2 - 130))
    
    pygame.display.update()