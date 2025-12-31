# Aggregation Functions in Pandas

import pandas as pd

# Read CSV file
df = pd.read_csv("pokemon.csv")


# 1 - Mean of "Total" column
print(df["Total"].mean())   # Average Total value of all Pokémon


# 2 - Sum of all numeric columns
print(df.sum(numeric_only=True))  # Adds values of all numeric columns


# 3 - Minimum value of all numeric columns
print(df.min(numeric_only=True))  # Finds minimum in each numeric column


# 4 - Maximum value of all numeric columns
print(df.max(numeric_only=True))  # Finds maximum in each numeric column


# 5 - Count of non-null values in each numeric column
print(df.count(numeric_only=True))  # Counts values ignoring NaN
