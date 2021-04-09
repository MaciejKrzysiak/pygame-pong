from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, LEFT, RIGHT, WHITE
import random
import pygame
import sys


class Paddle:
    def __init__(self, id):
        self.id = id
        self.length = 3
        self.positions = [
            [SCREEN_WIDTH / 2 - GRID_SIZE, SCREEN_HEIGHT - 2 * GRID_SIZE],
            [SCREEN_WIDTH / 2, SCREEN_HEIGHT - 2 * GRID_SIZE],
            [SCREEN_WIDTH / 2 + GRID_SIZE, SCREEN_HEIGHT - 2 * GRID_SIZE],
        ]
        self.direction = (0, 0)
        self.color = WHITE

    def turn(self, point):
        self.direction = point

    def draw(self, surface):
        for elem in self.positions:
            r = pygame.Rect((elem[0], elem[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    def reset(self):
        self.positions = [
            (SCREEN_WIDTH / 2 - GRID_SIZE, SCREEN_HEIGHT - 2 * GRID_SIZE),
            (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 2 * GRID_SIZE),
            (SCREEN_WIDTH / 2 + GRID_SIZE, SCREEN_HEIGHT - 2 * GRID_SIZE),
        ]
        self.direction = random.choice([LEFT, RIGHT])

    def move(self):
        x, y = self.direction
        for i in range(3):
            self.positions[i][0] = (self.positions[i][0] + x * GRID_SIZE) % SCREEN_WIDTH

    def user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                if event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
