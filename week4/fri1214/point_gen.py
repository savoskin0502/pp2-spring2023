import collections
import random


Point = collections.namedtuple('Point', ['x', 'y', 'symbol'])


# class Board:
    # def __init__(self):
    #     self.points = [
    #         [Point(),]
    #         [Point(), ]
    #     ]
    #
    # def display(self):
    #     pass


def point_generator(start_point, end_point):
    # start_point, end_point = 1, 10
    while True:
        yield Point(
            x=random.randint(start_point, end_point - 1),
            y=random.randint(start_point, end_point - 1),
            symbol=' * ',
        )


def display_points(points: list[Point, ...], board_size=5):
    board = [
        [' - ' for _ in range(board_size)]
        for _ in range(board_size)
    ]

    for point in points:
        board[point.x][point.y] = point.symbol

    print(
        *[''.join(row) for row in board], sep='\n'  #
    )


def is_rectangle(points: list[Point]):
    if len(points) != 4:
        return 'фигура должна иметь 4 стороны'

    print(
        (points[1].x - points[0].x), (points[1].y - points[0].y)
    )
    # [1, 2, 3, 4] => [ [1, 3, 4, 2],  [1, 4, 2, 3]]


size = 5
factory = point_generator(0, size)
point1 = next(factory)
point2 = next(factory)
point3 = next(factory)
point4 = next(factory)
display_points([point1, point2, point3, point4], board_size=size)
is_rectangle([point1, point2, point3, point4])