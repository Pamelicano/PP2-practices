n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    op = input().split()
    if op[0] == "abs":
        a = list(map(lambda x: abs(x), a))
    elif op[0] == "add":
        a = list(map(lambda x: x + int(op[1]), a))
    elif op[0] == "multiply":
        a = list(map(lambda x: x * int(op[1]), a))
    elif op[0] == "power":
        a = list(map(lambda x: x ** int(op[1]), a))
print(*a)