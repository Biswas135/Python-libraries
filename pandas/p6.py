# DATA Frames:

import pandas as pd

# Creating a DataFrame with custom index
data = {
    "Heroes": ["Ironman", "Spiderman", "Batman"],
    "Ages": [30, 18, 40]
}
df = pd.DataFrame(data, index=["Hero1", "Hero2", "Hero3"])

# ADD a New Column
df["Rate"] = [9, 8, 7]     # Adding new column 'Rate'
print(df)                  # Display updated DataFrame


# Add New Rows
new_rows = pd.DataFrame([
    {"Heroes": "Hulk", "Ages": 28, "Rate": 7},
    {"Heroes": "Thor", "Ages": 40, "Rate": 6.5}
], index=["Hero4", "Hero5"])

# Concatenating original DataFrame with new rows
df1 = pd.concat([df, new_rows])
print(df1)                 # Display final DataFrame
