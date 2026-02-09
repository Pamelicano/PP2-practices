# You can send arguments with the key = value syntax.
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Buddy")

# This way, with keyword arguments, the order of the arguments does not matter.

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

# The phrase Keyword Arguments is often shortened to kwargs in Python documentation.

# You can mix positional and keyword arguments in a function call.

# However, positional arguments must come before keyword arguments:

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")
