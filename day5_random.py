import numpy as np

# seed makes results reproducible every time you run this
np.random.seed(42)

# random integers - simulate 7 days of store visitor counts
visitors = np.random.randint(50, 200, size=7)
print(visitors)

# random floats between 0 and 1 - simulate a conversion rate per day
conversion_rate = np.random.rand(7)
print(conversion_rate)

# random numbers from a normal (bell curve) distribution
daily_revenue = np.random.normal(loc=1400, scale=300, size=7)
print(daily_revenue.round(2))

# combine two simulated arrays into a third - visitors * conversion = sales
sales_simulated = (visitors * conversion_rate).round().astype(int)
print(sales_simulated)

# shuffle an array
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
shuffled_days = days.copy()
np.random.shuffle(shuffled_days)
print(shuffled_days)

# random sample without repeats
sample = np.random.choice(visitors, size=3, replace=False)
print(sample)