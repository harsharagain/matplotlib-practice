import matplotlib.pyplot as plt

x = [0, 2, 4, 6, 8]
y = [2, 5, 7, 8, 9]

# plot() function is used to draw points (markers) in a diagram.
plt.plot(x, y)
# Parameter 1 is an array of x values
# Parameter 2 is an array of y values
# The plot function will create a line plot connecting the points defined by these x and y coordinates.
plt.show()