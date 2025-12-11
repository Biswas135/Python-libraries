#Calculate the area of circles corresponding to each radius using NumPy.”
 
# import NumPy library for numerical operations
import numpy as np  

# create a NumPy array containing radii of circles
radii = np.array([1, 2, 3])  

# calculate area of each circle using the formula π * r^2
# np.pi gives the value of π, radii**2 squares each radius
print(np.pi * radii**2)  # output → [ 3.14159265 12.56637061 28.27433388 ]
