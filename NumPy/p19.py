# Floating Point Numbers:
import numpy as np

# Generate a random floating-point number between 0 and 1
print(np.random.uniform())

# Generate a random floating-point number between -1 and 1
print(np.random.uniform(low=-1, high=1))

# Generate 3 random floating-point numbers between -1 and 1
print(np.random.uniform(low=-1, high=1, size=3))

# Generate a 3x2 matrix of random floating-point numbers between -1 and 1
print(np.random.uniform(low=-1, high=1, size=(3, 2)))
