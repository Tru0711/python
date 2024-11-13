import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 4]
data = np.random.randn(1000)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Line Plot')
axs[0, 1].scatter(np.random.rand(50), np.random.rand(50))
axs[0, 1].set_title('Scatter Plot')
axs[1, 0].bar(categories, values)
axs[1, 0].set_title('Bar Chart')
axs[1, 1].hist(data)
axs[1, 1].set_title('Histogram')
plt.tight_layout()
plt.show()