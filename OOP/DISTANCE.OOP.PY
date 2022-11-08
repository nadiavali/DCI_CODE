import math

# def distance(x1, y1, x2, y2):
#     return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

class Distance():
    def __init__(self, x, y) -> None:
        self.dx = y[0] - x[0]
        self.dy = y[1] - x[1]

    def distance(self):
        return math.sqrt((self.x -self.x1)**2 + (self.y -self.y1)**2)


d = Distance(2, 3, 5, 6)
print(d.distance())
