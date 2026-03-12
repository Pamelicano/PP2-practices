# To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for reading the content of the file:


f = open("demofile.txt")
print(f.read())

# Open a file on a different location:

f = open("D:\\myfiles\welcome.txt")
print(f.read())

# You can also use the with statement when opening a file:

with open("demofile.txt") as f:
  print(f.read())

#   Close the file when you are finished with it:

f = open("demofile.txt")
print(f.readline())
f.close()

# You can return one line by using the readline() method:

with open("demofile.txt") as f:
  print(f.readline())

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
        

with open("demofile.txt") as f:
  print(f.read(5))