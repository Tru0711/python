class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age if age is not None else "Unknown"

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

person1 = Person("Alice", 30)
person2 = Person("Bob")
print(person1.display())
print(person2.display())
