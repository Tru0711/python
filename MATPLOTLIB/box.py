import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data)
plt.title("Box Plot")
plt.xlabel("Distribution")
plt.ylabel("Value")
plt.show()