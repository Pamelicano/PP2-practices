n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))


ans = 0
w = zip(x, y)
for i in w:
    ans += i[0]*i[1]
print(ans)