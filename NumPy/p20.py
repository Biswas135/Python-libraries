# Shuffle array
import numpy as np

# Create a random number generator
rng = np.random.default_rng()

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Shuffle the array elements **in place**
# Meaning the original array gets rearranged
rng.shuffle(array)

# Print the shuffled array
print(array)
