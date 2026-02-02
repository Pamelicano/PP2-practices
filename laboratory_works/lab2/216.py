n = int(input())
a = list(map(int, input().split()))
freq = {}
for i in range(n):
    if a[i] in freq:
        print("NO")
    else:
        print("YES")
        freq[a[i]] = 1
