
class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

n, m = map(int, input().split())
rectangle = Rectangle(n, m)
print(rectangle.area())