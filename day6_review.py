import numpy as np

np.random.seed(1)

# 1. RANDOM (day 5) — simulate a month instead of a week
daily_sales = np.random.randint(800, 2200, size=30)
print("30 days of sales:", daily_sales)
 
# 2. INDEXING/SLICING (day 2) — first week vs last week
first_week = daily_sales[:7]
last_week = daily_sales[-7:]
print("First week:", first_week)
print("Last week:", last_week)

# 3. BOOLEAN MASKING (day 2) — which days were "good" (above overall average)
good_days = daily_sales > daily_sales.mean()
print("Number of good days:", good_days.sum())   # True counts as 1, so sum() = count

# 4. BROADCASTING (day 3) — apply a 10% discount promo to the whole month
discounted = daily_sales * 0.9
print("After discount:", discounted.round(2))

# 5. RESHAPE (day 4) — reshape 30 days into 6 weeks x 5 days
weekly = daily_sales.reshape(6, 5)
print("Reshaped into weeks:\n", weekly)

# 6. MATRIX OPS (day 4) — total per week using axis-based sum
weekly_totals = weekly.sum(axis=1)
print("Total per week:", weekly_totals)

# 7. DOT PRODUCT (day 4) — if each day had a different profit margin
margins = np.random.uniform(0.1, 0.3, size=30)   # random margin between 10-30%
total_profit = np.dot(daily_sales, margins)
print("Estimated total profit:", round(total_profit, 2))