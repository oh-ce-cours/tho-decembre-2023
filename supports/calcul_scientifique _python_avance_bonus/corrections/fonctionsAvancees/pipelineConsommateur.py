import re
from itertools import cycle
import time


def parser_ligne_log_apache(ligne):
    """Permet de parser une ligne de log apache.
    On utilise la méthode classique qui consiste en
    une expression régulière adaptée.
    """
    regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
    match = re.match(regex, ligne)
    if match:
        return match.groups()


def coroutine(func):
    """Permet d'appeler next la première fois automatiquement."""

    def wrapper(*arg, **kwargs):
        generator = func(*arg, **kwargs)
        next(generator)
        return generator

    return wrapper


@coroutine
def parser_ligne_apache(outputs):
    """
    Cette coroutine contient plusieurs sorties.
    Elles sont appelées les unes après les autres.
    """
    while True:
        ligne = (yield)
        ligne_parsee = parser_ligne_log_apache(ligne)
        if ligne_parsee:
            for output in outputs:
                output.send(ligne_parsee)


@coroutine
def trouver_erreur_404(output):
    """Notifie sa sortie quand on a une erreur 404
    """
    while True:
        ligne = (yield)
        if ligne[3] == "404":
            output.send("erreur 404, " + ligne[2])


@coroutine
def poids_images(output):
    """Notifie sa sortie quand une image à été servie.
    Calcule également le poids total des images servies.
    """
    poids_total = 0
    while True:
        ligne = (yield)
        if "jpg" in ligne[2]:
            poids_total += int(ligne[4])
            output.send(
                "jpg, poids : {}b || poids total jusqu'à présent : {}".format(
                    ligne[4], poids_total
                )
            )


@coroutine
def afficher():
    """Coroutine de terminaison. N'a pas d'output"""
    while True:
        x = (yield)
        print(x)


def build_pipeline():
    """On construit le pipeline.
    Il s'agit d'un graphe dirigé.
    Le parseur envoie aux différents filtres qui on un affichage commun.
    """
    aff = afficher()
    erreur404 = trouver_erreur_404(aff)
    img = poids_images(aff)
    parser = parser_ligne_apache([erreur404, img])
    return parser


def main():
    f = open("../../media/logs_apache_exemple.txt")
    pipeline = build_pipeline()
    # on simule un fichier infini
    for line in cycle(f):
        # on simule des connexions "lentes"
        time.sleep(0.01)
        pipeline.send(line)


if __name__ == "__main__":
    main()

