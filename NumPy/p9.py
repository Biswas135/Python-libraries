# Comparison operators using NumPy
import numpy as np

# create a NumPy array of scores
scores = np.array([91, 55, 100, 73, 82, 64])

# check which scores are exactly 100 → returns a boolean array
print(scores == 100)  # [False  False  True  False  False  False]

# check which scores are less than 60 → returns a boolean array
print(scores < 60)    # [False  True  False  False  False  False]

# Replace scores less than 60 with 0
scores[scores < 60] = 0  # select elements < 60 and assign 0

# print updated array
print(scores)  # [91  0 100 73 82 64]
