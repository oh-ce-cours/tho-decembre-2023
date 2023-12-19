import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


x0, y0 = 10, -5

NB_POINTS = 10000

dx = np.random.randint(-1, 2, NB_POINTS - 1)
dy = np.random.randint(-1, 2, NB_POINTS - 1)

xs = np.cumsum(np.append([x0], dx))
ys = np.cumsum(np.append([y0], dy))

dists = np.sqrt((xs - x0)**2 + (ys - y0)**2)
index = np.arange(NB_POINTS)

plt.plot(xs, ys, '-o', ms=2, alpha=0.2)
plt.scatter(xs, ys, c=index, s=7.5, alpha=0.7)
plt.scatter(xs[0], ys[0], color="red")
# plt.colorbar(shrink=.92)
plt.show()

with sns.axes_style('white'):
    sns.jointplot("x", "y", {"x": xs, "y": ys}, kind='kde')
plt.show()

fig = plt.figure()
sns.distplot(dists)
plt.show()
