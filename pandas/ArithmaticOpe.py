import pandas as pd

# Create two arrays as pandas Series
array1 = pd.Series([10, 20, 30, 40, 50])
array2 = pd.Series([5, 10, 15, 20, 25])

# Perform arithmetic operations
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

# Display results
print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)
print("\nAddition of Array 1 and Array 2:")
print(addition)
print("\nSubtraction of Array 1 and Array 2:")
print(subtraction)
print("\nMultiplication of Array 1 and Array 2:")
print(multiplication)
print("\nDivision of Array 1 and Array 2:")
print(division)


'''
Array 1:
0    10
1    20
2    30
3    40
4    50
dtype: int64

Array 2:
0     5
1    10
2    15
3    20
4    25
dtype: int64

Addition of Array 1 and Array 2:
0    15
1    30
2    45
3    60
4    75
dtype: int64

Subtraction of Array 1 and Array 2:
0     5
1    10
2    15
3    20
4    25
dtype: int64

Multiplication of Array 1 and Array 2:
0      50
1     200
2     450
3     800
4    1250
dtype: int64

Division of Array 1 and Array 2:
0    2.0
1    2.0
2    2.0
3    2.0
4    2.0
dtype: float64
'''