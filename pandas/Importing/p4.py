# Filtering Data in Pandas

import pandas as pd

# Reading the CSV file
df = pd.read_csv("pokemon.csv")


# 1 - Filter Pokémon by Type 1 = "Fire"
Power_pokemon = df[df["Type 1"] == "Fire"]
print(Power_pokemon)


# 2 - Filter Pokémon with Attack >= 90
Attack_Pokemon = df[df["Attack"] >= 90]
print(Attack_Pokemon)


# 3 - Filter Legendary Pokémon (Legendary == True)
Legendary_Pokemon = df[df["Legendary"] == True]
print(Legendary_Pokemon)


# 4 - Filter Pokémon whose Type 1 OR Type 2 is "Water"
Water_Pokemon = df[(df["Type 1"] == "Water") | (df["Type 2"] == "Water")]
print(Water_Pokemon)


# 5 - Filter Pokémon whose Type 1 is "Fire" AND Type 2 is "Flying"
FireFly_Pokemon = df[(df["Type 1"] == "Fire") & (df["Type 2"] == "Flying")]
print(FireFly_Pokemon)
