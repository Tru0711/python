class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal Constructor")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed
        print("Dog Constructor")

dog = Dog("Buddy", "Golden Retriever")
