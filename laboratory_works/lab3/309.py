class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2

r = int(input())
circle = Circle(r)
print(f"{circle.area():.2f}")