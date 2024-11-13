import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
ax.scatter(x, y, z)
ax.set_title("3D Scatter Plot")
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()