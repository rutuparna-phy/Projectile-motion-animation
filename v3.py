import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# User input
v0 = float(input("Enter initial velocity (m/s): "))
angle = float(input("Enter launch angle (degrees): "))

g = 9.8

theta = np.radians(angle)

t = np.linspace(0, 10, 500)

x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

mask = y >= 0
x = x[mask]
y = y[mask]

fig, ax = plt.subplots()

ax.set_xlim(0, max(x) * 1.1)
ax.set_ylim(0, max(y) * 1.1)

ax.set_xlabel("Distance (m)")
ax.set_ylabel("Height (m)")
ax.set_title("Projectile Motion Animation")

line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], 'ro')

def update(frame):
    line.set_data(x[:frame], y[:frame])
    point.set_data([x[frame]], [y[frame]])
    return line, point

ani = FuncAnimation(
    fig,
    update,
    frames=len(x),
    interval=20,
    blit=True
)

plt.grid(True)
plt.show()