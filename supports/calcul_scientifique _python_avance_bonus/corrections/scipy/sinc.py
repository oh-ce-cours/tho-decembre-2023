import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


xs = np.linspace(-10, 10, 100)
ys = np.linspace(-10, 10, 100)
xxs, yys = np.meshgrid(xs, ys)
sincs = np.sin(xxs**2 + yys**2) / (xxs**2 + yys**2)

plt.imshow(sincs, interpolation='nearest', cmap='RdBu')
plt.colorbar(shrink=.92)
plt.show()

# 3d
fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(xxs, yys, sincs, rstride=1, cstride=1, cmap='RdBu')
ax.contourf(xxs, yys, sincs, zdir='z', offset=-2, cmap='RdBu')
ax.set_zlim(-2,2)
fig.show()
