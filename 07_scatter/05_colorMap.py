# A colormap is like a list of colors, where each color has a value that ranges from 0 to 100
# Specify the colormap with the keyword argument `cmap`` with the value of the colormap.
# In this case 'viridis' which is one of the built-in colormaps available in Matplotlib.

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

colors = [0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100]

plt.scatter(x, y, c=colors, cmap='viridis')

# To include the colormap in the drawing, use the `plt.colorbar()` statement
plt.colorbar()
# If bar is not required, you can just remove the statement

plt.savefig("05_colorMap.png")

# Reference: https://matplotlib.org/stable/gallery/color/colormap_reference.html