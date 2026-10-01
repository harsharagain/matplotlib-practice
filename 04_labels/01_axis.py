# set the axis labels
# xlabel() and ylabel() functions to set a label for the x- and y-axis.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 8, 9]

plt.plot(x, y)

plt.title("Data")
plt.xlabel("axis of x")
plt.ylabel("axis of y")

plt.savefig("01_axis.png")