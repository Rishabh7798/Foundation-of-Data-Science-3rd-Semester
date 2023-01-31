#Design a python program using Random module of NumPy library.

#RANDOM MODULE
from numpy import random
import numpy as np

#generate random number
x = random.randint(100)
print("A random number below 100 is", x)
print()

#generate random array
x = random.randint(100, size = (5))
print("Array of 5 random numbers below 100 is\n",x)
x = random.randint(100, size = (3, 5))
print("Array of 3 rows and 5 columns having elements below 100 is\n",x)
print()

#random data distribution
#generate 1D array containing 100 values, where each value has to be 2, 4, 6 or 8
x = random.choice([2, 4, 6, 8], p = [0.1, 0.2, 0.3, 0.4], size = (100))
print("1D array having 100 elements where each element is 2 or 4 or 6 or 8 is\n",x)
print()

#shuffling arrays
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
random.shuffle(arr)
print("Shuffled array:", arr)
print()

#generating permutation of array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("A permutation of array", arr, "is", random.permutation(arr))

