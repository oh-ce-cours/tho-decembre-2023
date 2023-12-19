from collections import Counter, defaultdict
import requests

"""
Implémentation de quelques méthodes pour manipuler des ensembles de mots.

On se focalise sur l'estimation de la complexité algorithmique des opérations.
La référence officielle sur les compléxités est ici : https://wiki.python.org/moin/TimeComplexity

Quand on pense compléxité, il faut toujours réfléchir à quelle est l'ensemble sur lequel on le calcul.
Dans cet exercice, ça ne sera pas toujours le nombre de mots dans un texte.
"""


def mots_differents(mots):
    """
    On utilise le fait qu'un set supprime les répétitions.

    Compléxité linéaire O(n):
        * O(n) pour construire le set des mots (il faut tous les parcourir)
    """
    return set(mots)


def mots_differents_lent(mots):
    """
    Exemple pour montrer ce qu'il ne faut pas faire...
    On fait à la main le filtre sur les répétitions.

    Compléxité quadratique O(n*k) => O(n^2) :
        * O(n) pour parcourir les mots du texte
        * O(k) pour vérifier si un mot est présent dans la liste des mots uniques (k: taille de la liste)
        * on effectue k opérations pour chaque mots => k*n opérations
    """
    mots_uniques = []
    for mot in mots:
        if not mot in mots_uniques:
            mots_uniques.append(mot)
    return mots_uniques


def nb_mots_differents(mots):
    """
    On utilise le fait qu'un ensemble supprime les répétitions.

    Compléxité linéaire O(n):
        * O(n) pour la construction
        * O(1) pour avoir sa longueur (à vérifier)

    On fait une opération O(n) puis une O(1) => O(n)
    """
    return len(mots_differents(mots))


def mots_communs_aux_deux_textes(mots1, mots2):
    """
    On utilise les opérations sur les ensembles.

    Complexité linéaire O(n):
        * O(n) d'après la doc
    """
    return set(mots1).intersection(set(mots2))


def mots_uniquement_presents_texte_1(mots1, mots2):
    """
    On utilise les opérations sur les ensembles.

    Complexité linéaire O(n):
        * n accès à un élément d'un set
        * n * O(1) d'après la doc
        * => O(n)
    """
    return set(mots1) - set(mots2)


def compte_le_nombre_de_repetitions_dun_mot_dans_un_texte(mots):
    """
    Utilise la bibliothèque standart pour compter le nombre d'occurrences d'un mot dans le texte.

    Complexité linéaire O(n) :
        * O(1) pour accéder à un mot dans le dictionnaire
        * O(n) pour parcourir la liste de tous les mots
        * on fait N fois une opération o(1), ça donne une complexité linéaire
    """
    return Counter(mots)


def compte_nombre_mots_dupliques(mots):
    """
    On utilise le comptage des mots que l'on a fait précédemment.

    Complexité linéaire :
        * O(n) pour construire le dictionnaire
        * O(n) pour compter les mots (iteration sur les valeurs d'un dictionnaire)
        * On fait 2 opérations linéaires à la suite => O(n)
    """
    compteur = compte_le_nombre_de_repetitions_dun_mot_dans_un_texte(mots)
    dupliques = 0
    for mot in compteur:
        if compteur[mot] > 1:
            dupliques += 1
    return dupliques


def liste_des_n_mots_preferes(mots, nb):
    """
    Complexité linéaire sur le nombre de mots :
        * on fait une suite d'opérations de complexité linéaire
        * le sort est d'une compléxité log(n) => n est le nombre de tailles de mots différents dans ce cas

    """

    def inverse_dictionnaire(d):
        """Inverse les clefs et les valeurs d'un dico.
        Comme il peut y avoir plusieurs valeurs identiques dans le
        dico d'origine, on crée des listes pour stocker les valeurs
        dans le nouveau dico.
        """
        res = defaultdict(list)
        for k, v in d.items():
            res[v].append(k)
        return res

    compteur = compte_le_nombre_de_repetitions_dun_mot_dans_un_texte(mots)
    d_longueurs = inverse_dictionnaire(compteur)
    longueurs = d_longueurs.keys()
    longueurs = sorted(longueurs)
    return [" - ".join(d_longueurs[l]) for l in longueurs[-nb:]]


def telecharge_et_extrait_mots_des_livres(urls):
    """
    Télécharge les textes à partir des urls.
    Coupe les textes en liste de mots (séparés par des espaces).
    Renvoie la liste de liste.

    Les textes téléchargés sont du type byte, on les décode pour
    avoir des str normales.
    Dans le cas où on utilise request, la bibliothèque le fait pour nous,
    c'est stocké dans la variable text de la requête
    (content contient la version non décodée).
    """
    return [requests.get(u).text.split() for u in urls]


def main():
    url1 = "https://www.gutenberg.org/cache/epub/51804/pg51804.txt"
    url2 = "https://www.gutenberg.org/files/53311/53311-0.txt"
    t1, t2 = telecharge_et_extrait_mots_des_livres([url1, url2])

    print(
        "Il y a {} mots dupliqués dans {}".format(
            compte_nombre_mots_dupliques(t1), url1
        )
    )

    print("Il y a {} mots différents dans {}".format(nb_mots_differents(t2), url2))

    print(
        f"Les textes comptent {len(mots_communs_aux_deux_textes(t1, t2))} mots en commun"
    )

    print(
        f"Le texte 1 compte {len(mots_uniquement_presents_texte_1(t1, t2))} mots qui lui sont spécifiques"
    )

    print(
        "Les 5 mots les plus présents dans {} sont {}".format(
            url1, liste_des_n_mots_preferes(t1, 5)
        )
    )

    print(
        "Les 5 mots les plus présents dans {} sont {}".format(
            url2, liste_des_n_mots_preferes(t2, 5)
        )
    )


if __name__ == "__main__":
    main()

