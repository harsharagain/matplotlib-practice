# Use `subplot()` function to draw multiple plots in one figure
# `subplot()` function takes three arguments that describes the layout of the figure.
# The layout is organized in rows and columns, which are represented by the first and second argument.
# The third argument represents the index of the current plot.


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 9, 1, 4, 2]

plt.subplot(1, 2, 1)
# The figure has 1 row, 2 columns, and this plot is the first plot.
plt.plot(x, y)

x = [1, 2, 3, 4, 5]
y = [2, 5, 10, 30, 70]

plt.subplot(1, 2, 2)
# The figure has 1 row, 2 columns, and this plot is the second plot.
plt.plot(x, y)

plt.savefig("01_subplot.png")

