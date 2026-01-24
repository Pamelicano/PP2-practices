#String literals in Python can be enclosed in either single quotes or double quotes:

print("Hello")
print('Hello')

#You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Strings can be indexed (subscripted), with the first character having index 0.

b = "Hello, World!"
print(b[0])  #First character
print(b[7])  #Eighth character

#You can use negative indexing to start from the end of the string:

print(b[-1]) #Last character
print(b[-5]) #Fifth character from the end

#You can specify a range of characters by using the slice syntax.

print(b[2:5])  #Characters from position 2 to 4
print(b[:5])   #Characters from the beginning to position 4
print(b[2:])   #Characters from position 2 to the end
print(b[-5:-2]) #Characters from the fifth-last to the third-last

#Strings are immutable, which means they cannot be changed after they are created.
#But you can create a new string based on the existing string.