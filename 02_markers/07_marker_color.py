# markeredgecolor (mec) and markerfacecolor (mfc) both combined

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 8, 9]

plt.plot(x, y, marker='o', mfc='y', mec='r', ms=20)
plt.savefig("07_marker_color.png")

# Hexadecimal color values can also be used to set the color