import sys
from functools import lru_cache

# on augment la limite de récursion
sys.setrecursionlimit(1000000)


def deco_cache(f):
    """
    Décorateur qui va cacher le résultat d'une fonction
    """
    cache = {}

    def wrapper(n):
        """
        Si une valeur n'est pas dans le cache, on la calcule et on la renvoie.
        Si elle est dans le cache, on ne la calcule même pas...

        On peut également afficher des infos sur les caches misses ou les bons.
        """
        try:
            print("cache ok", n)
            val = cache[n]
        except KeyError:
            print("cache miss", n)
            val = f(n)
            cache[n] = val
        return val

    return wrapper


# @deco_cache
@lru_cache(3, typed=False)
def fibo(n):
    if n <= 2:
        return n
    # print("fibo n", n)
    return fibo(n - 1) + fibo(n - 2)


def main():
    # print(fibo(10))
    print(fibo(1000))
    print(fibo.cache_info())


if __name__ == "__main__":
    main()

"""
Pour LRU cache, on peut changer la taille du cache.
Il suffit d'une petite taille de cache pour avoir de gros effets.
"""
