#Design a python program to count the total number of lower case, upper case letters and digits from a given .txt file.

file = open("Sample.txt", "r")
content = file.read()
print(content)

uc_count, lc_count, digits_count = 0, 0, 0

for i in content:
    if (i.islower()):
        lc_count += 1
    if (i.isupper()):
        uc_count += 1
    if (i.isdigit()):
        digits_count += 1

print("\n")
print("No. of lower case letters in given file is", lc_count)
print("No. of upper case letters in given file is", uc_count)
print("No. of digits in given file is", digits_count)

file.close()

