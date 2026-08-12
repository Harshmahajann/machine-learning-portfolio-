#DAY 2

import numpy as np

sales = np.array([1200, 1450, 980, 1600, 1100, 2000, 1750])
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])



# indexing — single elements
print(sales[0])       # Monday
print(sales[-1])      # Sunday (last element)

# slicing — ranges
print(sales[0:3])     # Mon-Wed
print(sales[3:6])     # Thu-Fri
print(sales[::2])     # every other day

# boolean masking — filter by a condition
mask = sales > 1500
print(mask)            # [False False False True False True True]
print(sales[mask])     # only the days over 1500
print(days[mask])      # which days those were

# fancy indexing — pick specific positions at once
print(sales[[0, 3, 6]])   # Mon, Thu, Sun
print(days[[0, 3, 6]])

# combine both: days that beat the weekly average
print(days[sales > sales.mean()])