import numpy as np
import matplotlib.pyplot as plt

# Generate some data to plot
data = np.random.normal(50, 10, 1000)

# Plot the histogram
plt.hist(data, bins=20, color='blue', edgecolor='black', alpha=0.5)

plt.title("Histogram")
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.show()
