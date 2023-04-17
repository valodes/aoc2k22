import time
from itertools import product

import numpy as np

t = time.perf_counter()
# -------------------------------------- Input: -------------------------------------- #
lava = np.full((21, 21, 21), False, bool)
for pos in (tuple(map(int, line.split(","))) for line in open("./src/day_18/input.txt")):
    lava[pos] = True
# -------------------------------------- Part 1: ------------------------------------- #
res1 = sum(np.sum(np.diff(lava, 1, dim, False, False)) for dim in [0, 1, 2])
print(f"Result 1: {res1} in {time.perf_counter() - t:.4f} s")

# -------------------------------------- Part 2: ------------------------------------- #
# A position is exposed air if it is NOT lava AND (any of its neighbors are exposed air)
t = time.perf_counter()

# Set array boundary to air (there is no lava outside the range 1-19):
exp_air = np.full_like(lava, True, bool)
exp_air[1:-1, 1:-1, 1:-1] = False

# Check if any neighbors are exposed. Repeat until the resulting array doesn't change:
prev = 0
while prev != (s := exp_air.sum()):
    prev = s
    neighbors = [np.roll(exp_air, dir, ax) for dir, ax in product([1, -1], [0, 1, 2])]
    exp_air = ~lava & np.any(neighbors, axis=0)
# Same calculation as part 1, but this time enclosed air is treated as lava.
res2 = sum(np.sum(np.diff(~exp_air, 1, dim, False, False)) for dim in [0, 1, 2])
print(f"Result 2: {res2} in {time.perf_counter() - t:.4f} s")