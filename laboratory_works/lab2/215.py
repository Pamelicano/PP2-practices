n = int(input())
a = []
for _ in range(n):
    s = input()
    a.append(s)
s = set(a)
print(len(s))
