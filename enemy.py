from constants import (
    SCREEN_WIDTH,
    GRID_SIZE,
    GRID_WIDTH,
    WHITE,
    BLACK,
)
import pygame


class Enemy:
    def __init__(self, id):
        self.id = id
        self.position = [0, 0]
        self.exists = True
        self.color = WHITE
        self.set_position()

    def set_position(self):
        offset = self.id // (GRID_WIDTH / 2)
        if self.id >= (GRID_WIDTH / 2):
            offset = offset * 2 * GRID_SIZE
        self.position = [
            (2 * self.id * GRID_SIZE) % SCREEN_WIDTH,
            2 * GRID_SIZE + offset,
        ]

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, self.color, r, 1)

    def reset(self):
        self.color = WHITE
        self.exists = True

    def destroyed(self):
        self.color = BLACK
        self.exists = False
