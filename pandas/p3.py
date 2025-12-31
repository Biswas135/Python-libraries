# Series filter

# Importing pandas library
import pandas as pd

# Creating a Series with custom index values
data = [100, 101, 102, 202, 209]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])

# Filtering values that are greater than or equal to 200
print(series[series >= 200])   # Output will show only 202 and 209
