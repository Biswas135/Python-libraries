# Random Number-1:
import numpy as np 

# Create a random number generator using the newer recommended method
rng = np.random.default_rng()

# Generate a single random integer from 1 to 6 (7 is excluded)
print(rng.integers(1, 7))

# Generate 3 random integers from 1 to 100
print(rng.integers(low=1, high=101, size=3))

# Generate a 3x2 matrix of random integers from 1 to 100
print(rng.integers(low=1, high=101, size=(3, 2)))
