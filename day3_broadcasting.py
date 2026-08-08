import numpy as np
import time

sales = np.array([1200, 1450, 980, 1600, 1100, 2000, 1750])

# broadcasting a scalar across a whole array
tax_adjusted = sales * 1.05
bonus_days = sales + 100
print(tax_adjusted)
print(bonus_days)

# broadcasting a 1D array across a 2D array
store_a = sales
store_b = np.array([900, 1100, 1050, 1400, 1300, 1800, 1600])
combined = np.array([store_a, store_b])              # shape (2, 7)
daily_target = np.array([1000]*7)                     # shape (7,)

diff_from_target = combined - daily_target
print(diff_from_target)

# vectorized speed vs a loop, on 1 million numbers
big = np.random.randint(0, 100, 1_000_000)

start = time.time()
loop_result = [x * 2 for x in big]
print(f"loop: {time.time() - start:.4f}s")

start = time.time()
vector_result = big * 2
print(f"vectorized: {time.time() - start:.4f}s")
