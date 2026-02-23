
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

n = int(input())   
for i in square_generator(n):
    print(i)