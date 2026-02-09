class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b 

    def sum(self):
        return self.a + self.b

a1, b1, a2, b2 = map(int, input().split())
pair1 = Pair(a1, a2)
pair2 = Pair(b1, b2)
print(f"Result: {pair1.sum()} {pair2.sum()}")
