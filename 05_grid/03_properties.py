# Set the line properties of the grid, like this: 
# grid(color = 'color', linestyle = 'linestyle', linewidth = number)

import matplotlib.pyplot as plt

y = [2, 5, 9, 3, 6]

plt.plot(y)

plt.grid(color='r', linestyle='--', linewidth=0.5)

plt.savefig("03_properties.png")