import itertools

"""
Itertools est un module de la bibliothèque standard qui
permet de manipuler les itérateurs.

Cette bibliothèque permet de développer de manière
paraisseuse (en retardant le temps d'exécution).

Pour l'exercice de manipulation de fichiers, nous devions :
    * cat : iterateur classique
    * tac : ce n'est pas possible, on ne peut pas lire le fichier
    * ne pas considérer les N premières lignes : islice
    * ne pas considérer les N dernières lignes : islice quand
        on connait la taille du fichier (il faut le lire une fois probablement)
    * filtre personnalisé : islice quand on connait la taille du fichier
"""


def filtre_perso(iterateur, debut, fin, pas):
    """
    Affiche les éléments de l'itérateur.
    Entre l'élément d'index "debut" et celui de "fin".
    Saute "pas" éléments entre chaque.

    Cela ne respecte pas la demande de l'exercice 1. Sauf si
    l'on connait la taille de l'itérateur
    et que l'on fait en sorte que "fin" corresponde à la
    valeur "taille(iterateur) - fin"
    """
    for element in itertools.islice(iterateur, debut, fin, pas):
        print(element)


def main():
    lines = (x.rstrip() for x in open("slice_paraisse.py"))
    filtre_perso(lines, 1, 10, 2)


if __name__ == "__main__":
    main()
