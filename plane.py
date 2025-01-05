import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
v = np.array([1, 0, 1])
w = np.array([1, 1, -1])
normal = np.cross(v, w)  # Normal vector

# Create a grid of points for the plane
xx, yy = np.meshgrid(np.linspace(-2, 2, 50), np.linspace(-2, 2, 50))

zz = (-normal[0] * xx - normal[1] * yy) / normal[2]  # Solve for z

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='blue')

# Plot the vectors
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='red', label='v')
ax.quiver(0, 0, 0, w[0], w[1], w[2], color='green', label='w')
ax.quiver(0, 0, 0, normal[0], normal[1], normal[2], color='purple', label='Normal')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()

