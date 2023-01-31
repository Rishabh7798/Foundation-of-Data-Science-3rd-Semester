# Design a python program using NumPy library functions.
#Design a python program using NumPy library functions.

from numpy import random
import numpy as np

#checking version
print("Current version:", np.__version__)
print()

#making array using list
arr = np.array([1, 2, 3, 4, 5, 6])
print("Array is", arr)

#type of array
print("Type :", type(arr))
print()

#dimensions in arrays
print("DIMENSIONS OF ARRAY -\n")
print("Types of dimensions -")
print("0D array is \n{}".format(np.array(200)))
print("1D array is \n{}".format(np.array([1, 2, 3, 4, 5, 6])))
print("2D array is \n{}".format(np.array([[1, 2, 3], [4, 5, 6]])))
print("3D array is \n{}".format(np.array([[1, 2, 3], [10, 20, 30], [100, 200, 300]])))
print()

#check number of dimensions
a = np.array(42)
b = np.array([1,2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[10, 20, 30], [40, 50, 60]]])
print("Checking number of dimensions of given arrays -")
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print()

#higher dimensional arrays
#an array can have any number of dimensions
arr = np.array([1, 2, 3, 4], ndmin = 5)
print("Converting array to higher dimensional array -\n",arr)
print()

#access array elements
print("ACCESSING ELEMENTS OF ARRAY -\n")
arr = np.array([1, 2, 3, 4])
print("Element at index 1 of\n",arr, "\nis", arr[1])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("The 5th element on 2nd row of\n",arr, "\nis", arr[1, 4])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[10, 20 ,30], [40, 50, 60]]])
print("The 3rd element of 2nd array of 1st array of\n",arr, "\nis", arr[0, 1, 2])
print()

#slicing arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("SLICING -")
print("Slicing an array",arr," from 2nd element to 5th element gives",arr[1:5])
print()

#copy
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print("COPY -")
print(arr)
print(x)
print()

#view
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print("VIEW -")
print(arr)
print(x)
print()

#NumPy array shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("ARRAY SHAPE -")
print(arr.shape)
print()

#reshaping arrays
#reshape from 1D to 2D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(4, 3)
print("RESHAPING -\n")
print("Original array is\n", arr)
print("Reshaped array is\n", new_arr)
print()

#reshape from 1D to 2D
new_arr = arr.reshape(2, 3, 2)
print("Original array is\n", arr)
print("Reshaped array is\n", new_arr)
print()

#flattening the arrays
#flattening an array means converting a multi-dimensional array into 1D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
new_arr = arr.reshape(-1)
print("FLATTENING -\n")
print("Original array is\n", arr)
print("Reshaped array is\n", new_arr)
print()

#iterating 2D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("ITERATION -\n")
print("Using 'for' loop -")
print("Original array -\n", arr)
print("After iteration -")
for x in arr:
    for y in x:
        print(y)
print()

#iterating arrays using nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Using 'nditer()' function -")
print("Original array -\n", arr)
print("After iteration -")
for x in np.nditer(arr):
    print(x)
print()

#joining NumPy arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print("CONCATENATION -")
print(arr)
print()

#joining arrays using stack functions
#stacking along rows
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print("JOINING -\n")
print("Array 1 is",arr1)
print("Array 2 is",arr2)
print()
print("Joining along rows -")
print(arr)

#stacking along columns
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print("Joining along columns -")
print(arr)

#stacking along height (depth)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print("Joining along height -")
print(arr)
print()

#splitting numpy arrays
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 3)
print("SPLTTING -")
print(new_arr)
print()

#filtering arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
new_arr = arr[filter_arr]
print("FILTERING -")
print("T/F array based on filtering condition is", filter_arr)
print("Filtered array is", new_arr)
