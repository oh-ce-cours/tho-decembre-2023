import random

pierre = 0
feuille = 1
ciseaux = 2


def jeu(nom_joueur_1, nom_joueur_2):
    joueur_a = random.choice([pierre, feuille, ciseaux])
    joueur_b = random.choice([pierre, feuille, ciseaux])

    if joueur_a == pierre:
        human_a = "pierre"
    if joueur_a == feuille:
        human_a = "feuille"
    if joueur_a == ciseaux:
        human_a = "ciseaux"

    if joueur_b == pierre:
        human_b = "pierre"
    if joueur_b == feuille:
        human_b = "feuille"
    if joueur_b == ciseaux:
        human_b = "ciseaux"

    print(nom_joueur_1, human_a, joueur_a, '-', nom_joueur_2, human_b, joueur_b)
    gagnant = (joueur_a - joueur_b) % 3
    if gagnant == 1:
        print(nom_joueur_1, "a gagné")
    if gagnant == 2:
        print(nom_joueur_2, "a gagné")
    if gagnant == 0:
        print("égalité")


print(jeu("pierre", "paul"))
