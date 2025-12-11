# vectorized math functions using NumPy
import numpy as np

array = np.array([9, 16, 25])  # create a 1D array
print(np.sqrt(array))           # compute square root of each element → [3. 4. 5.]

array1 = np.array([1.01, 2.5, 3.99])  
print(np.round(array1))         # round each element to nearest integer → [1. 2. 4.]

array2 = np.array([1.01, 2.5, 3.99])  
print(np.floor(array2))         # round down (floor) each element → [1. 2. 3.]

array3 = np.array([1.01, 2.5, 3.99])  
print(np.ceil(array3))          # round up (ceiling) each element → [2. 3. 4.]

print(np.pi)                    # print the value of pi → 3.141592653589793
