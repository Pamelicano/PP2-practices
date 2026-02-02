n = int(input())
a = []
for _ in range(n):
    s = input()
    a.append(s)

first_pos = {}
for i in range(n):
    if a[i] not in first_pos:
        first_pos[a[i]] = i + 1

for key in sorted(first_pos):  
    print(key, first_pos[key])
