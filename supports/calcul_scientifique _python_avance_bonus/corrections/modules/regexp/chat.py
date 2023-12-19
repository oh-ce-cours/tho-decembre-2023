import re

text = open("../media/texte_regex.txt").read()


def version_regex(text):
    # pattern1 = "chat"  # 1ere étape
    # pattern2 = "ch?at"  # on détecte chat et cat
    pattern3 = r"\bch?at\b"  # on ne détecte que les mots
    matches = re.finditer(pattern3, text)

    # bonus de présentation
    prez = "Match {} was found at {}-{}: {}"
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        print(prez.format(matchNum, match.start(), match.end(), match.group()))


def findall(sub, string):
    index = 0 - len(sub)
    try:
        while True:
            index = string.index(sub, index + len(sub))
            yield index, index + len(sub)
    except ValueError:
        pass


def version_python_1(text):
    # facile
    res = [i for i in findall("chat", text)]
    print(res)
    return res


def version_python_2(text):
    # un peu plus dur
    chat = [i for i in findall("chat", text)]
    cat = [i for i in findall("cat", text)]
    res = chat + cat
    return res


def version_python_3(text):
    # a ne pas faire...
    elements = version_python_2(text)
    res = []
    STOPS = set(["'", '"', " ", "."])
    for element in elements:
        try:
            before_is_not_word = text[element[0] - 1] in STOPS
        except IndexError:
            before_is_not_word = True

        try:
            after_is_not_word = text[element[1]] in STOPS
        except IndexError:
            after_is_not_word = True

        if before_is_not_word and after_is_not_word:
            res.append(element)
    return res


def main():
    text = open("../media/texte_regex.txt").read()
    version_regex(text)

    print("Python version 1")
    version_python_1(text)

    print("Python version 2")
    print(version_python_2(text))

    print("Python version 3")
    print(version_python_3(text))
