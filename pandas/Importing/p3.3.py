# Selection of data by Row using integer indexing (iloc)

import pandas as pd

# Reading CSV file and setting 'Name' column as index
df = pd.read_csv("pokemon.csv", index_col="Name")


# 1 - Selection of multiple rows using integer indexing
# Select rows from position 0 to 10 (iloc is exclusive of stop index 11)
print(df.iloc[0:11])


# 2 - Selection of multiple rows using step
# Select rows from position 0 to 10, taking every 2nd row
print(df.iloc[0:11:2])


# 3 - Selection of rows AND columns using integer indexing
# Select rows 0 to 10 and columns 0 to 2 (first three columns)
print(df.iloc[0:11, 0:3])
