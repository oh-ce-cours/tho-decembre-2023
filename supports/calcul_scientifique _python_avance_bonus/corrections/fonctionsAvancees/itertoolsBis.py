import itertools

"""
Réimplémentation des fonctions de itertools
    * chain
    * cycle
"""


def chain1(*iterables):
    for it in iterables:
        for element in it:
            yield element


def chain2(*iterables):
    for iterable in iterables:
        yield from iterable


def cycle(iterable):
    """On ne peut pas cycler sur un iterable
    en temps normal. Il faut donc sauvegarder les
    éléments en mémoire.

    Cea peut poser un problème de mémoire en cas d'itérables
    très gros...
    """
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element


def main():
    iterables = [range(10), range(20), range(3)]

    print("chain1")
    for element in chain1(iterables[0], iterables[1], iterables[2]):
        print(element)

    print("chain2")
    for element in chain2(*iterables):
        print(element)

    print("cycle")
    for element in itertools.islice(cycle(range(10)), 30):
        print(element)


if __name__ == "__main__":
    main()
