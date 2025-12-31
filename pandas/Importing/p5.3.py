# Group By Function in Pandas

import pandas as pd

# Read CSV file
df = pd.read_csv("pokemon.csv")


# Group Pokémon by "Type 1"
group = df.groupby("Type 1")


# 1 - Mean of "Total" for each Type 1
print(group["Total"].mean())   # Average Total for Pokémon of each Type 1


# 2 - Sum of "Total" for each Type 1
print(group["Total"].sum())    # Adds Total values for each Type 1


# 3 - Count of Pokémon for each Type 1
print(group["Total"].count())  # Counts how many Pokémon are in each Type 1
