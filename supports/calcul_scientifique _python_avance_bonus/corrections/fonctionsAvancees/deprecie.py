import functools
import inspect

"""
Nous voulons marquer des fonctions comme dépréciées.
Pour cela, nous faisons un décorateur.

Il utilisera le module inspect pour avoir des informations
sur la fonction décorée.

Le décorateur va également enregistrer les fonctions qu'il décore
pour pouvoir les lister.
"""

# liste globale qui va stocker les fonctions dépréciées
FONCTIONS_DEPRECIEES = []


def deprecie(f):
    # il faut que le stockage de la fonction
    # se fasse en dehors du wrapper
    FONCTIONS_DEPRECIEES.append(f)

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print("attention fonction dépréciée utilisée")
        f()

    return wrapper


def analyse():
    print("Fonction dépréciées : ")
    for f in FONCTIONS_DEPRECIEES:
        # on utilise les fonctions du module inspect
        nom, ligne = inspect.getsourcelines(f)
        fichier = inspect.getfile(f)
        print(" * {} - {} - {}".format(fichier, ligne, f.__name__))


@deprecie
def test1():
    pass


@deprecie
def test2(a, b):
    pass


def test3():
    pass


def main():
    analyse()


if __name__ == "__main__":
    main()

