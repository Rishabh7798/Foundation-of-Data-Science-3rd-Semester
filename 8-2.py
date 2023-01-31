#Design a python program using Series module of Pandas library.

import pandas as pd

a = [1,7,2]

myvar1 = pd.Series(a)
print(myvar1)
print()
print("Element at index 0:", myvar1[0])

myvar2 = pd.Series(a, index = ["x","y","z"])
print(myvar2)
print()
print("Element at index y:", myvar2["y"])

calories = {"Day 1":420, "Day 2":380, "Day 3":390}

myvar3 = pd.Series(calories)
print(myvar3)

