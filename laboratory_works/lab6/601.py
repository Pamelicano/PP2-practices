n = int(input())
numbers = list(map(int, input().split()))
sq = list(map(lambda x: x**2, numbers))
print(sum(sq))
