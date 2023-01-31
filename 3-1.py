#Design a python program(s) to understand the working of loops.
#Write a program to print Fibonacci Series using ‘For’ loop.

n = int(input("Enter number of terms you want in your Fibonacci Series: "))
print()

print("The FIBONACCI SERIES till ", n, "terms is as follows:")
a = 0
b = 1
print(a, b, sep = '\n')

# to generate terms of series
for i in range(n-1):
    c = a+b
    a = b
    b = c
    print(c)
