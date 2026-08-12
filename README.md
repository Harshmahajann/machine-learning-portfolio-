# Week 1 — NumPy

Five days building the foundation for everything else in this plan: arrays, indexing, broadcasting, matrix operations, and simulating data.

## What's in here

| `day1_arrays.py` | Creating arrays, basic math operations |
| `day2_indexing.py` | Indexing, slicing, boolean masking, fancy indexing |
| `day3_broadcasting.py` | Broadcasting scalars/arrays, vectorized speed vs loops |
| `day4_matrix.py` | Reshape, transpose, dot product |
| `day5_random.py` | Random arrays, seeding, simulating data |

## Key takeaways

- NumPy does math on entire arrays at once instead of looping — dramatically faster, and the foundation pandas and every ML model sit on top of.
- Boolean masking (`array[array > x]`) is the most-reused pattern here — it's exactly how filtering works in pandas next week.
- Broadcasting applies an operation across mismatched shapes automatically — this is how feature scaling works in ML.
- The dot product (`np.dot`) is literally the math behind a linear model's prediction — comes back in Week 6.

## Next: Week 2 — Pandas
