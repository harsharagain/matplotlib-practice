# Format Strings **fmt**

# The format string is a convenient way to define basic formatting like marker, line style and color
# The format string is specified in the third parameter of the plot() function.
# marker|line|color

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 8, 9]

plt.plot(x, y, 's-b') # Square markers, blue line

plt.savefig("03_format_strings.png")

# Marker Reference: https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
# Line Reference: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html#sphx-glr-gallery-lines-bars-and-markers-linestyles-py
# Color Reference: https://matplotlib.org/stable/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py
# https://www.w3schools.com/python/matplotlib_markers.asp


