class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def shift(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def __str__(self):
        return f"Point({self.x}, {self.y})"


point1 = Point(10, 4)
point2 = Point(5, 12)

print(point1.distance(point2))
point1.shift(10, 1)

print(point1.distance(point2))
print(point2.__str__())
