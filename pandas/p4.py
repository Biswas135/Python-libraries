# Using Dictionaries to create a Pandas Series

import pandas as pd

# Creating a dictionary where keys become index and values become data
calories = {
    "Day1": 1750,
    "Day2": 2100,
    "Day3": 1700
}

# Converting dictionary to Series
series = pd.Series(calories)
print(series)  # Printing the whole Series

# In order to print specific value and edit it
series.loc["Day3"] += 500  # Increasing Day3 calories by 500
print(series.loc["Day3"])  # Printing updated value for Day3
