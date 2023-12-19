import random

print("Vous devez deviner un nombre entre 1 et 100")

nb = random.randint(1, 100)

while True:
    try:
        guess = int(input())
    except ValueError as e:
        print("booooh", e)
        continue

    if guess == nb:
        print("Bravo \o/")
        break
    elif guess < nb:
        print("C'est plus")
    elif guess > nb:
        print("C'est moins")
