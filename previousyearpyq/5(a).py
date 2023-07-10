import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

X = np.array(input("Enter the input data (X): ").split(), dtype=float)
y = np.array(input("Enter the output data (y): ").split(), dtype=float)

slope, intercept, r_value, p_value, std_err = linregress(X, y)
line = slope * X + intercept

plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, line, color='red', label='Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
