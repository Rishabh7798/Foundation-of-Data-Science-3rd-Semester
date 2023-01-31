import numpy as np
import matplotlib.pyplot as plt

# Generate some data to plot
x = np.random.randn(100)
y = np.random.randn(100)

# Plot the scatter plot
plt.scatter(x, y, color='blue', marker='x')

plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
