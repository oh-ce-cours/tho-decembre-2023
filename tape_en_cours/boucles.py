nom_utilisateur = "Matthieu"

print("boucle cas 1")

for index in range(0, len(nom_utilisateur)):
    print(nom_utilisateur[index])

print("#############")

print("boucle cas 2")

for index in range(0, len(nom_utilisateur)):
    lettre = nom_utilisateur[index]
    print(lettre)
    
print("#############")

print("boucle cas 2")

for lettre in nom_utilisateur:
    print(lettre)

print("#############")

print("boucle while")

entre_utilisateur = -1

while not 0 < entre_utilisateur < 10 :
    entre_utilisateur = int(input("Entrez un nombre entre 1 et 10 "))
print("Vous avez choisi", entre_utilisateur)   