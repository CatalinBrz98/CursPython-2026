from math import pi

class Shape:
    def area(self) -> float:
        raise NotImplementedError()

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        # verificam daca suma celor 2 laturi mai mici este strict mai mare decat cea mai mare latura (si ridicam ValueError daca nu)

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

if __name__ == "__main__":
    shapes = [Rectangle(100, 200), Circle(100), Triangle(100, 200, 150)]
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    print(total_area)