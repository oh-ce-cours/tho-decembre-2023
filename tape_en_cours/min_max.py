ma_liste = [5, 3, 2, 6, 4, 1, 8]

min_courant = ma_liste[0]
max_courant = ma_liste[0]

for valeur in ma_liste:
    if min_courant > valeur:
        min_courant = valeur
    if max_courant < valeur:
        max_courant = valeur
    
print(min_courant, max_courant)


############

min_courant = min(ma_liste)
max_courant = max(ma_liste)
print(min_courant, max_courant)

###########

liste_triee = sorted(ma_liste)
print(liste_triee[0], liste_triee[len(liste_triee) - 1])