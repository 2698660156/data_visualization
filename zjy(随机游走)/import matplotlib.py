import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(0)

num_steps = 1000

step_distances = np.random.uniform(-4, 4, size=(num_steps, 3))

positions = np.cumsum(step_distances, axis=0)

x = positions[:, 0]
y = positions[:, 1]
z = positions[:, 2]

colors = np.arange(num_steps)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=colors, cmap='blues', linewidths=0.5, alpha=0.7)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Three-Dimensional Random Walk')
fig.colorbar(scatter, label='Number of Steps')
plt.show()