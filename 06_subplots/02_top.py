# On top of each other

import matplotlib.pyplot as plt

y = [2, 4, 6, 8, 10]
plt.subplot(2, 1, 1)
# The figure has 2 row, 1 columns, and this plot is the first plot.
plt.plot(y)

y = [3, 9, 1, 4 , 8]
plt.subplot(2, 1, 2)
# The figure has 2 row, 1 columns, and this plot is the second plot.
plt.plot(y)

plt.savefig("02_top.png")