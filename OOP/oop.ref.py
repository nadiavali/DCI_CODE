# Add a method reflect_x to Point which returns a new Point, one which is the reflection 
# of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)

class Reflection():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def reflect_x(self):
        return (self.x,-self.y)



p = Reflection(2, 3)
print(p.reflect_x())
