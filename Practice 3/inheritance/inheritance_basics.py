# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
  pass

# Now the Student class has the same properties and methods as the Person class.

x = Student("Mike", "Olsen")
x.printname()

# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).


class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    pass

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        pass

# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.
