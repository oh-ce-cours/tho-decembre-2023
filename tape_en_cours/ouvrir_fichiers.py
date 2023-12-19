# ouverture en lecture 
f = open("rappel_j2.md.py", encoding="utf8") # on spécifie l'encodage du fichier
# f = open("C://Documents/pro/projet/file.txt")  # ouverture en mode absolue
f = open("../supports/medias/phrases_magic_8_ball.txt")  # ouverture en mode relatif

# on lit le contenu et on le mets à jour en rajoutant une ligne à la fin
file_content = f.readlines()
new_line = "Rajouté depuis Python :) \n"
file_content.append(new_line)

# # ouverture en écriture (on mets à jour le fichier)
# f_ecriture = open("rappel_j2.md.py", mode="w")
# f_ecriture.writelines(file_content)
# f_ecriture.close()