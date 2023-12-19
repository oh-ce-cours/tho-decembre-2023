#!/usr/bin/env python

import argparse
import sys

"""
On doit réimplémenter des fonction UNIX classique.
Cela est une excuse pour manipuler des listes et des slices.

L'exercice propose comme difficultés :
    * manipulation des slices et des listes

Difficultés supplémentaires :
    * gestion des paramètres de ligne de commande
    * gestion de la mémoire (selon la taille des fichiers)

Lire les commentaires pour avoir les réponses à l'exercice.
"""


def cat(lines):
    """Ré-implémentation de la commande UNIX cat.
    cat imprime les lignes d'un fichier dans l'ordre.
    """
    for line in lines:
        print(line)


def tac(lines):
    """Ré-implémentation de la commande UNIX tac.
    tac imprime les lignes d'un fichier à l'envers.
    """
    reversed_lines = lines[::-1]
    for line in reversed_lines:
        print(line)


def head(lines, n):
    """Ré-implémentation de la commande UNIX head.
    head imprime les n premières lignes d'un fichier
    """
    n_first_lines = lines[:n]
    for line in n_first_lines:
        print(line)


def tail(lines, n):
    """Ré-implémentation de la commande UNIX tail.
    tail imprime les n dernières lignes d'un fichier.
    """
    n_last_lines = lines[-n:]
    for line in n_last_lines:
        print(line)


def perso(lines, nb_avant, nb_apres, saut):
    """Affiche des lignes.
        * à partir de 'nb_avant'
        * jusqu'à 'nb_apres' avant la fin
        * en sautant 'saut' lignes entre chaque
    """
    lines_to_show = lines[nb_avant:-nb_apres:saut]
    for line in lines_to_show:
        print(line)


def parser_arguments():
    parser = argparse.ArgumentParser(
        description="Quelle fonction UNIX voulez vous utiliser ? cat / tac / head / tail"
    )
    parser.add_argument(
        "fonction",
        choices=["cat", "head", "tail", "tac", "perso"],
        help="la fonction à utiliser",
    )
    parser.add_argument("fichier", type=str, help="le fichier à imprimer")

    parser.add_argument(
        "--nb", type=int, help="le nombre de lignes à afficher (pour head et tail)"
    )
    parser.add_argument(
        "--nb_avant",
        type=int,
        help="numéro de ligne à partir de laquelle on commence à afficher",
    )
    parser.add_argument(
        "--nb_apres",
        type=int,
        help="nombre de lignes avant la fin du fichier où l'on n'affiche plus",
    )
    parser.add_argument(
        "--nb_saut",
        type=int,
        help="le nombre de lignes à ne pas considérer entre chaque lignes affichées",
    )
    return parser.parse_args()


def fichier_existant(filepath):
    """
    Vérifie si un fichier existe.
    Met en place le système de "better ask for forgiveness than permission".
    """
    try:
        open(filepath)
    except FileNotFoundError:
        return False
    else:
        return True


def lire_lignes_fichier(filepath):
    """
    On lit toutes les lignes en mémoire
    cela peut poser des problèmes dans les cas où le
    fichier ne tient pas en RAM.

    Dans ce cas, il faudra utiliser des générateurs
    ou alors utiliser des codes comme celui-ci
    https://stackoverflow.com/questions/5896079
    qui va parcourir le fichier par morceaux pour
    trouver les points d'intérêts.
    """
    if not fichier_existant(filepath):
        sys.exit("Le fichier demandé n'existe pas")

    with open(filepath) as f:
        lines = [l.rstrip() for l in f.readlines()]
    return lines


def main():
    arguments = parser_arguments()
    lines = lire_lignes_fichier(arguments.fichier)

    if arguments.fonction == "cat":
        return cat(lines)
    elif arguments.fonction == "tac":
        return tac(lines)
    elif arguments.fonction == "head":
        return head(lines, arguments.nb)
    elif arguments.fonction == "tail":
        return tail(lines, arguments.nb)
    elif arguments.fonction == "perso":
        # cette fonction est un exemple de mauvais paramétrage
        # de ligne de commande à mon avis...
        # on ne devrait pas avoir autant d'options
        # spécifiques pour une seule fonction
        return perso(lines, arguments.nb_avant, arguments.nb_apres, arguments.nb_saut)


if __name__ == "__main__":
    # exemples d'appels :
    # python slices.py cat slices.py
    # python slices.py tac slices.py
    # python slices.py head slices.py --nb 10
    # python slices.py tail slices.py --nb 10
    # python slices.py perso slices.py --nb_avant 10 --nb_apres 10 --nb_saut 2

    # on peut tester les fonction UNIX en comparant la sortie à celle du vrai outil
    # diff <(python slices.py head slices.py --nb 15) <(head -n 15 slices.py)
    main()
