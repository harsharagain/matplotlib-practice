# fontdict parameter in xlabel(), ylabel(), title() allows you to set font properties

import matplotlib.pyplot as plt

x =  [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
y = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

font1 = {'family':'serif', 'color': 'blue', 'size': 20}
font2 = {'family':'serif', 'color': 'red', 'size': 25}

plt.plot(x, y)
plt.xlabel('Average Pulse', fontdict=font1)
plt.ylabel("Calorie Burnage", fontdict=font2)

plt.savefig("02_set_font.png")