import numpy as np
from numpy import random as r

l1 = []
l2 = []

arr = r.choice([7, 20, 45, 60, 73, 80, 82, 98, 110, 128, 232, 240], size = (3, 4))
print("Array generated:\n", arr)

#SLICING

for x in arr:
    for y in x:
        #adding multiple of 10 in sliced array 1 and 0 at places of non-multiple of 10
        #adding 0 at places of multiple of 10 in sliced array 2 and values at other places
        if y % 10 == 0:
            l1.append(y)
            l2.append('X')
        else:
            l1.append('X')
            l2.append(y)

print()

a1 = np.array(l1)
sa1 = a1.reshape(3, 4)
print("Sliced array having multiples of 10 and X at other places:\n", sa1)
print()

a2 = np.array(l2)
sa2 = a2.reshape(3, 4)
print("Sliced array having non-multiples of 10 and X at other places:\n", sa2)
print()

#BOOLEAN INDEXING

print("The boolean indexing array of generated array:")
print(arr % 10 == 0)