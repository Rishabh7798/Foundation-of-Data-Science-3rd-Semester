#Design a python program to generate and print a list except for the first five elements, where the values are squares of numbers between 1 and 30.

n = int(input("Enter no. of elements in a list: "))
x = 0
list, flist = [], []
print()

# to ask for elements from user
for i in range(n):
    element = int(input("Enter element: "))
    list.append(element)
print()

# to check whether no. of elements >5 or not
if n < 5:
    print("There are only", n, "elements in a list.")
else:
    for j in range(5, n):
        if list[j]**2 > 1 and list[j]**2 < 30:
            flist.append(list[j])
            x = 1
    print("List to be analyzed: ", list)
    print("\nList containing elements after 5th element whose squares are between 1 and 30: ", flist)

# print message if there is no required element
if x == 0:
    print("\nThere is no element after 5th element whose square is between 1 and 30.")
