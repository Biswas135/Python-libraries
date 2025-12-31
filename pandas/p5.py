# Data Frames:

import pandas as pd

# Creating a DataFrame using dictionary (columns as keys & data as list values)
data = {
    "Name": ["Abishek", "Ram", "Sita"],
    "Age": [30, 35, 50]
}
df = pd.DataFrame(data)
print(df)  # Prints the full DataFrame


# We can set our own index in DataFrame by specifying index manually
data1 = {
    "Cartoon": ["Doraemon", "Motu Patlu", "Tom & Jerry"],
    "Origin": ["Japan", "India", "USA"]
}
df1 = pd.DataFrame(data1, index=["A", "B", "C"])
print(df1)  # Prints DataFrame with custom index


# We can access a single row using loc with index name
print(df1.loc["B"])  # Output will show cartoon = Motu Patlu, Origin = India
