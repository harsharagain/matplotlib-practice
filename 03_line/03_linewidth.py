# linewidth (or) lw to set the width of the line connecting the markers

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 2, 9]

plt.plot(x, y, lw=20) # Set the width of the line to 20
plt.savefig("03_linewidth.png")
