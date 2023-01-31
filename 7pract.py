# Design a Python program using Numpy library functions
import numpy as np

# Generate a 1D array of random numbers
array_1d = np.random.rand(10)
print("1D Array:\n", array_1d)

# Generate a 2D array of random numbers
array_2d = np.random.rand(3, 5)
print("\n2D Array:\n", array_2d)

# Calculate the mean of the 2D array
mean = np.mean(array_2d)
print("\nMean of the 2D Array:", mean)

# Calculate the standard deviation of the 2D array
std = np.std(array_2d)
print("\nStandard Deviation of the 2D Array:", std)

# Reshape the 2D array into a 3D array
array_3d = np.reshape(array_2d, (1, 3, 5))
print("\n3D Array:\n", array_3d)
