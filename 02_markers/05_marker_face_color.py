# Setting the color of the marker (points) in the plot
# markerfacecolor (or) mfc parameter is used to set the color of the marker in the plot.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 8, 9]

plt.plot(x, y, marker='o', mfc='y')
plt.savefig("05_marker_face_color.png")