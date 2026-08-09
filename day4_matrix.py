import numpy as np

sales = np.array([1200, 1450, 980, 1600, 1100, 2000, 1750])

# reshape — same data, different shape
reshaped = sales.reshape(7, 1)      # turn the 7-element row into a 7x1 column
print(reshaped.shape)                # (7, 1)

# transpose — flip rows and columns
combined = np.array([
    [1200, 1450, 980, 1600, 1100, 2000, 1750],   # store A
    [900, 1100, 1050, 1400, 1300, 1800, 1600],   # store B
])
print(combined.shape)          # (2, 7) -> 2 stores, 7 days
print(combined.T.shape)        # (7, 2) -> transposed: 7 days, 2 stores

# dot product on two 1D arrays — weighted sum in one line
quantities = np.array([10, 5, 8, 12, 6, 15, 9])     # units sold each day
prices = np.array([25, 30, 20, 22, 28, 18, 24])     # price per unit that day

total_revenue = np.dot(quantities, prices)
print(total_revenue)   # one number: (qty*price) for each day, summed

# dot product on a matrix — same idea, but for every store at once
store_quantities = np.array([
    [10, 5, 8, 12, 6, 15, 9],    # store A daily units
    [8, 6, 7, 10, 9, 14, 11],    # store B daily units
])   # shape (2, 7)

weekly_revenue_per_store = store_quantities.dot(prices)   # shape (2,)
print(weekly_revenue_per_store)   # one total per store, computed together