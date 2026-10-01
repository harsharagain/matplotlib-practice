# Use the loc paramter in title() to position the title
# Legal values are: 'left', 'right', and 'center'
# Default value is 'center'

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 2, 7, 1]

#
plt.title("Data", loc='left')

font1 = { 'family':'serif', 'color':'blue', 'size': 15}
font2 = {'family':'serif', 'color':'hotpink', 'size': 20}
plt.plot(x, y, color='red', marker='o')
plt.xlabel("X-Axis", fontdict=font1)
plt.ylabel("Y-Axis", fontdict=font2)


plt.savefig("03_position_title.png")
