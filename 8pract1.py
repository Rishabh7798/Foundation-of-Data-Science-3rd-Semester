# Perform Statistics and Data Visualization in python.
import numpy as np
import matplotlib.pyplot as plt

# Generate a 1D array of random numbers
array = np.random.randn(100)

# Calculate the mean and standard deviation of the array
mean = np.mean(array)
std = np.std(array)

# Plot a histogram of the array
plt.hist(array, bins=20, color='blue')
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2)
plt.axvline(mean + std, color='green', linestyle='dashed', linewidth=2)
plt.axvline(mean - std, color='green', linestyle='dashed', linewidth=2)
plt.title("Histogram of Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
