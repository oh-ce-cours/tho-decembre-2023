import math
import numpy as np

start = -1
stop = 1
nb = 842


def main_numpy():
    def carre(x):
        return x ** 2

    def cos(x):
        return np.cos(x)

    def complique(x):
        return np.log(x**2) / np.exp(-x)

    xs = np.linspace(start, stop, num=nb)

    return carre(xs), cos(xs), complique(xs)


def main_python():
    def carre(xs):
        return [x ** 2 for x in xs]

    def cos(xs):
        return [math.cos(x) for x in xs]

    def complique(xs):
        return [math.log(x**2) / math.exp(-x) for x in xs]

    norms = (i / (nb - 1) for i in range(nb))
    xs = list(((i * 2) - 1 for i in norms))

    return carre(xs), cos(xs), complique(xs)


def main_vectorize():
    def carre(x):
        return x ** 2

    def cos(x):
        return math.cos(x)

    def complique(x):
        return math.log(x**2) / math.exp(-x)

    norms = (i / (nb - 1) for i in range(nb))
    xs = list(((i * 2) - 1 for i in norms))

    carre = np.frompyfunc(carre, 1, 1)
    cos = np.frompyfunc(cos, 1, 1)
    complique = np.frompyfunc(complique, 1, 1)
    return carre(xs), cos(xs), complique(xs)


def main():
    np_ca, np_cos, np_com = main_numpy()
    py_ca, py_cos, py_com = main_python()
    vec_ca, vec_cos, vec_com = main_vectorize()

    np.testing.assert_almost_equal(np_ca, py_ca)
    np.testing.assert_almost_equal(np_cos, py_cos)
    np.testing.assert_almost_equal(np_com, py_com)
