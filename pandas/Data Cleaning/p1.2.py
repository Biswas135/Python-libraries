# Data Cleaning:

import pandas as pd

# Loading CSV file into 3 separate DataFrames for different operations
df = pd.read_csv("people-100.csv")
df2 = pd.read_csv("people-100.csv")
df3 = pd.read_csv("people-100.csv")


# 3 - Fix Inconsistent Values
# Replacing variations to maintain consistency in 'Sex' column
df["Sex"] = df["Sex"].replace({
    "Male": "MALE",
    "Female": "FEMALE"
})
print(df.to_string())


# 4 - Standardize Text
# Converting all First Name values to lowercase for uniformity
df2["First Name"] = df2["First Name"].str.lower()
print(df2.to_string())


# 5 - Remove Duplicates
# Removing duplicate rows from dataset
df3 = df3.drop_duplicates()
print(df3.to_string())
