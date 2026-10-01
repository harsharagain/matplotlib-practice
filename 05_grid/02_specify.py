# Use `axis` parameter in the grid() function to specify which grid lines to display

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 8, 2, 5]

plt.plot(x, y)

plt.grid(axis='x')

plt.savefig("02_specify.png")