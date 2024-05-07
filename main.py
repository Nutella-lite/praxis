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
target_width, target_height = 300, 65
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)


running = True
while running:
    screen.fill(color)
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()
    pass


pygame.quit()
