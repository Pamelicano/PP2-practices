class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def move(self, new_x, new_y):
        self.x  = new_x
        self.y  = new_y
    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

point = Point(x1, y1)
print(point)
point.move(x2, y2)
print(point)
point.dist(Point(x3, y3))
print(f"{point.dist(Point(x3, y3)):.2f}")