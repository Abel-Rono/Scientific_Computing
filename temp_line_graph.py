import matplotlib.pyplot as plt

temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

plt.plot(days, temperatures, marker='o', linewidth=1.5, markersize=5, color='blue')

plt.title('Weekly Temperature Readings', fontsize=12, fontweight='bold')
plt.xlabel('Day of the Week', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True)

plt.show()