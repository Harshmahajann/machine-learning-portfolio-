import pandas as pd

df = pd.read_csv("weekly_sales.csv")

# .loc — select by label (column names, row index labels)
print(df.loc[0])                      # entire first row
print(df.loc[:, "sales"])             # entire sales column
print(df.loc[0:2, ["day", "sales"]])  # rows 0-2, only day and sales columns

# .iloc — select by position (integer index, ignores labels)
print(df.iloc[0])          # first row, by position
print(df.iloc[0:3])        # first 3 rows
print(df.iloc[:, 1])       # second column, by position

# boolean filtering — the pattern you already know from NumPy masking
high_sales = df[df["sales"] > 1400]
print(high_sales)

# multiple conditions — & for AND, | for OR, each condition in its own ()
busy_and_profitable = df[(df["visitors"] > 150) & (df["sales"] > 1400)]
print(busy_and_profitable)

# filter, then pick specific columns
print(df.loc[df["sales"] > 1400, ["day", "sales"]])