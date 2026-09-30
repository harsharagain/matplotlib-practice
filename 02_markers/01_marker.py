import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 8, 9]

# Mark each point with a circle (along with line)
plt.plot(x, y, marker="o")
# For without line, we can use "o" as the third parameter in the plot() function.

plt.savefig("01_marker.png")