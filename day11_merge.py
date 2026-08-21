import pandas as pd

# two related tables — sales data, and store info that doesn't repeat every row
sales = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "store_id": ["A", "B", "A", "B", "A"],
    "sales": [1200, 980, 1450, 1600, 1100],
})

stores = pd.DataFrame({
    "store_id": ["A", "B", "C"],
    "manager": ["Priya", "Jordan", "Sam"],
    "city": ["Edmonton", "Calgary", "Toronto"],
})

# merge — like a SQL join, combine on a shared column
merged = pd.merge(sales, stores, on="store_id")
print(merged)

# merge, but keep every row from the left table even without a match
left_merged = pd.merge(sales, stores, on="store_id", how="left")
print(left_merged)

# merge, but keep every row from both, even unmatched (store C has no sales rows)
outer_merged = pd.merge(sales, stores, on="store_id", how="outer")
print(outer_merged)

# concat — stack tables on top of each other (same columns, more rows)
more_sales = pd.DataFrame({
    "day": ["Sat", "Sun"],
    "store_id": ["A", "B"],
    "sales": [2000, 1750],
})
all_sales = pd.concat([sales, more_sales], ignore_index=True)
print(all_sales)