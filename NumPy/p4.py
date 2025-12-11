import numpy as np

# Create a 4x4 2D NumPy array
array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Select the first row (row index 0)
print(array[0])  # Output: [1 2 3 4]

# Select rows from index 1 to 3 (4 is excluded)
print(array[1:4])  
# Output:
# [[ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]

# Select every 2nd row from index 0 to 3
print(array[0:4:2])  
# Output:
# [[ 1  2  3  4]
#  [ 9 10 11 12]]

# Reverse the rows of the array
print(array[::-1])  
# Output:
# [[13 14 15 16]
#  [ 9 10 11 12]
#  [ 5  6  7  8]
#  [ 1  2  3  4]]

# Rows:

# Select all rows, column 0
print(array[:, 0])  # Output: [ 1  5  9 13]

# Select all rows, column 1
print(array[:, 1])  # Output: [ 2  6 10 14]

# Select all rows, columns 0 to 2 (2 is excluded)
print(array[:, 0:3])  
# Output:
# [[ 1  2  3]
#  [ 5  6  7]
#  [ 9 10 11]
#  [13 14 15]]

# Select all rows (:) and columns from index 1 to 3 (4 is excluded)
print(array[:, 1:4])  
# Output:
# [[ 2  3  4]
#  [ 6  7  8]
#  [10 11 12]
#  [14 15 16]]
