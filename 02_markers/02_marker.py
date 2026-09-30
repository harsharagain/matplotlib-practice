import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 8, 9]

plt.plot(x, y, marker='*')  
# Mark each point with a star (along with line)
plt.savefig("02_marker.png")

#Marker Reference: https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers