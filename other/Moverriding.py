class Parent:
    def show(self):
        print("Inside Parent")

class Child(Parent):
    def show(self):
        print("Inside Child")

child = Child()
child.show()                    