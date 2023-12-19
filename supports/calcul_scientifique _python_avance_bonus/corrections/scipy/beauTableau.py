import numpy as np
import matplotlib.pyplot as plt


res = np.zeros((11, 11))

res[3:6, 8:11] = np.eye(3, 3) * 1
res[1:3, 3:9] = 2
res[4:8, 1:3] = 3
res[8:12, 2:11] = 4
res[4:10, 5:9] = 5

plt.imshow(res, cmap="Accent")
plt.colorbar(shrink=.92)

ax = plt.gca()

# Major ticks
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(0, 11, 1))

# Minor ticks
ax.set_xticks(np.arange(-.5, 11, 1), minor=True)
ax.set_yticks(np.arange(-.5, 11, 1), minor=True)

# Gridlines based on minor ticks
ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
plt.savefig("./tableau.png")
plt.show()
