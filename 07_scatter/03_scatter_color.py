# Use color or c argument to set color for each scatter

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 9, 3, 6, 8]
plt.scatter(x, y, color='hotpink')

x = [1, 2, 3, 4, 5]
y = [5, 8, 1, 5, 4]
plt.scatter(x, y, color='blue')

plt.savefig('03_color.png')

