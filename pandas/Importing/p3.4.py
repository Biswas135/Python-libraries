# Simple Exercise: User types a Pokémon name and it prints the data if it exists

import pandas as pd

# Read CSV and set 'Name' column as index
df = pd.read_csv("pokemon.csv", index_col="Name")

# Take input from user
pokemon = input("Enter a Pokémon Name: ")

# Try to access the Pokémon data
try:
    print(df.loc[pokemon])  # Print the row corresponding to the Pokémon name

except KeyError:
    # If the Pokémon name does not exist in the index, catch the error
    print(f"{pokemon} not found")
