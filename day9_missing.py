import pandas as pd
import numpy as np

# build a dataset with some missing values on purpose, to practice on
data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "visitors": [120, 150, np.nan, 200, 175, np.nan, 160],
    "sales": [1200, np.nan, 980, 1600, 1100, 2000, 1750],
    "store": ["A", "A", "A", "A", "A", "A", "A"],
}
df = pd.DataFrame(data)

# isna / notna — find where the missing values are
print(df.isna())              # True/False grid, same shape as df
print(df.isna().sum())        # count of missing values per column

# dropna — remove rows that have any missing value
dropped = df.dropna()
print(dropped)

# dropna on one specific column only
dropped_sales = df.dropna(subset=["sales"])
print(dropped_sales)

# fillna — fill instead of dropping
filled_zero = df.fillna(0)
print(filled_zero)

# fillna with the column's mean — more realistic than 0 for numeric data
filled_mean = df.copy()
filled_mean["visitors"] = filled_mean["visitors"].fillna(filled_mean["visitors"].mean())
filled_mean["sales"] = filled_mean["sales"].fillna(filled_mean["sales"].mean())
print(filled_mean)

# check and fix data types
print(df.dtypes)
df["visitors"] = df["visitors"].astype("Int64")   # nullable integer type — allows NaN, unlike plain int
print(df.dtypes)