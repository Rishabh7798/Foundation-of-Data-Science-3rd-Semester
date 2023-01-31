import numpy as np
import matplotlib.pyplot as plt

# Generate a set of random x and y data
x = np.random.randn(100)
y = x * 3 + 2 + np.random.randn(100)

# Calculate the slope and intercept of the line of best fit
a, b = np.polyfit(x, y, 1)

# Plot the scatter plot
plt.scatter(x, y, color='blue')

# Plot the line of best fit
x_fit = np.linspace(np.min(x), np.max(x), 100)
y_fit = a * x_fit + b
plt.plot(x_fit, y_fit, color='red', linewidth=2)

plt.title("Scatter Plot with Line of Best Fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
