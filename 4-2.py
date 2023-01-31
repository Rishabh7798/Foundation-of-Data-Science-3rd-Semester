#Design a python program(s) to understand the working of Functions.
#Write a program to find the power of a number using recursion.

base = int(input("Enter the number: "))
pow = int(input("Enter the power: "))

def power(base, pow):
    if pow == 0:
        return 1
    else:
        return base * power(base, pow-1)

print(power(base, pow))

