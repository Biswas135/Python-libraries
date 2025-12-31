# Aggregation Functions for Single Column

import pandas as pd

# Read CSV file
df = pd.read_csv("pokemon.csv")


# 1 - Mean of "Total" column
print(df["Total"].mean())   # Average Total value of all Pokémon


# 2 - Sum of "Speed" column
print(df["Speed"].sum())    # Adds all Speed values of Pokémon


# 3 - Count of non-null values in "Name" column
print(df["Name"].count())   # Counts how many Pokémon names exist (ignores missing values)
