import numpy as np

ones_2_2 = np.ones((2, 2))
range_4_8 = np.arange(4, 8)
range_4_6 = np.arange(4, 6)
range_4 = np.arange(4)
range_2 = np.arange(2)
range_1_3 = np.arange(1, 3)

# additions
ones_2_2 + 5
ones_2_2 + range_4_8.reshape((2, 2))
ones_2_2 + range_4_6.reshape((1, 2))
ones_2_2 + range_4_6.reshape((2, 1))
range_4_6.reshape((2, 1)) + range_4_6.reshape((1, 2))

# multplications (terme à terme)
range_4.reshape((2, 2)) * np.arange(2).reshape((2, 1))
range_4.reshape((2, 2)) * range_1_3.reshape((2, 1))
range_4.reshape((2, 2)) * range_1_3.reshape((1, 2))

# multiplications matricielles
# attention, cette fois, l'ordre est important
range_1_3.reshape((1, 2)).dot(range_4.reshape((2, 2)))
