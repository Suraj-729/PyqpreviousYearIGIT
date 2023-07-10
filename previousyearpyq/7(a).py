import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 5, 6, 7, 9, 9, 10, 12, 13, 14, 15, 16, 18, 17, 21, 22])
y = np.array([100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100])

degree = 3  # Set the degree of the polynomial
coefficients = np.polyfit(X, y, degree)
polynomial_func = np.poly1d(coefficients)

x_values = np.linspace(X.min(), X.max(), 100)

plt.scatter(X, y, color='blue', label='Data')
plt.plot(x_values, polynomial_func(x_values), color='red', label='Polynomial Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
