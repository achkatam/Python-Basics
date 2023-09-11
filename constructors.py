# Defining a class is similar to C#
class Point:
    def __init__(self, x, y): # Constructor
        self.x = x
        self.y = y
    
    def move(self):
        print("move function")

    def draw(self):
        print("draw function")


point = Point(10, 20)
point.x = 14
result = point.x
print(result)