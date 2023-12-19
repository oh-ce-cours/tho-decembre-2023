import time
from statistics import mean, stdev
from contextlib import contextmanager

"""
On cherche à développer différentes méthodes pour mesure le temps
d'exécution d'une fonction.

On implémente :
    * un décorateur
    * un context_manager créé par un décorateur
    * un context_manager créé avec une classe
"""


def fonction_lente():
    time.sleep(0.5)


def deco_tempo(f, n):
    """Décorateur permettant de mesurer
    le temps d'exécution d'une fonction.

    Le décorateur prend en paramètre un nombre d'itérations.
    Il va exécuter la fonction à dont on veut connaître le temps
    d'exécution N fois et donner des mesures statistiques sur la
    durée d'exécution.

    Ce décorateur n'utilise pas @wrap, donc, il modifie
    l'introspection de la fonction décorée.
    """

    def wrapper(*args, **kwargs):
        durees = []
        for _ in range(n):
            tic = time.time()
            f(*args, **kwargs)
            tac = time.time()
            print("Temps : {}s".format(tac - tic))
            durees.append(tac - tic)
        print(
            (
                "Stats (en s) :"
                "\n\tmin : {}"
                "\n\tmoyen : {}"
                "\n\tmax : {}"
                "\n\tstd : {}"
            ).format(min(durees), mean(durees), max(durees), stdev(durees))
        )

    return wrapper


@contextmanager
def context_manager_timer():
    """
    Context manager implémenté avec le décorateur et yield.
    Yield effectue une sorte de pause dans la fonction.
    """
    tic = time.time()
    yield
    tac = time.time()
    print("context manager décoré -- temps écoulé: {}".format(tac - tic))


class TimerContext:
    """
    Context manager implémenté comme une classe.
    """

    def __enter__(self):
        self.tic = time.time()

    def __exit__(self, *args):
        self.toc = time.time()
        print("class manager : {}s".format(self.toc - self.tic))


def basique(f):
    """
    Mesure basique du temps d'exécution.
    Ce n'est pas un décorateur car on ne renvoie pas
    la fonction que l'on veut mesurer.
    """
    tic = time.time()
    f()
    tac = time.time()
    print("basique -- temps écoulé: {}".format(tac - tic))


def main(fonction_lente):
    print("basique")
    basique(fonction_lente)

    print("fonction context manager")
    with context_manager_timer():
        fonction_lente()

    print("classe context manager")
    with TimerContext():
        fonction_lente()

    fonction_lente = deco_tempo(fonction_lente, 10)
    print("décorateur")
    fonction_lente()


if __name__ == "__main__":
    main(fonction_lente=fonction_lente)
