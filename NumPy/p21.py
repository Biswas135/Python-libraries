# Choice Array
import numpy as np

# Create a random number generator
rng = np.random.default_rng()

# Create an array of fruit names
fruits = np.array(["Apple", "Banana", "Kiwi", "Pineapple","Mango"])

# Randomly select 3 items from the array
# size=3 → choose 3 fruits
# By default: selection is WITH replacement (items can repeat)
fruits = rng.choice(fruits, size=3)

# Print the selected fruits
print(fruits)
