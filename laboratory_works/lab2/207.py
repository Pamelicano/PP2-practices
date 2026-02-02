n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(1)
    exit()
mx = a[0]
id = -1
for i in a:
    if i > mx:
        mx = i
        id = a.index(i)
print(id+1)
