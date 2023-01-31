#Design a python program(s) to understand the working of loops.
#Write a program to check whether the number entered is an armstrong number or not. (Sum of cubes of digits = Number)
n = int(input("Enter a number to be checked: "))
print()

sum = 0

# int to str
a = str(n)

# sum of cubes of digits
for x in range(len(a)):
    sum += int(a[x])**3
print("Since, sum of the cubes of digits is", sum)

# to check if sum = number or not
if sum == int(a):
    print("Therefore,", a, "is an armstrong number.")
else:
    print("Therefore,", a, "is not an armstrong number.")
    

# Enter the number : 153
# Digit cube sum is:  153
# Given number is a armstrong number
# PS E:\FODS practical> python -u "e:\FODS practical\2-2.py"
# Enter the number : 145
# Digit cube sum is:  190
# Given number is not a armstrong number