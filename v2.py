import numpy as np
import matplotlib.pyplot as plt

# User input
v0 = float(input("Enter initial velocity (m/s): "))
angle = float(input("Enter launch angle (degrees): "))

g = 9.8

# Convert angle to radians
theta = np.radians(angle)

# Time values
t = np.linspace(0, 10, 500)

# Equations
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Remove points below ground
mask = y >= 0
x = x[mask]
y = y[mask]

# Plot
plt.plot(x, y)

plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.title("Projectile Motion")

plt.grid(True)
plt.show()