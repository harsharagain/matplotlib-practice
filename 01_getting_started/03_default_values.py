# Plotting with default values
# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.

import matplotlib.pyplot as plt

y = [2, 5, 1, 3, 10]

plt.plot(y)

plt.show()