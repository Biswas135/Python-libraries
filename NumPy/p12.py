#broadcasting-3
#Table 
import numpy as np 

array1 = np.array([[1,2,3,4,6,7,8,9,10]])  # shape (1, 9)
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])  # shape (10, 1)

print(array1.shape)
print(array2.shape)

print(array1 * array2)
