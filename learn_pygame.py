import pygame
import random
import math

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 36)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
screen.fill(color)

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/button.png")
TARGET_WIDTH, TARGET_HEIGHT = target_image.get_size()
target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

def draw_fireworks(x, y, num_particles, colors):
    for _ in range(num_particles):
        color = random.choice(colors)
        radius = random.randint(50, SCREEN_HEIGHT // 2)
        angle = random.random() * 2 * math.pi
        dx = int(radius * math.cos(angle))
        dy = int(radius * math.sin(angle))
        pygame.draw.line(screen, color, (x, y), (x + dx, y + dy), 3)
        num_dots = random.randint(5, 15)
        for _ in range(num_dots):
            dot_x = x + dx + random.randint(-50, 50)
            dot_y = y + dy + random.randint(-50, 50)
            dot_radius = random.randint(1, 6)
            dot_color = random.choice(colors)
            pygame.draw.circle(screen, dot_color, (dot_x, dot_y), dot_radius)


COUNTDOWN = 60000
countdown, countup, UP = COUNTDOWN, 0, int(COUNTDOWN // 1200)
running = True

while running:
    countdown -= 1
    if countdown <= 0:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + TARGET_WIDTH and target_y <= mouse_y <= target_y + TARGET_HEIGHT:
                countup += 1
                color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
                target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)
    screen.fill(color)
    countdown_text = font.render(f"Осталось: {countdown} мс", True, (255, 255, 255))
    screen.blit(countdown_text, (285, 10))
    countup_text = font.render(f"Собрано: {countup} шансов из {UP}", True, (255, 255, 255))
    screen.blit(countup_text, (265, 570))
    screen.blit(target_image, (target_x, target_y))
    if countup >= UP:
        draw_fireworks(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 100,
                       [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)])
    pygame.display.update()

pygame.quit()
