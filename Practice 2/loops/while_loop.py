# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  i += 1

#Note: remember to increment i, or else the loop will continue forever.

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
# The condition of the while loop is checked first, and if it is true, the body of the loop is executed.
# After the body is executed, the condition is checked again. If it is still true,
# the body is executed again. This continues until the condition becomes false.
# The example above will print numbers from 1 to 5. When i becomes 6, the condition i < 6 becomes false,
# and the loop stops.   
