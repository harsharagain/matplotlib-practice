# linestyle (or) ls to set the style of the line connecting the markers

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 8, 9]

plt.plot(x,y, ls="dotted")
plt.savefig("01_linestyle.png")


# dotted can be written as :
# dashed can be written as --
# solid can be written as -