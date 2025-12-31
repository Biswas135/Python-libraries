# Selection of column(s) in a DataFrame

import pandas as pd

# Reading the CSV file into a DataFrame
df = pd.read_csv("pokemon.csv")


# SELECTION BY SINGLE COLUMN
# Selecting only the 'Name' column (returns a Series)
print(df["Name"])

# To print all values in the column without truncation
print(df["Name"].to_string())


# SELECTION BY MULTIPLE COLUMNS
# Selecting multiple columns (returns a DataFrame)
# Uncomment to use:
# print(df[["Name", "Total", "HP Attack"]].to_string())
