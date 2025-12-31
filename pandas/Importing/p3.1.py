# Selection of data by Row

import pandas as pd

# Reading the CSV file into a DataFrame
df = pd.read_csv("pokemon.csv")


# SELECTION BY ROW using index label with loc
# loc[0] selects the first row (row with index 0)
print(df.loc[0])
