import numpy as np  # Importing the NumPy library

my_list = [1, 2, 3, 4]  # Creating a Python list
print(my_list)  # Printing the original list

my_list1 = my_list * 2  # Repeating the list (not multiplying elements)
print(my_list1)  # Prints [1, 2, 3, 4, 1, 2, 3, 4]

# If you want to multiply each element by 2, use NumPy:
my_array = np.array(my_list)  # Convert list to NumPy array

print(type(my_array)) #<class 'numpy.ndarray'>
my_array1 = my_array * 2  # Multiply each element by 2
print(my_array1)  # Prints [2 4 6 8]
