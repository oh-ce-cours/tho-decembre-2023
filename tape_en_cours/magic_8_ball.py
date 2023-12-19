f = open("../supports/medias/phrases_magic_8_ball.txt")  # ouverture en mode relatif

phrases_magic_8_ball = []

for line in f:
    if line != "\n":
        print(line)