import pygame
import sys
import random
from settings import Settings

pygame.init()

SW, SH = 800, 800
BLOCK_SIZE = 50
FONT = pygame.font.Font("font.ttf", BLOCK_SIZE*2)

gm_settings = Settings()

screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
pygame.display.set_caption(gm_settings.caption)
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        global apple
        global current_score
        global record_score

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                self.dead = True
                
            if self.dead:
                self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
                self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
                self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
                self.xdir = 1
                self.ydir = 0
                self.dead = False
                apple = Apple()
                current_score = 1
                save_record(record_score)

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, "red", self.rect)

def drawgrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#ffffff", rect, 1)

def load_record():
    try:
        with open("record.txt", "r") as file:
            return int(file.readline().strip())
    except FileNotFoundError:
        return 0

def save_record(record):
    with open("record.txt", "w") as file:
        file.write(str(record))

current_score = 1
record_score = load_record()

score = FONT.render(str(current_score), True, "white")
score_rect = score.get_rect(center=(SW / 2, SH / 20))

record = FONT.render(str(record_score), True, "white")
record_rect = record.get_rect(center=(SW / 2, SH - 50))

drawgrid()

snake = Snake()
apple = Apple()

running = True
while running:
    screen.fill(gm_settings.bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and snake.ydir == 0:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP and snake.ydir == 0:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT and snake.xdir == 0:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT and snake.xdir == 0:
                snake.ydir = 0
                snake.xdir = -1

    snake.update()

    screen.fill('green')
    drawgrid()

    apple.update()

    current_score = len(snake.body) + 1
    score = FONT.render(f"{current_score}", True, "white")
    screen.blit(score, score_rect)

    if current_score > record_score:
        record_score = current_score
        save_record(record_score)

    record = FONT.render(f"Record: {record_score}", True, "white")
    screen.blit(record, record_rect)

    pygame.draw.rect(screen, "#fc8403", snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, "#fc8403", square)

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()

    pygame.display.update()
    clock.tick(5)
