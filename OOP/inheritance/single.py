class Parent:
    def show(self):
        return "Parent class"

class Child(Parent):
    def display(self):
        return "Child class"

# Testing Single Inheritance
c = Child()
print(c.show())
print(c.display())