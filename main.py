import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GRID_SIZE,
    FRAME_RATE,
    GRID_WIDTH,
    GRID_HEIGHT,
    DETECTION_THRESHOLD,
    NUMBER_OF_ENEMIES,
    BLACK,
    WHITE,
)
from paddle import Paddle
from ball import Ball
from enemy import Enemy


def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            r = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, BLACK, r)


def collision_detection(paddle, ball, enemies):
    for elem in paddle.positions:
        if (
            abs(ball.position[0] - elem[0]) < DETECTION_THRESHOLD
            and abs(ball.position[1] - elem[1]) < DETECTION_THRESHOLD
        ):
            ball.velocity = ball.velocity[0], -1 * ball.velocity[1]
            return 0

    for enemy in enemies:
        if (
            enemy.exists
            and abs(ball.position[0] - enemy.position[0]) < DETECTION_THRESHOLD
            and abs(ball.position[1] - enemy.position[1]) < DETECTION_THRESHOLD
        ):
            ball.velocity = ball.velocity[0], -1 * ball.velocity[1]
            enemy.destroyed()
            return 1

    if ball.position[1] == 0:
        ball.velocity = ball.velocity[0], -1 * ball.velocity[1]
        return 0

    if ball.position[0] == 0:
        ball.velocity = (-1 * ball.velocity[0], ball.velocity[1])
        return 0

    if ball.position[1] >= SCREEN_HEIGHT - GRID_SIZE:
        return -1

    return 0


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    paddle = Paddle(0)
    ball = Ball(0)
    enemies = []
    for i in range(NUMBER_OF_ENEMIES):
        enemy = Enemy(i)
        enemies.append(enemy)

    draw_grid(surface)

    myfont = pygame.font.SysFont("monospace", 16)
    score = 0

    while True:
        clock.tick(FRAME_RATE)
        paddle.user_input()
        draw_grid(surface)
        paddle.move()
        ball.move()

        result = collision_detection(paddle, ball, enemies)
        if result == -1:
            score = 0
            ball.reset()
            for enemy in enemies:
                enemy.reset()
        if result == 1:
            score += 1

        paddle.draw(surface)
        ball.draw(surface)
        for enemy in enemies:
            enemy.draw(surface)
        screen.blit(surface, (0, 0))
        text = None
        if score == NUMBER_OF_ENEMIES:
            text = myfont.render("WINNER", 50, WHITE)
            screen.blit(text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
            ball.destroy()
        else:
            text = myfont.render(f"Score: {score}", 1, WHITE)
            screen.blit(text, (5, 10))
        pygame.display.update()


main()
