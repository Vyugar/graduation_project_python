import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра в жанре аркада Pygame-Ball")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREEN = (6, 43, 3)
ORANGE = (255, 165, 0)

# Загрузка музыки и графики
pygame.mixer.music.load('assets/music/background.mp3')
pygame.mixer.music.play(-1)  # Бесконечное воспроизведение

background_image = pygame.image.load('assets/images/background.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Частота обновления
clock = pygame.time.Clock()
FPS = 60

# Класс платформы
class Paddle:
    def __init__(self):
        self.width = 150
        self.height = 20
        self.color = YELLOW
        self.rect = pygame.Rect(WIDTH // 2 - self.width // 2, HEIGHT - 30, self.width, self.height)
        self.speed = 10

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Класс шара
class Ball:
    def __init__(self):
        self.radius = 10
        self.color = RED
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.speed_x, self.speed_y = 5, -5

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Отскок от стен
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1
        if self.y - self.radius <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Класс блока
class Block:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GREEN
        self.active = True

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.color, self.rect)

# Класс падающего бонуса
class FallingBonus:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = ORANGE
        self.speed = 5
        self.active = True

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.color, self.rect)

# Создание блоков
def create_blocks(rows, cols):
    blocks = []
    block_width = WIDTH // cols
    block_height = 20
    for row in range(rows):
        for col in range(cols):
            block_x = col * block_width
            block_y = row * block_height
            blocks.append(Block(block_x, block_y, block_width - 5, block_height - 5))
    return blocks

# Проверка столкновений с блоками
def check_block_collisions(ball, blocks):
    for block in blocks:
        if block.active and block.rect.collidepoint(ball.x, ball.y):
            block.active = False
            ball.speed_y *= -1
            return 100  # Очки за разрушенный блок
    return 0

# Проверка столкновений с платформой
def check_collision(ball, paddle):
    if paddle.rect.collidepoint(ball.x, ball.y + ball.radius):
        ball.speed_y *= -1

# Проверка столкновений с бонусами
def check_bonus_collisions(paddle, bonuses):
    score_bonus = 0
    for bonus in bonuses:
        if bonus.active and paddle.rect.colliderect(bonus.rect):
            bonus.active = False
            score_bonus += 50  # Очки за пойманный бонус
    return score_bonus

# Создание бонуса с шансом
BONUS_PROBABILITY = 0.01  # Вероятность появления бонуса

def create_bonus():
    if random.random() < BONUS_PROBABILITY:
        x = random.randint(0, WIDTH - 20)
        return FallingBonus(x, 0, 20)
    return None

# Отображение счёта
def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Очки: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Отображение уровня
def draw_level(screen, level):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Уровень: {level}", True, WHITE)
    screen.blit(text, (WIDTH - 150, 10))

# Отображение оставшихся попыток
def draw_lives(screen, lives):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Осталось жизней: {lives}", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 100, 10))

# Основной игровой цикл
paddle = Paddle()
ball = Ball()
blocks = create_blocks(5, 10)
bonuses = []
score = 0
level = 1
lives = 3
running = True

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление объектов
    paddle.move(keys)
    ball.move()
    check_collision(ball, paddle)
    score += check_block_collisions(ball, blocks)

    # Создание бонусов
    new_bonus = create_bonus()
    if new_bonus:
        bonuses.append(new_bonus)

    # Обновление бонусов
    for bonus in bonuses:
        bonus.move()

    # Проверка столкновений с бонусами
    score += check_bonus_collisions(paddle, bonuses)

    # Удаление бонусов, вышедших за экран
    bonuses = [bonus for bonus in bonuses if bonus.active and bonus.rect.y <= HEIGHT]

    # Проверка проигрыша
    if ball.y - ball.radius > HEIGHT:
        lives -= 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball.speed_x, ball.speed_y = 5, -5
        if lives <= 0:
            print("Игра окончена!")
            running = False

    # Увеличение уровня и сложности
    if all(not block.active for block in blocks):
        level += 1
        ball.speed_x *= 1.1
        ball.speed_y *= 1.1
        blocks = create_blocks(5, 10)

    # Рендеринг
    screen.blit(background_image, (0, 0))
    paddle.draw(screen)
    ball.draw(screen)
    for block in blocks:
        block.draw(screen)
    for bonus in bonuses:
        bonus.draw(screen)
    draw_score(screen, score)
    draw_level(screen, level)
    draw_lives(screen, lives)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
