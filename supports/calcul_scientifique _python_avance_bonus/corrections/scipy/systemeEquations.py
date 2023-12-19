import numpy as np

equals = np.array([[11], [7]])
coeffs = np.array([[1, 5], [3, 2]])
coeffs_inv = np.linalg.inv(coeffs)

res = coeffs_inv @ equals

# ou alors

res2 = np.linalg.solve(coeffs, equals)
