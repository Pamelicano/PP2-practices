# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.
# The enumerate() function can be used in a for loop to get the index and value of
# the items in the collection.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
# The zip() function is used to map the similar index of multiple containers so that they can
# be used just using a single entity.
names = ["John", "Jane", "Doe"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)

#If one tuple contains more items, these items are ignored:

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)