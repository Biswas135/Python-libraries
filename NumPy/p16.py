# Filtering-2 (using np.where)
# Preserves the original shape of the array
import numpy as np

# Creating a 2x8 NumPy array of ages
ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,20,21,25]]) 

# Use np.where to filter adults (ages >= 18)
# If condition is True → keep the value, else → replace with 0
adults = np.where(ages >= 18, ages, 0)

# Print the result
print(adults)
