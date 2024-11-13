class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("successfully deleted.")

p = Person("trupti")
del p