E=2.718

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def area_of_triangle(b, h):
    return 0.5 * b * h


class Square:

    def area(self,side):
        return side*side

    def perimeter(self,side):
        return 4*side


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)







