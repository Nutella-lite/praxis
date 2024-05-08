import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 36)  # Выбор шрифта и размера
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
screen.fill(color)

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/button.png")
TARGET_WIDTH, TARGET_HEIGHT = target_image.get_size()
target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

countdown = 60000
countup = 0

running = True
while running:
    countdown -= 1
    if countdown <= 0:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + TARGET_WIDTH and target_y <= mouse_y <= target_y + TARGET_HEIGHT:
                countup += 1
                color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
                target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)
    screen.fill(color)
    countdown_text = font.render(f"Осталось: {countdown} мс", True, (255, 255, 255))
    screen.blit(countdown_text, (285, 10))
    countup_text = font.render(f"Собрано: {countup} шансов из 40", True, (255, 255, 255))
    screen.blit(countup_text, (265, 570))
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()
