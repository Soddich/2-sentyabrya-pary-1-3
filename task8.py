class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color
    def draw(self):
        print("Рисуется фигура")

class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length
    def draw(self):
        print("Рисуется линия")

class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height
    def draw(self):
        print("Рисуется прямоугольник")

class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius
    def draw(self):
        print("Рисуется эллипс")

class Triangle(Figure):
    def draw(self):
        print("Рисуется треугольник")

line = Line((10,20), 5, "Синий", 15)
rect = Rect((5,2), 8, "Красный", 6)
ellipse = Ellipse((1,5), 10, "Желтый", 5)
triangle = Triangle((8,10), 6, "Зеленый")

figures = [line, rect, ellipse, triangle]

for figure in figures:
    figure.draw()