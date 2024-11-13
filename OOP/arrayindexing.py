import numpy as np

a = np.array([12])
b = np.array([3,4,6,8])
c = np.array([[1,2,3],[5,6,7]])
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])

# POSITIVE INDEXING
print(a[0])
print(b[3])
print(c[0,2])
print(d[0,1,2])

# NEGATIVE INDEXING
print("c[0,2] : ",c[0,-2])
print("d[0,1,-1] : ",d[0,1,-1])