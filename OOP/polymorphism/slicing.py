import numpy as np

print("-----------1 D ARRAY---------")
a = np.array([3,4,5,6,7,8,9,10])

print(a)
print("a[2:] - ",a[2:])
# a[2::] -  [ 5  6  7  8  9 10]

print("a[:5] - ",a[:5] )
# a[:5] -  [3 4 5 6 7]

print("a[1:5] -",a[1:5])
# a[1:5] - [4 5 6 7]
print("-----------2 D ARRAY----------")
 
b = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(b)
print(b[1, 1:4])
print("-----------3 D ARRAY----------")
c = np.array([[[1,2,3],[3,4,5]],[[9,8,7],[10,20,30]]])
print(c)
print()