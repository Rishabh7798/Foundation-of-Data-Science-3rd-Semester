# Design a Python program to understand the working of loops.
#3.Design a python program to print pascals triangle.
from math import factorial

numRows=int(input("Enter the number of Rows you want : "))
print("Required Pascal's Triangle is : ")

def pascal_tri(numRows):
    for i in range(numRows):
        # loop to get spaces
        for j in range(numRows-i+1):
            print(end=" ")
        # loop to get elements of row i
        for j in range(i+1):
            # nCr = n!/((n-r)!*r!)
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print("\n")
pascal_tri(numRows)

# Enter the number of Rows you want : 6
# Required Pascal's Triangle is : 
#        1

#       1 1

#      1 2 1

#     1 3 3 1

#    1 4 6 4 1

#   1 5 10 10 5 1