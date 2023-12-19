f = open("rappel_j2.md.py")

file_content = f.readlines()
new_line = "Rajouté depuis Python :) \n"
file_content.append(new_line)

f = open("rappel_j2.md.py", mode="w")