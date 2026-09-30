# Marker Edge 
# markeredgecolor (or) mec to set the color of the edge of the markers

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 8, 9]

plt.plot(x, y, marker='o', mec='r')
plt.savefig("06_marker_edge_color.png")