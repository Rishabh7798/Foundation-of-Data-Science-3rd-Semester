# Design a Python program to reverse each word in a given .txt file.
f=open("notepad\\fods05_c.txt",'r+')
file=f.read()
print("Given File is : \n{}".format(file))
rev_file="".join(reversed(file))
print("\nReversed File is : \n{}".format(rev_file))
