# Assign a specific color for each dot by using an array of colors as value for the c argument (or) color

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
colors = ["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"]

plt.scatter(x, y, c=colors)

plt.savefig("04_color_each_dot.png")