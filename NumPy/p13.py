# Aggregate Function Example-1
import numpy as np

# Creating a 2x5 NumPy array
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

# Sum of all elements
print(np.sum(array))      # 55

# Mean (average) of all elements
print(np.mean(array))     # 5.5

# Standard deviation of all elements
print(np.std(array))      # 2.8722813232690143

# Variance of all elements
print(np.var(array))      # 8.25

# Minimum value in the array
print(np.min(array))      # 1

# Maximum value in the array
print(np.max(array))      # 10

# Index of the minimum value (in flattened array)
print(np.argmin(array))   # 0

# Index of the maximum value (in flattened array)
print(np.argmax(array))   # 9
