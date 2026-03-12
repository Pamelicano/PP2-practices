n = int(input())
a = list(map(int, input().split()))
if all(map(lambda x: x >= 0, a)):
    print("Yes")