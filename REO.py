# Parent Class: Shape
class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

# Child Class: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Child Class: Square (inherits from Rectangle)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# Child Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Example Usage
if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    print(f"Rectangle Area: {rectangle.area()}")
    print(f"Rectangle Perimeter: {rectangle.perimeter()}")

    square = Square(4)
    print(f"Square Area: {square.area()}")
    print(f"Square Perimeter: {square.perimeter()}")

    circle = Circle(3)
    print(f"Circle Area: {circle.area():.2f}")
    print(f"Circle Perimeter: {circle.perimeter():.2f}")
