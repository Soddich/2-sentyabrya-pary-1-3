class Graph:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._scale = 1

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def change_scale(self, factor):
        self._scale *= factor

graph1 = Graph()
graph2 = Graph()
graph3 = Graph()

graph1.move(10, 5)

graph2.change_scale(2)

print(f"Состояние первого объекта: x={graph1._x}, y={graph1._y}, scale={graph1._scale}")
print(f"Состояние второго объекта: x={graph2._x}, y={graph2._y}, scale={graph2._scale}")
print(f"Состояние третьего объекта: x={graph3._x}, y={graph3._y}, scale={graph3._scale}")