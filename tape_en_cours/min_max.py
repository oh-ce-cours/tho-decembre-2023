ma_liste = [5, 3, 2, 6, 4, 1, 8]

min_courant = ma_liste[0]
max_courant = ma_liste[0]

for valeur in ma_liste:
    if min_courant > valeur:
        min_courant = valeur
    if max_courant < valeur:
        max_courant = valeur
    
print(min_courant, max_courant)