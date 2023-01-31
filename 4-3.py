#Design a python program(s) to understand the working of Functions.
#Write a program to find the middle element of a string passed and if the middle element is not there, then return null string.

string = input("Enter the string: ")

def mid(string):
    n = len(string)
    if n%2 == 1:
        middle = n//2
        return string[middle]
    else:
        return "'NULL'"

print(mid(string))

        
