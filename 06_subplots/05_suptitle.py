# Super Title
# `suptitle()` function can be used to add a title to the entire figure

import matplotlib.pyplot as plt

y = [2, 9, 3, 6, 1]
plt.subplot(1, 2, 1)
plt.plot(y)
plt.title("Graph-1")

y = [2, 4, 6, 8, 10]
plt.subplot(1, 2, 2)
plt.plot(y)
plt.title("Graph-2")

plt.suptitle("GRAPHS")
plt.savefig("05_suptitle.png")