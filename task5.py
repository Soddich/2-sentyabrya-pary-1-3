class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

class Circle(Figure):
    def __init__(self, coords, width, color):
        super().__init__(coords, width, color)

circle = Circle((10,20), 5, "Желтый")

print(circle.coords, circle.width, circle.color)
