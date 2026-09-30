# Setting the size of the marker (points) in the plot
# markersize (or) ms parameter is used to set the size of the marker in the plot.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 8, 9]

plt.plot(x, y, marker='o', ms=15)
plt.savefig("04_marker_size.png")
