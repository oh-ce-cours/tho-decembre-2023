# ouverture en lecture 
f = open("rappel_j2.md.py")

# on lit le contenu
file_content = f.readlines()
new_line = "Rajouté depuis Python :) \n"
file_content.append(new_line)

# ouverture en écriture (on mets à jour le fichier)
f_ecriture = open("rappel_j2.md.py", mode="w")
f_ecriture.writelines(file_content)
f_ecriture.close()