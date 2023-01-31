# create a synthetic dataset (.csv/.xlsx) to work upon and design a python program to read and print that data
import csv

# Create a synthetic dataset and save it to a CSV file
with open('dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["John", 25, "London"])
    writer.writerow(["Jane", 30, "New York"])
    writer.writerow(["Jim", 35, "Paris"])

# Read and print the contents of the CSV file
with open('dataset.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
