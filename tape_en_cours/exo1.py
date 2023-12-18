# DEBUT
# VARIABLE CHAINE(str) : nom_utilisateur
# VARIABLE ENTIER(int) : nb_lettres
# 
# DEMANDE nom_utilisateur
# nb_lettres = LONGUEUR(nom_utilisateur)
# 
# SI nb_lettres > 10
#     AFFICHE "votre nom est long"
# SINON
#     AFFICHE "votre nom est court"
# FINSI
# 
# FIN

nom_utilisateur = input("Quel est votre nom : ")
nb_lettres = len(nom_utilisateur)

if nb_lettres > 10:
    print("votre nom est long")
else:
    print("votre nom est court")
