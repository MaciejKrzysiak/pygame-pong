from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, LEFT, RIGHT, WHITE, BLACK
import random
import pygame


class Ball:
    def __init__(self, id):
        self.id = id
        self.position = [
            SCREEN_WIDTH / 2 - GRID_SIZE,
            SCREEN_HEIGHT / 2 - 2 * GRID_SIZE,
        ]
        self.direction = random.choice([LEFT, RIGHT])
        self.color = WHITE
        self.velocity = [random.choice([-1, 1]), 1]

    def reset(self):
        self.position = [
            SCREEN_WIDTH / 2 - GRID_SIZE,
            SCREEN_HEIGHT / 2 - 2 * GRID_SIZE,
        ]

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, self.color, r, 1)

    def move(self):
        self.position[0] = (
            self.position[0] + self.velocity[0] * GRID_SIZE
        ) % SCREEN_WIDTH
        self.position[1] = (
            self.position[1] + self.velocity[1] * GRID_SIZE
        ) % SCREEN_HEIGHT

    def destroy(self):
        self.color = BLACK
