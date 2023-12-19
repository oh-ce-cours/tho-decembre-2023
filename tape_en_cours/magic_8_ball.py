import random

f = open("../supports/medias/phrases_magic_8_ball.txt")  # ouverture en mode relatif

phrases_magic_8_ball = []

for line in f:
    if line != "\n":
        phrases_magic_8_ball.append(line)
    

print(random.choice(phrases_magic_8_ball))