import matplotlib.pyplot as plt

# Generate some data to plot
labels = ['A', 'B', 'C', 'D', 'E']
data = [20, 25, 15, 10, 30]

# Plot the pie chart
plt.pie(data, labels=labels, autopct='%1.1f%%')

plt.title("Pie Chart")
plt.axis('equal')
plt.show()
