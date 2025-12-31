# Data Cleaning:

import pandas as pd

# Reading the CSV file
df = pd.read_csv("people-100.csv")


# 1 - Drop Irrelevant Columns
# Removing unwanted columns ('Sex' & 'Date of birth') from DataFrame
df1 = df.drop(columns=["Sex", "Date of birth"])
print(df1.to_string())     # Print full table without cutting rows


# 2 - Handle Missing Data (Print only non-missing values)
# dropna(subset=["Email"]) removes rows where Email is missing (NaN)
df2 = df.dropna(subset=["Email"])
print(df2.to_string())


# 3 - Handle Missing Data (Replace NA with custom value)
# fillna({"Email": "None"}) will replace all missing email values with "None"
df3 = df.fillna({"Email": "None"})
print(df3.to_string())
