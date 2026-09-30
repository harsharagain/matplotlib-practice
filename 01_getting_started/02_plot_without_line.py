# Plotting without line

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 8, 9]

plt.plot(x, y, "o") 
# The marker parameter is used to specify the shape of the markers that will be drawn at each data point. 
# In this case, "o" indicates that circular markers will be used.

plt.show()