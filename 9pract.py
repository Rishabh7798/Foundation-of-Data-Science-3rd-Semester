# Design a Python program to implement Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate some data to fit the model
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# Train the linear regression model
model = LinearRegression().fit(x, y)

# Predict the values for the trained model
y_pred = model.predict(x)

# Plot the data and the regression line
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='red')

plt.title("Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
