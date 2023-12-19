import random
import time
import json
from collections import defaultdict

from matplotlib import pyplot as plt

"""
Nous allons étudié la complexité algorithmique du
test de contenu (in) des types de base :
    * list
    * set
    * tuple
    * dict

L'exercice propose comme difficultés :
    * définition du "plan d'expérience"
    * génération de données aléatoires
    * mesure du temps passé
"""


def creer_conteneurs(n):
    """
    Fonction qui crée des conteneurs avec N éléments.
    """
    elements = [i for i in range(n)]

    list_rempli = list(elements)
    tuple_rempli = tuple(elements)
    set_rempli = set(elements)
    dict_rempli = {i: 1 for i in elements}
    conteneurs = [list_rempli, tuple_rempli, set_rempli, dict_rempli]
    return conteneurs


def tester_taille_n(n):
    """
    Teste l'opération "in" sur des conteneurs de taille donnée en paramètre.
    """
    conteneurs = creer_conteneurs(n)
    valeurs_a_trouver = [random.randrange(-10000, 10000) for _ in range(100_000)]

    temps_total = {}
    for conteneur in conteneurs:
        tic = time.time()
        for valeur_a_trouver in valeurs_a_trouver:
            # opération que l'on veut tester
            valeur_a_trouver in conteneur
        tac = time.time()
        temps_total[type(conteneur).__name__] = tac - tic

    return temps_total


def traitement(resultats, valeurs_a_tester):
    """
    Effectue le traitement des résultats que l'on a obtenu.
    Pour cela, on doit avoir une liste de durée par type de conteneur.

    On plot ensuite un les résultats pour avoir une visualisation graphique.
    """
    resultats_par_type = defaultdict(list)
    for nb_iteration in resultats:
        for nom_conteneur in resultats[nb_iteration]:
            temps = resultats[nb_iteration][nom_conteneur]
            resultats_par_type[nom_conteneur].append(temps)
    resultats_par_type = dict(resultats_par_type)

    for nom_conteneur in resultats_par_type:
        plt.plot(valeurs_a_tester, resultats_par_type[nom_conteneur])
    plt.legend(resultats_par_type.keys())
    plt.xlabel("nb tests")
    plt.ylabel("temps (en s)")
    plt.savefig("complexite.png")
    plt.title(
        "Analyse de la complexité du test de contenu\npour différents conteneurs Python"
    )
    plt.show()


def main():
    resultats = {}
    valeurs_a_tester = [10, 100, 1000, 10000, 100_000]
    for n in valeurs_a_tester:
        test = tester_taille_n(n)
        print(test)
        resultats[n] = test

    # les résultats sont potentiellement longs à obtenir...
    # on les sauvegardes dans un fichier JSON
    json.dump(resultats, open("tests_complexite.json", "w"))
    traitement(resultats, valeurs_a_tester)


if __name__ == "__main__":
    main()
