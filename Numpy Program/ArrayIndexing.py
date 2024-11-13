import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr)
# Accessing element at index 2
print("Element at index 2:", arr[2])
print("-----------------------------------------")
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# Accessing element at row 1, column 2
print("Element at (1, 2):", arr_2d[1, 2])
print("-----------------------------------------")
print(arr)

# Slicing from index 1 to 3 (exclusive)
print("Sliced Array:", arr[1:4])
print("-----------------------------------------")

print(arr_2d)
# Slicing first row
print("First Row:", arr_2d[0, :])

# Slicing first column
print("First Column:", arr_2d[:, 0])
