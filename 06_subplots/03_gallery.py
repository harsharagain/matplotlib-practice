import matplotlib.pyplot as plt

y = [4, 9, 2, 4, 8]
plt.subplot(3, 3, 1)
plt.plot(y)

y = [2, 4, 6, 8, 10]
plt.subplot(3, 3, 2)
plt.plot(y)

y = [50, 10, 30, 40, 50]
plt.subplot(3, 3, 3)
plt.plot(y)

y = [24, 12, 4, 6, 8]
plt.subplot(3, 3, 4)
plt.plot(y)

y = [2, 6, 7, 2, 4]
plt.subplot(3, 3, 5)
plt.plot(y)

y = [92, 34, 56, 87, 43]
plt.subplot(3, 3, 6)
plt.plot(y)

plt.savefig("03_gallery.png")