import pygame
import sys
from settings import Settings
from game_functions import Snake, Apple, drawgrid, load_record, save_record

pygame.init()

BLOCK_SIZE = 50

gm_settings = Settings()

screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
pygame.display.set_caption(gm_settings.caption)
clock = pygame.time.Clock()

FONT = pygame.font.Font("font.ttf", 50)


record_score = load_record()

score_rect = pygame.Rect(400, 20, 100, 50)
record_rect = pygame.Rect(400, 750, 100, 50)

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
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and snake.ydir == 0:
                snake.ydir = 1
                snake.xdir = 0
            elif (event.key == pygame.K_UP or event.key == pygame.K_w) and snake.ydir == 0:
                snake.ydir = -1
                snake.xdir = 0
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and snake.xdir == 0:
                snake.ydir = 0
                snake.xdir = 1
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and snake.xdir == 0:
                snake.ydir = 0
                snake.xdir = -1

    snake.update()

    drawgrid(screen)

    apple.update(screen)

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

    if snake.head.colliderect(apple.rect):
        snake.body.append(pygame.Rect(snake.body[-1].x, snake.body[-1].y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()

    pygame.display.update()
    clock.tick(5)
