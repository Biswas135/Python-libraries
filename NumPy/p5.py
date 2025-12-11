# scalar arithmetic with NumPy arrays
import numpy as np

array = np.array([1, 2, 3])  # create a 1D NumPy array

print(array + 1)  # add 1 to each element → [2, 3, 4]
print(array - 2)  # subtract 2 from each element → [-1, 0, 1]
print(array * 3)  # multiply each element by 3 → [3, 6, 9]
print(array ** 5) # raise each element to the power of 5 → [1, 32, 243]
