# Q4. Create a class Shape with a method area(). 
# Create subclasses Circle , , and that override the area() 
# method.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height


# Example
circle = Circle(5)
square = Square(4)
rectangle = Rectangle(3, 6)
print(f"Area of Circle: {circle.area()}")
print(f"Area of Square: {square.area()}")
print(f"Area of Rectangle: {rectangle.area()}")


