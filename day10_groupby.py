import pandas as pd

data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "store": ["A", "A", "B", "B", "A", "B", "A"],
    "visitors": [120, 150, 90, 200, 175, 220, 160],
    "sales": [1200, 1450, 980, 1600, 1100, 2000, 1750],
}
df = pd.DataFrame(data)

# group by one column, aggregate another
print(df.groupby("store")["sales"].sum())     # total sales per store
print(df.groupby("store")["sales"].mean())    # average sales per store

# multiple aggregations at once
print(df.groupby("store")["sales"].agg(["sum", "mean", "max", "min"]))

# group by, aggregate multiple different columns
print(df.groupby("store").agg({
    "sales": "sum",
    "visitors": "mean"
}))

# group by, then reset back into a normal flat table
summary = df.groupby("store")["sales"].sum().reset_index()
print(summary)

# group by and count rows per group
print(df.groupby("store").size())