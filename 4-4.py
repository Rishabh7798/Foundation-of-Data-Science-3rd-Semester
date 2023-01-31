#Design a python program(s) to understand the working of Functions.
#Write a program to print a pattern that should be accepted, input an integer and print the pattern accordingly.

number = input("Enter the number: ")

def pattern(number):
    n = len(number)
    y = 0
    for i in range(n):
        for j in range(int(number[y])):
            print("*", end = " ")
        y += 1
        print()

pattern(number)
    
