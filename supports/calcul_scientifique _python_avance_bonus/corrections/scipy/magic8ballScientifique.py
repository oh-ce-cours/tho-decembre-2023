import random
from collections import Counter

from scipy.stats import chisquare
from numpy.random import choice as np_choice

NB_REPETITIONS = 500


def messages():
    with open('../media/phrases_magic_8_ball.txt') as f:
        reponses = (l.strip() for l in f.readlines())
        reponses = [l for l in reponses if l]
    return reponses


def magic_1():
    return random.choice(messages())


def magic_2():
    m = messages()
    return m[random.randrange(0, len(m))]


def magic_3():
    m = {i: message for (i, message) in enumerate(messages())}
    return m[random.randrange(0, len(m))]


def magic_pipo_numpy():
    m = messages()
    probs = [1 / len(m)] * len(m)
    probs[0] = probs[0] * 10
    p_total = sum(probs)
    probs = [p / p_total for p in probs]
    return list(np_choice(m, NB_REPETITIONS, p=probs))


def magic_pipo():
    m = messages()
    n = random.randrange(0, len(m) + 1) % len(m)
    return m[n]


def magic_numpy():
    m = messages()
    return list(np_choice(m, NB_REPETITIONS))


def verification():

    def chi_deux(c):
        observe = [v for k, v in c.items()]
        return chisquare(observe)

    c1 = Counter([magic_1() for i in range(NB_REPETITIONS)])
    c2 = Counter([magic_2() for i in range(NB_REPETITIONS)])
    c3 = Counter([magic_3() for i in range(NB_REPETITIONS)])

    print("vérification")
    print(len(c1), len(c2), len(c3))
    print(c1)
    print(c2)
    print(c3)

    print("Test chi 2")
    # pvalue > 0.05 on ne
    # peut pas rejeter l'hypothèse nulle
    # => on considère que c'est équilibré
    print("1", chi_deux(c1).pvalue > 0.05)
    print("2", chi_deux(c2).pvalue > 0.05)
    print("3", chi_deux(c3).pvalue > 0.05)
    print("numpy", chi_deux(Counter(magic_numpy())).pvalue > 0.05)
    print("pipo numpy", chi_deux(Counter(magic_pipo_numpy())).pvalue > 0.05)
    print("pipo", chi_deux(Counter(magic_pipo())).pvalue > 0.05)


def main():
    print(magic_1())
    print(magic_2())
    print(magic_3())
    verification()


if __name__ == "__main__":
    main()
