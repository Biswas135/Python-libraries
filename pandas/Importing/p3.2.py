# Selection of data by Row using custom index

import pandas as pd

# Reading CSV file and setting 'Name' column as index
df = pd.read_csv("pokemon.csv", index_col="Name")


# SELECTION BY ROW using row label (Name)
# Select all data for "Pikachu"
print(df.loc["Pikachu"])


# SELECTION BY ROW AND SPECIFIC COLUMNS
# Select only "Total" and "Speed" for "Pikachu"
print(df.loc["Pikachu", ["Total", "Speed"]])


# SELECTION OF MULTIPLE ROWS using slicing
# Rows from "Ivysaur" to "Charmeleon" (inclusive) for columns "Total" and "Speed"
print(df.loc["Ivysaur":"Charmeleon", ["Total", "Speed"]])
