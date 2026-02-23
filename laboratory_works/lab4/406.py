def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
n = int(input())
g = fib()
first = True
for i in range(n):
    if first:
        print(next(g), end="")
        first = False
    else:
        print(f",{next(g)}", end="")
print()