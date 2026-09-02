class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

line = Line((10,20), 5, "Синий", 15)
rect = Rect((5,2), 8, "Красный", 6)
ellipse = Ellipse((1,5), 10, "Желтый", 5)

print(line.coords, line.width, line.color, line.length)
print(rect.coords, rect.width, rect.color, rect.height)
print(ellipse.coords, ellipse.width, ellipse.color, ellipse.radius)