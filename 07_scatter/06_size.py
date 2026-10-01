# To change the size of the each dots use `s`` argument.

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
sizes = [20,50,100,200,500,1000,60,90,10,300,600,800,75]

plt.scatter(x, y, s=sizes)
plt.savefig("06_size.png")
