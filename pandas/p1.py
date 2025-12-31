# Importing pandas library
import pandas as pd

# Creating a series using a list of integers
data1 = [100, 102, 104]
series1 = pd.Series(data1)
print(series1)

# Creating a series using a list of floating-point numbers
data2 = [100.2, 100.3, 1004.3]
series2 = pd.Series(data2)
print(series2)

# Creating a series using a list of strings
data3 = ["A", "B", "C"]
series3 = pd.Series(data3)
print(series3)

# Creating a series using a list of boolean values
data4 = [True, False, True]
series4 = pd.Series(data4)
print(series4)
