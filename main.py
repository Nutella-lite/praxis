import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/button.png")
TARGET_WIDTH, TARGET_HEIGHT = target_image.get_size()
target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(color)
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()
    pass


pygame.quit()
