#Broadcasting -1
import numpy as np 

array1 = np.array([[1,2,3,4]])   # shape (1, 4)
array2 = np.array([[1],[2],[3],[4]])  # shape (4, 1)

print(array1.shape)
print(array2.shape)

print(array1 * array2)
