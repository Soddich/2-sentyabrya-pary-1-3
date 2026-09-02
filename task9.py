import math
class Figure:
    def __init__(self, coords):
        self._coords = coords

    def get_coords(self):
        return self._coords

    def set_coords(self, coords):
        self._coords = coords

class Circle(Figure):
    def __init__(self, coords, radius):
        super().__init__(coords)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Square(Figure):
    def __init__(self, coords, side):
        super().__init__(coords)
        self.side= side
    def calculate_area(self):
        return self.side ** 2

circle1 = Circle((10, 20), 5)
circle2 = Circle((5, 10), 1)
circle3 = Circle((15, 10), 10)
square1 = Square((30, 40), 4)
square2 = Square((20, 10), 2)

figures = [circle1, circle2, circle3, square1, square2]
total_area = 0

for figure in figures:
    total_area = total_area + figure.calculate_area()

print(f"Общая площадь составляет {total_area}")