#  method_overriding in python inheritance with examples
class Parent:
    def show(self):
        print("This is the parent class method.")

class Child(Parent):
    def show(self):
        print("This is the child class method.")

# Create an instance of the Child class
child_instance = Child()
# Call the show method, which will use the overridden method in the Child class
child_instance.show()
# Output: This is the child class method.
# Create an instance of the Parent class
parent_instance = Parent()
# Call the show method, which will use the method in the Parent class
parent_instance.show()
# Output: This is the parent class method.
