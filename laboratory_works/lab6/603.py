n = int(input())

x = list(map(str, input().split()))
for i, block in enumerate(x):
    print(str(i)+":"+block, end = " ")

