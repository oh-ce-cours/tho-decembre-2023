from math import pi
import numpy as np
from matplotlib import pyplot as plt


def plot(xs, ys, dists):
    plt.scatter(xs, ys, color="red")
    plt.scatter(xs[dists < 1], ys[dists < 1], color="green")
    plt.axes().set_aspect('equal', 'datalim')  # garder le ratio 1:1
    plt.grid()
    plt.show()


def estimate_pi(nb_points):
    aire_carre = 2 * 2
    xs = np.random.uniform(-1, 1, nb_points)
    ys = np.random.uniform(-1, 1, nb_points)
    dists = np.sqrt((xs ** 2 + ys ** 2))

    points_dans_cercle = dists[dists <= 1]
    aire_cercle_est = points_dans_cercle.size / nb_points
    pi_est = aire_cercle_est * aire_carre
    return pi_est, xs, ys, dists


def main():
    nb_points = 10000000
    pi_est, xs, ys, dists = estimate_pi(nb_points)
    print("Mon pi :", pi_est)
    print("Ecart à la réalité :", abs(pi_est - pi))

    plot(xs, ys, dists)
