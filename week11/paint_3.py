import collections

import pygame

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)


# Point = collections.namedtuple('Point', ['x', 'y'])

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return


class Button(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH // 2 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH // 2 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass


class Pen(GameObject):
    def __init__(self, *args, **kwargs):  # Pen(1, 2, 3, a=4) =>
        self.points: list[Point, ...] = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                WHITE,
                start_pos=(point.x, point.y),  # self.points[idx]
                end_pos=(next_point.x, next_point.y),
                width=5
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))  # (x, y) Point((x, y)) => Point(x, y)



class Rectangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            WHITE,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


def main():
    running = True
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen  # current_shape()
    button = Button()
    objects = [
        button
    ]

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    current_shape = Rectangle
                    # current_shape = button.connected_shape
                else:
                    active_obj = current_shape(start_pos=event.pos)
                    objects.append(active_obj)

            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object

        for obj in objects:
            obj.draw()

        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
    main()
