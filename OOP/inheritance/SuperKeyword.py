# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

# Child class
class Student(Person):
    def __init__(self, name, age, dob):
        # Using the super() function to call the parent class constructor
        super().__init__(name, age)
        self.dob = dob

    def displayInfo(self):
        # Displaying the student's information
        print(self.name, self.age, self.dob)

# Creating an object of the Student class
obj = Student("Mayank", 23, "16-03-2000")
obj.display()       # Calling the display method from Person class
obj.displayInfo()   # Calling the displayInfo method from Student class
