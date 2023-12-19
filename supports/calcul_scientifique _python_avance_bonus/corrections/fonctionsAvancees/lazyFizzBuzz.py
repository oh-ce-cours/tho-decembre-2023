"""
On veut faire un générateur qui génère un fizz-buzz.

On propose 2 solutions, une utilisant "yield" et une avec "yield from".
"""


def fizz_buzz_1(taille):
    """
    Iterateur avec un yield.
    """
    for i in range(taille):
        to_print = ""
        if i % 3 == 0:
            to_print += "fizz"
        if i % 5 == 0:
            to_print += "buzz"
        if not to_print:
            to_print = str(i)
        yield to_print


def fizz_buzz_2(taille):
    """
    Iterateur avec un yield from depuis un generator comprehension.
    """
    yield from (
        "fizz" * (n % 3 == 0) + "buzz" * (n % 5 == 0) or str(n) for n in range(taille)
    )


def main():
    # On itère sur les deux générateurs en même temps.
    # Si la taille n'était pas la même, on s'arrêterai au même
    # moment que le plus court.

    taille = 101
    for value1, value2 in zip(fizz_buzz_1(taille), fizz_buzz_2(taille)):
        print(value1, value2)


if __name__ == "__main__":
    main()
