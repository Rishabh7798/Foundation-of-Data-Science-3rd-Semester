# Design a Python program to replace all spaces from text with dash(-) from a given .txt file.
f=open("notepad\\fods05_b.txt","r+")
file=f.read()
print("\nGiven file :\n{}".format(file))

for i in file:
    if(i.isspace()):
        file=file.replace(i,"-")
print("\nFile after changes : \n{}".format(file))

f.close()
