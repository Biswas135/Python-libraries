# Random Number -2
#seed
import numpy as np

# Create a random number generator with a fixed seed
# seed=2 → results will always be the same every time you run this code
rng = np.random.default_rng(seed=2)

# Generate random integers from 1 to 100
# size=(3,2) → creates a 3x2 matrix
print(rng.integers(low=1, high=101, size=(3, 2)))
