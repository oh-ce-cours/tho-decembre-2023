import time
from statistics import mean, stdev
from contextlib import contextmanager


def loooong():
    time.sleep(0.5)


def deco_tempo(f, n):
    """Décorateur permettant de mesurer le temps
    d'exécution d'une fonction
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
            ).format(
                min(durees), mean(durees),
                max(durees), stdev(durees)
            )
        )
    return wrapper


@contextmanager
def context_manager_timer():
    tic = time.time()
    yield
    tac = time.time()
    print(
        "cm -- temps écoulé: {}".format(tac - tic)
    )


class TimerContext():
    def __enter__(self):
        self.tic = time.time()

    def __exit__(self, *args):
        self.toc = time.time()
        print("class manager : {}s".format(
            self.toc - self.tic))


def basique(f):
    tic = time.time()
    f()
    tac = time.time()
    print(
        "basique -- temps écoulé: {}".format(tac - tic)
    )


def main():
    global loooong
    print("basique")
    basique(loooong)

    print("fonction context manager")
    with context_manager_timer():
        loooong()

    print("classe context manager")
    with TimerContext():
        loooong()

    loooong = deco_tempo(loooong, 10)
    print("décorateur")
    loooong()
