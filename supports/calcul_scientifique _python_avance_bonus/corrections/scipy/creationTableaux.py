import numpy as np
from matplotlib import pyplot as plt

# vecteur de 10 zéros avec un 4 à la 5ème position
a = numpy.zeros(10)
a[4] = 4
print(a)

# vecteur entre 13 et 23
b = 13 + np.arange(11)
print(b)

# vecteur, 854 éléments régulièrement espacés entre 1 et 2
c = np.linspace(1, 2, 854)
print(c)

# matrice 3*4 avec les nombres de 1 à 13
d = np.arange(1, 13).reshape((3, 4))
print(d)
print(d.T)

# matrice diagonale
e = np.eye(3)
print(e)

# matrice aléatoire + moyennes selon les axes
f = np.random.randint(0, 10, (5, 6, 7))
print(f.mean(axis=0).shape, f.mean(axis=0))
print(f.mean(axis=1).shape, f.mean(axis=1))
print(f.mean(axis=2).shape, f.mean(axis=2))

# échiquier 9x9
g = np.zeros((9, 9))
g[1::2, ::2] = 1
g[::2, 1::2] = 1
plt.imshow(g)
plt.show()

# échiquier 2
h = np.tile([[0, 1], [1, 0]], (5, 5))[:9, :9]
print((g == h).all())

# normalisation
i = (b - b.min()) / (b.max() - b.min())
