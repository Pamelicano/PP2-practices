n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a, reverse=True)
print(*sorted_a)