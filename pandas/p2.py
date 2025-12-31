# Series2

# Importing pandas library
import pandas as pd

# Creating a Series with custom index values
data = ["Abhishek", "Raj", "Gita"]
series = pd.Series(data, index=["Roll.1", "Roll.2", "Roll.3"])
print(series)

# In order to access a specific location using index label
print(series.loc["Roll.1"])   # Output: Abhishek

# In order to change/modify data at a specific index
series.loc["Roll.3"] = "Ram"  # Changing "Gita" to "Ram"
print(series)                 # Updated Series will be printed
