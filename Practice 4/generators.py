
#TASK 1: Create a generator function that yields the squares of numbers from 1 to N.
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

#TASK 2:Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
even_numbers = even_generator(n)
print(", ".join(str(num) for num in even_numbers))

#TASK 3: Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def div_gen(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
div_nums = div_gen(n)
print(", ".join(str(num) for num in div_nums))

#TASK 4:Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a, b = map(int, input().split())
for square in squares(a, b):
    print(square)

#TASK 5: Implement a generator that returns all numbers from (n) down to 0.

def countdown(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
for num in countdown(n):
    print(num)