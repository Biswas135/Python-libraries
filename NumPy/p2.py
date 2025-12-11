#Dimensional In NUmpy
import numpy as np

array = np.array('A')
print(array.ndim)  # Output: 0



array1 = np.array(['A', 'B', 'C'])
print(array1.ndim)  # Output: 1


array2 = np.array([
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I']
])
print(array2.ndim)  # Output: 2
print(array2.shape)

array3 = np.array([
    [['A','B','C'], ['D','E','F'], ['G','H','I']],
    [['J','K','L'], ['M','N','O'], ['P','Q','R']],
    [['S','T','U'], ['V','W','X'], ['Y','Z',' ']]
])
print(array3.ndim)  # Output: 3

print(array3.shape)