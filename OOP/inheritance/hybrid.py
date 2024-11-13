class A:
    def method_a(self):
        return "Class A method"

class B(A):
    def method_b(self):
        return "Class B method"

class C(A):
    def method_c(self):
        return "Class C method"

class D(B, C):
    def method_d(self):
        return "Class D method"

# Testing Hybrid Inheritance
d = D()
print(d.method_a())
print(d.method_b())
print(d.method_c())
print(d.method_d())