import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
v0 = 20          # m/s
angle = 45       # degrees
g = 9.8          # m/s²

# Convert angle to radians
theta = np.radians(angle)

# Time values
t = np.linspace(0, 3, 100)

# Projectile equations
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Plot
plt.plot(x, y)

plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.title("Projectile Motion")

plt.grid(True)

plt.show()