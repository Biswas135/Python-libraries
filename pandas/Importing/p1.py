import pandas as pd

# Reading the CSV file into a DataFrame
df = pd.read_csv("pokemon.csv")

# Print the default view (first 5 & last 5 rows) of the DataFrame
print(df)

# In order to print all data without truncation
# to_string() will display the full DataFrame in the console
print(df.to_string())
