import random


def messages():
    with open('../media/phrases_magic_8_ball.txt') as f:
        reponses = (l.strip() for l in f.readlines())
        reponses = [l for l in reponses if l]
    return reponses


def magic_1():
    return random.choice(messages())


def magic_2():
    m = messages()
    return m[random.randrange(0, len(m))]


def main():
    print(magic_1())
    print(magic_2())


if __name__ == "__main__":
    for _ in range(10):
        main()
