import random

POSSIBILITE = {
    "pierre": 0,
    "feuille": 1,
    "ciseaux": 2,
}

def regles(j1, j2):
    gagnant = (j1 - j2) % 3
    return gagnant

def affiche(j1, j2, resultat):
    nom_j1, choix_j1 =  j1
    nom_j2, choix_j2 =  j2

    debug = "{} a joue {}"
    print(debug.format(nom_j1, choix_j1))
    print(debug.format(nom_j2, choix_j2))

    if resultat == 1:
        print("{} a gagné".format(nom_j1))
    elif resultat == 2:
        print("{} a gagné".format(nom_j2))
    else:
        print("egalité")

def _jeu(j1, j2):
    nom_j1, choix_j1_humain =  j1
    nom_j2, choix_j2_humain =  j2

    choix_j1 = POSSIBILITE[choix_j1_humain]
    choix_j2 = POSSIBILITE[choix_j2_humain]


    gagnant = regles(choix_j1, choix_j2)
    affiche((nom_j1, choix_j1_humain), (nom_j2, choix_j2_humain), gagnant)
    return gagnant


def jeu(nom_j1, nom_j2):
    choix_j1_humain = random.choice(list(POSSIBILITE.keys()))
    choix_j2_humain = random.choice(list(POSSIBILITE.keys()))

    return _jeu((nom_j1, choix_j1_humain), (nom_j2, choix_j2_humain))


print(jeu("pierre", "paul"))
