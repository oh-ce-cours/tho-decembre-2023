import functools

"""
On veut réaliser un décorateur qui imprime :
    * pain
    * salade
    * tomate
    * steak
    * fromage
    * salade
    * pain

Avec la fonction centrale est celle qui imprime steak.


Cela nous permet de manipuler les décorateurs et les décorateurs paramétrés.
"""


def pain(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print("pain")
        f()
        print("pain")

    return wrapper


def tomate(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print("tomate")
        f()

    return wrapper


def fromage(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        f()
        print("fromage")

    return wrapper


def salade(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print("salade")
        f()
        print("salade")

    return wrapper


# les décorateurs sont appliqués du plus près de la
# fonction vers le plus loin.
# Il faut que l'on mette le pain tout en haut pour qu'
# il soit sur les bords du sandwich.


@pain
@salade
@tomate
@fromage
def steak(viande):
    print(viande)


steak("poulay")


HAUT = 1
BAS = 2


def ingredient(nom, cote=(HAUT + BAS)):
    def le_vrai_decorateur(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if cote == HAUT or cote == (HAUT + BAS):
                print(nom)
            f()
            if cote == BAS or cote == (HAUT + BAS):
                print(nom)

        return wrapper

    return le_vrai_decorateur


@ingredient("pain")
@ingredient("salade")
@ingredient("tomate", cote=HAUT)
@ingredient("fromage", cote=BAS)
def steak2():
    print("steak")


if __name__ == "__main__":
    print("--------------------------")
    print("decorateur normal")
    print("--------------------------")
    steak()

    print("--------------------------")
    print("décorateur paramétré")
    print("--------------------------")
    steak2()
