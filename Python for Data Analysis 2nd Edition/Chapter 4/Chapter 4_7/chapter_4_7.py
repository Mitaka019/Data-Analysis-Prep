
# 4.7 Example: Random Walks

import numpy as np
import random
import matplotlib.pyplot as plt

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:100])
plt.show()

nsteps = 1000
draws = np.random.randint(0, 2, size = nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

print(walk.min())
print(walk.max())

print((np.abs(walk) >= 10).argmax())

# Simulating Many Random Walks at Once

# If your goal was to simulate many random walks, say 5,000 of them, you can generate
# all of the random walks with minor modifications to the preceding code.

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(walks)

print(walks.max())
print(walks.min())

# Out of these walks, let’s compute the minimum crossing time to 30 or –30.

hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)

print(hits30.sum()) # Number that hit 30 or -30

# We can use this boolean array to select out the rows of walks that actually cross the
# absolute 30 level and call argmax across axis 1 to get the crossing times:

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crossing_times.mean())

