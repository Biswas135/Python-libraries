# Aggregate Function Example-2
import numpy as np

# Creating a 2x5 NumPy array
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

# Sum of elements **column-wise** (axis=0)
# Adds elements along each column: [1+6, 2+7, 3+8, 4+9, 5+10]
print(np.sum(array, axis=0))  # Output: [ 7  9 11 13 15]

# Sum of elements **row-wise** (axis=1)
# Adds elements along each row: [1+2+3+4+5, 6+7+8+9+10]
print(np.sum(array, axis=1))  # Output: [15 40]
