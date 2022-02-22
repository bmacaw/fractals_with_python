# Code from https://scipython.com/book/chapter-7-matplotlib/examples/a-torus/

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # TODO: why is this import not used?

n = 100

theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)

# We need theta and phi to range over the interval (0, 2pi) independently, so
# use a meshgrid
theta, phi = np.meshgrid(theta, phi)
c, a = 2, 1
x = (c + a*np.cos(theta)) * np.cos(phi)
y = (c + a*np.cos(theta)) * np.sin(phi)
z = a * np.sin(theta)

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_zlim(-3, 3)

# We can use keywords such as edgecolors to style the polygon patched created
# by ax.plot_surface
ax1.plot_surface(x, y, z, rstride=5, cstride=5, color='k', edgecolors='w')
ax1.view_init(36, 26)

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x, y, z, rstride=5, cstride=5, color='k', edgecolors='w')
ax1.view_init(0, 0)
ax2.set_xticks([])
plt.show()
