import pandas as pd

# creating a small sample CSV to work with 
data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "visitors": [120, 150, 90, 200, 175, 220, 160],
    "sales": [1200, 1450, 980, 1600, 1100, 2000, 1750],
    "store": ["A", "A", "A", "A", "A", "A", "A"],
}
df = pd.DataFrame(data)
df.to_csv("weekly_sales.csv", index=False)

# now load it back in, like you would with any real CSV
df = pd.read_csv("weekly_sales.csv")

print(df.head())       # first 5 rows
print(df.info())       # column types, non-null counts, memory usage
print(df.describe())   # summary stats for numeric columns
print(df.shape)         # (rows, columns)
print(df.columns)       # column names