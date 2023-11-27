import pygame
import random

# 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("부루마블 게임")

# 색깔 정의
white = (255, 255, 255)
red = (255, 0, 0)

# 플레이어 위치
player_position = [40, 40]

# 주사위
dice_value = 1

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 주사위 굴리기
                dice_value = random.randint(1, 6)

    # 플레이어 이동
    player_position[0] += dice_value * 20

    # 화면 그리기
    screen.fill(white)
    pygame.draw.rect(screen, red, (player_position[0], player_position[1], 30, 30))

    # 주사위 값 표시
    font = pygame.font.Font(None, 36)
    text = font.render("주사위 값: {}".format(dice_value), True, red)
    screen.blit(text, (10, 10))

    pygame.display.flip()

# 게임 종료
pygame.quit()