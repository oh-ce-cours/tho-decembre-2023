# https://scipy-cookbook.readthedocs.io/items/LoktaVolterraTutorial.html
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# Definition of parameters
a = 1.
b = 0.1
c = 1.5
d = 0.75


def dX_dt(X, t=0):
    """ Return the growth rate of fox and rabbit populations. """
    return np.array([ a*X[0] -   b*X[0]*X[1] ,
                  -c*X[1] + d*b*X[0]*X[1] ])


# équilibre
def etude_equilibre():
    #  pts a étudier
    X_f0 = np.array([0., 0.])
    X_f1 = np.array([c / (d * b), a / b])

    #  matrice jacobienne
    def d2X_dt2(X, t=0):
        """ Return the Jacobian matrix evaluated in X. """
        return np.array([[a - b * X[1], -b * X[0]],
                      [b * d * X[1], -c + b * d * X[0]]])

    # a cote de f0
    A_f0 = d2X_dt2(X_f0)

    #  a cote de f1
    A_f1 = d2X_dt2(X_f1)

    # on regarde les valeurs propres => imaginaires => population périodique
    lambda1, lambda2 = np.linalg.eigvals(A_f1)
    T_f1 = 2 * np.pi / np.abs(lambda1)
    print(lambda1, lambda2)

def integration():
    t = np.linspace(0, 15, 1000)
    # initials conditions: 10 rabbits and 5 foxes
    X0 = np.array([10, 5])
    X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)
    infodict['message']
    return t, X


def plot_populations():
    t, X = integration()
    rabbits, foxes = X.T
    f1 = plt.figure()
    plt.plot(t, rabbits, 'r-', label='Rabbits')
    plt.plot(t, foxes  , 'b-', label='Foxes')
    plt.grid()
    plt.legend(loc='best')
    plt.xlabel('time')
    plt.ylabel('population')
    plt.title('Evolution of fox and rabbit populations')
    f1.savefig('rabbits_and_foxes_1.png')
