class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

math_op = MathOperations()
print(math_op.add(3, 5))      # Two arguments
print(math_op.add(3, 5, 7))   # Three arguments
