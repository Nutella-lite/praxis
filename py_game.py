import pygame
import random

pygame.init()

WIDTH, HEIGHT = 300, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тетрис")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Циан
    (255, 0, 0),    # Красный
    (0, 255, 0),    # Зеленый
    (255, 255, 0),  # Желтый
    (255, 165, 0),  # Оранжевый
    (0, 0, 255),    # Синий
    (128, 0, 128)   # Фиолетовый
]

# Размеры клетки
BLOCK_SIZE = 30
GRID_WIDTH = WIDTH // BLOCK_SIZE
GRID_HEIGHT = HEIGHT // BLOCK_SIZE

# Фигуры тетриса
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Tetris:
    def __init__(self):
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.get_new_piece()
        self.next_piece = self.get_new_piece()
        self.game_over = False

    def get_new_piece(self):
        return Tetromino(random.choice(SHAPES))

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(WIN, self.grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
                pygame.draw.rect(WIN, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_piece(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(WIN, piece.color, ((piece.x + x) * BLOCK_SIZE, (piece.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
                    pygame.draw.rect(WIN, WHITE, ((piece.x + x) * BLOCK_SIZE, (piece.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def check_collision(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    if piece.y + y >= GRID_HEIGHT or piece.x + x < 0 or piece.x + x >= GRID_WIDTH or self.grid[piece.y + y][piece.x + x] != BLACK:
                        return True
        return False

    def merge_piece(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[piece.y + y][piece.x + x] = piece.color

    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(self.grid[y][x] != BLACK for x in range(GRID_WIDTH)):
                del self.grid[y]
                self.grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])
                lines_cleared += 1
        return lines_cleared

    def update(self):
        if not self.game_over:
            self.current_piece.y += 1
            if self.check_collision(self.current_piece):
                self.current_piece.y -= 1
                self.merge_piece(self.current_piece)
                self.current_piece = self.next_piece
                self.next_piece = self.get_new_piece()
                if self.check_collision(self.current_piece):
                    self.game_over = True
            self.clear_lines()

    def move_piece(self, dx):
        if not self.game_over:
            self.current_piece.x += dx
            if self.check_collision(self.current_piece):
                self.current_piece.x -= dx

    def rotate_piece(self):
        if not self.game_over:
            self.current_piece.rotate()
            if self.check_collision(self.current_piece):
                for _ in range(3):
                    self.current_piece.rotate()

    def drop_piece(self):
        if not self.game_over:
            while not self.check_collision(self.current_piece):
                self.current_piece.y += 1
            self.current_piece.y -= 1
            self.update()

def main():
    clock = pygame.time.Clock()
    game = Tetris()
    fall_time = 0

    while True:
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_piece(-1)
                if event.key == pygame.K_RIGHT:
                    game.move_piece(1)
                if event.key == pygame.K_DOWN:
                    game.drop_piece()
                if event.key == pygame.K_UP:
                    game.rotate_piece()

        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= 0.5:
            game.update()
            fall_time = 0

        game.draw_grid()
        game.draw_piece(game.current_piece)

        pygame.display.flip()

if __name__ == "__main__":
    main()
pygame.quit()
