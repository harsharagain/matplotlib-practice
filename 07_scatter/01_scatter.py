# `scatter()` function can be used to draw a scatter plot
# scatter() function plots one dot for each observation

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [4, 9, 1, 2, 5]
plt.scatter(x, y)

plt.savefig("01_scatter.png")
