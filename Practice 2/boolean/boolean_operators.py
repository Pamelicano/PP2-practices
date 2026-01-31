# Logical operators are used to combine conditional statements:
x = 5
print(x > 3 and x < 10)  # This will return True because both
print(x > 3 or x < 4)   # This will return True because at least one condition is True  
print(not(x > 3 and x < 10)) # This will return False because the expression is True, and not True is False
# You can use logical operators to build complex boolean expressions:
a = 10
b = 20
print((a < b) and (b > 15))  # This will return True because both conditions are True
print((a > b) or (b > 15))   # This will return True
print(not(a > b))            # This will return True because a > b is False, and not False is True
# Logical operators can also be used in conditional statements:
if (a < b) and (b > 15):
    print("Both conditions are True")
else:
    print("At least one condition is False")
# You can also use logical operators in loops:
count = 0
while (count < 5) and (count % 2 == 0):
    print(count)
    count += 1
# This loop will print even numbers from 0 to 4, as long as the condition is True.
"""
In summary, logical operators (and, or, snot) are essential for combining multiple boolean
expressions and controlling the flow of a program based on complex conditions.
"""