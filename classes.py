# Defining a class is similar to C#
class Point:
    def move(self):
        print("move function")

    def draw(self):
        print("draw function")

# This is how we call a method of a class
point1 = Point().draw()  
point2 = Point().move()

point3 = Point()

point3.move()
point3.x = 10
point3.y = 20
print(point3.x)