
# Boolean values are often used in conditional statements to control the flow of a program.
a = 200
b = 33
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
# You can also combine multiple boolean expressions using logical operators:
x = 5
print(x > 3 and x < 10)  # This will return True because both conditions are True
print(x > 3 or x < 4)   # This will return True because at least one condition is True
print(not(x > 3 and x < 10)) # This will return False because the expression is True, and not True is False
# Boolean values can also be used in loops to control iteration:
count = 0
while count < 5:
    print(count)
    count += 1
# This loop will print numbers from 0 to 4, as long as the condition count < 5 is True.
# In summary, boolean values (True and False) are fundamental in programming for making decisions, controlling flow, and evaluating conditions.
# They help determine the behavior of programs based on different conditions.
# You can also use comparison operators to create boolean expressions:
print(5 != 3)  # This will return True because 5 is not equal to 3
print(5 >= 3)  # This will return True because 5 is greater than
print(5 <= 3)  # This will return False because 5 is not less than or equal to 3
print(5 < 3)   # This will return False because 5 is not less than 3
print(5 > 3)   # This will return True because 5 is greater than 3
print(5 == 3)  # This will return False because 5 is not equal to 3


