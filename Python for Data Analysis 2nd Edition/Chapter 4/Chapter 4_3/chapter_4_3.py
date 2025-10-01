
# 4.3 Array-Oriented Programming with Arrays

import numpy as np
import matplotlib.pyplot as plt

# In general, vectorized array operations will often be one or two (or more) orders
# of magnitude faster than their pure Python equivalents, with the biggest impact in
# any kind of numerical computations.

points = np.arange(-5, 5, 0.01) # 1000 equally spaced points

xs, ys = np.meshgrid(points, points)

print(ys)

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()