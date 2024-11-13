class Grandparent:
    def grandparent_wisdom(self):
        return "Grandparent's wisdom"

class Parent(Grandparent):
    def parent_love(self):
        return "Parent's love"

class Child(Parent):
    def child_dreams(self):
        return "Child's dreams"

# Testing Multilevel Inheritance
c = Child()
print(c.grandparent_wisdom())
print(c.parent_love())
print(c.child_dreams())