# In programming you often need to know if an expression is True or False.

# You can evaluate any expression in Python, and get one of two answers, True or False.

# For example:
print(10 > 9)  # This will return True because 10 is greater than 9
print(10 == 9) # This will return False because 10 is not equal to 9
print(10 < 9)  # This will return False because 10 is not less

# You can also use the bool() function to evaluate any value, and give you True or False.
print(bool("Hello")) # This will return True because non-empty strings are considered True
print(bool(15))      # This will return True because non-zero numbers are considered True
print(bool(0))       # This will return False because zero is considered False
print(bool(""))      # This will return False because empty strings are considered False
print(bool(None))    # This will return False because None is considered False

# You can use the bool() function to evaluate any expression, for example:
print(bool(10 > 9))  # This will return True
print(bool(10 == 9)) # This will return False

# You can also use comparison operators to create boolean expressions:
print(5 != 3)  # This will return True because 5 is not equal
print(5 >= 3)  # This will return True because 5 is greater than or equal to 3
print(5 <= 3)  # This will return False because 5 is not less than or equal to 3
print(5 < 3)   # This will return False because 5 is not less than 3
