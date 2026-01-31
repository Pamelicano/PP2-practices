"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
"""

a = 33
b = 200
if b > a:
    print("b is greater than a")
# In the example above we use the if statement to check whether b is greater than a.
# Since b is indeed greater than a, we print the message.

# The if statement evaluates a condition (an expression that results in True or False). 
# If the condition is true, the code block inside the if statement is executed. 
# If the condition is false, the code block is skipped.

number = 15
if number > 0:
  print("The number is positive")

# In this example, we check if the variable number is greater than 0.
# Since 15 is greater than 0, the condition evaluates to True, and the message
"""
Multiple Statements in If Block
You can have multiple statements inside an if block. All statements must be indented at the same level.
"""

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#Boolean variables can be used directly in if statements without comparison operators.

is_logged_in = True
if is_logged_in:
  print("Welcome back!")

  