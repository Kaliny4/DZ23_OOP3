"""
Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание двух окружностей,
вычитание радиусов произвести по модулю.
Если вычитаются две окружности с одинаковым значением радиуса,
то результатом вычитания будет точка класса Point.
"""

import math
from DZ23_OOP3_Point import Point


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return super().__str__()[:-1] + f', radius={self.radius})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius**2)

#перевизначений спецметод __sub__ (x-y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        return Circle(radius, x, y) if radius else Point(x, y)


a = Circle(8, 12, 13)
b = Circle(8, 5, 3)
print(a)
print(b)
print(a - b)
