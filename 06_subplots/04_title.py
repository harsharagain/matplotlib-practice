# `title()` function can be used to add a title to each plot

import matplotlib.pyplot as plt

y = [2, 4, 6, 8, 10]
plt.subplot(1, 2, 1)
plt.plot(y)
plt.title("Graph-1")

y = [6, 9, 1, 5, 8]
plt.subplot(1, 2, 2)
plt.plot(y)
plt.title("Graph-2")

plt.savefig("04_title.png")


