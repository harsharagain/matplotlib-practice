# grid() function to add grid lines to the plot.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 8, 2, 4]

plt.plot(x, y)

plt.grid()

plt.savefig("01_basic.png")