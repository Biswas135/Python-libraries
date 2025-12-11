import numpy as np

# Creating a 2x8 NumPy array of ages
ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,20,21,25]])  # both rows have 8 elements

# Filter ages less than 18 → teenagers
teenagers = ages[ages < 18]
print(teenagers)  # [17 16 15]

# Filter ages between 18 (inclusive) and 65 (exclusive) → adults
adults = ages[(ages >= 18) & (ages < 65)]
print(adults)  # [21 19 20 30 18 39 22 18 20 21 25]

# Filter ages 65 or older → seniors
seniors = ages[ages >= 65]
print(seniors)  # [65 99]

# Filter even ages
evens = ages[ages % 2 == 0]
print(evens)  # [20 16 30 18 22 18 20]

# Filter odd ages
odds = ages[ages % 2 != 0]   # Use != instead of !==
print(odds)  # [21 17 19 39 15 65 99 21 25]
