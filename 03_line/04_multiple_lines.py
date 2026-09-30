# plot more lines using multiple plot() functions

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 5, 7, 2, 9]
y2 = [1, 4, 6, 7, 2]

plt.plot(x, y1, color='b')
plt.plot(x, y2, color='y')

plt.savefig("04_multiple_lines.png")