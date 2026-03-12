

# The map() function applies a given function to each item of an iterable (e.g. list) and returns 
# a list of the results.
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# The filter() function constructs an iterator from elements of an iterable for
#  which a function returns true.
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

# The reduce() function is a part of the functools module and is used to apply a function of 
# two arguments cumulatively to the items of an iterable, 
# from left to right, to reduce the iterable to a single value.
from functools import reduce
def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)
