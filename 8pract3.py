import numpy as np
import matplotlib.pyplot as plt

# Generate some data to plot
labels = ['A', 'B', 'C', 'D', 'E']
data = np.random.randint(0, 100, len(labels))

# Plot the bar plot
plt.bar(labels, data, color='blue')

plt.title("Bar Plot")
plt.xlabel("Labels")
plt.ylabel("Data")
plt.show()
