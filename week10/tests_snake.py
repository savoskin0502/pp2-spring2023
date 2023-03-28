import random

import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

HEIGHT, WIDTH = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
BLOCK_SIZE = 40


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.points = [
            Point(10, 10)
        ]

    def draw(self):
        head = self.points[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(BLOCK_SIZE * head.x, BLOCK_SIZE * head.y, BLOCK_SIZE, BLOCK_SIZE)
        )

        for point in self.points[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, BLUE, rect)

    def move(self, dx, dy):
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy

        if self.points[0].x < 0:
            self.points[0].x = WIDTH // BLOCK_SIZE - 1

        elif self.points[0].x > WIDTH // BLOCK_SIZE - 1:
            self.points[0].x = 0
        #
        # if self.points[0].x < 0:
        #     self.points[0].x = WIDTH // BLOCK_SIZE - 1
        #
        # if self.points[0].x < 0:
        #     self.points[0].x = WIDTH // BLOCK_SIZE - 1

    def check_collision(self, food):
        if self.points[0].x != food.x:
            return False
        if self.points[0].y != food.y:
            return False
        return True


class Food:
    def __init__(self, x, y):
        self.point = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            pygame.Rect(BLOCK_SIZE * self.point.x, BLOCK_SIZE * self.point.y, BLOCK_SIZE, BLOCK_SIZE)
        )

    @property
    def x(self):
        return self.point.x

    @property
    def y(self):
        return self.point.y


def main():
    running = True
    snake = Snake()
    dx, dy = 0, 0
    food = Food(15, 15)

    while running:
        SCREEN.fill(BLACK)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = 1, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, 1

        snake.move(dx, dy)
        if snake.check_collision(food):
            snake.points.append(Point(snake.points[-1].x - dx, snake.points[-1].y - dy))
            food = Food(
                x=random.randint(1, WIDTH // BLOCK_SIZE - 1),
                y=random.randint(1, HEIGHT // BLOCK_SIZE - 1),
            )

        snake.draw()
        food.draw()

        pygame.display.flip()
        CLOCK.tick(10)


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


if __name__ == '__main__':
    main()
