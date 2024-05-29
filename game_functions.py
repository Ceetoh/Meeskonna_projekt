import pygame
import random

BLOCK_SIZE = 50

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [
            pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)
        ]
        self.dead = False

    def update(self):
        for square in self.body:
            if self.head.colliderect(square):
                self.dead = True
            if self.head.x not in range(0, 800) or self.head.y not in range(0, 800):
                self.dead = True
                
            if self.dead:
                self.__init__()

        self.body.insert(0, pygame.Rect(self.head.x, self.head.y, BLOCK_SIZE, BLOCK_SIZE))
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        if not self.dead:
            self.body.pop()

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, 800) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, 800) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self, screen):
        pygame.draw.rect(screen, "red", self.rect)

def drawgrid(screen):
    for x in range(0, 800, BLOCK_SIZE):
        for y in range(0, 800, BLOCK_SIZE):
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
