# Author: Nicolas Rougier
# http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html

import numpy as np


def iterate(Z):
    # Count neighbours
    N = (Z[0:-2, 0:-2] + Z[0:-2, 1:-1] + Z[0:-2, 2:] +
         Z[1:-1, 0:-2]                + Z[1:-1, 2:] +  # noqa
         Z[2:  , 0:-2] + Z[2:  , 1:-1] + Z[2:  , 2:])  # noqa

    # Apply rules
    birth = (N == 3) & (Z[1:-1, 1:-1] == 0)
    survive = ((N == 2) | (N == 3)) & (Z[1:-1, 1:-1] == 1)
    Z[...] = 0  # sélectionne tout
    Z[1:-1, 1:-1][birth | survive] = 1
    return Z


Z = np.random.randint(0, 2, (50, 50))
for i in range(100):
    Z = iterate(Z)
