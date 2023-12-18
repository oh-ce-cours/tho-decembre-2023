import string
from collections import Counter
import requests


def build_translator(nb, orig):
    """Construit un dictionnaire avec comme clé la 
    lettre d'origine et comme valeur la lettre décallé 
    selon le nombre passé comme décalage;  
    """
    shift = list(orig[nb:]) + list(orig[:nb])
    translator = {o: s for o, s in zip(orig, shift)}
    return translator


def build_translator_all_ascii(nb):
    """Construit le traducteur pour les lettres majuscules et minuscules. 

    On doit les construire séparément pour gérer correctement les majuscules et minuscules. 
    Ensuite, on les regroupe. 
    """
    lowercases = build_translator(nb, list(string.ascii_lowercase))
    uppercases = build_translator(nb, list(string.ascii_uppercase))

    # on regroupe les deux dictionnaires, on pourrait le faire dans une boucle for
    return {**lowercases, **uppercases}


def invert_translator(converter):
    """Inverse les clés et les valeurs d'un dictionnaire.
    """
    return {v: k for k, v in converter.items()}


def convert_char(converter, c):
    """Converti un caractère unique et donc déchiffre
    une lettre du chiffre de César.
    """
    return converter.get(c, c)


def convert_all_text(converter, message):
    """Décale un texte entier à partir d'un dictionnaire de convertion. 
    """
    crypted = [convert_char(converter, c) for c in message]
    return "".join(crypted)


def build_cipher_decipher(nb):
    """Construit un dictionnaire permettant de chiffrer et déchiffrer
     un texte avec un décallage donné. 

    Retourne 2 dictionnaire, un pour chiffrer et un pour déchiffrer.
    """
    shift = nb % len(string.ascii_lowercase)
    dict_cipher = build_translator_all_ascii(shift)
    dict_decipher = invert_translator(dict_cipher)
    return dict_cipher, dict_decipher


def most_common_letter(text):
    """Récupère la lettre la plus commune dans un texte.
    """
    return Counter(
        [text for text in text.lower() if text in string.ascii_lowercase]
    ).most_common(1)[0][0]


def build_cipher_from_text(text):
    """Pour un texte donné, renvoie le cesar cipher pour le déchiffrer
    en utilisant une analyse en fréquences.
    """
    most_common_letter_in_text = most_common_letter(text)
    # la lettre la plus fréquente doit être le e
    # on calcule la distance entre la lettre la plus fréquente et le e
    shift = ord(most_common_letter_in_text) - ord("e")
    return build_cipher_decipher(shift)


def analyze_urls(urls):
    """Filtre une liste d'URL pour ne récupérer 
    que celles qui ont un code de status à 200 (OK).
    """
    print("urls found:", urls)
    res = []
    for url in urls:
        # on enlève le retour à la ligne qui est
        # encore présent à la fin de la chaîne
        url = url.strip()
        print("analyzing {}".format(url))
        r = requests.get(url)
        if r.status_code != 200:
            continue
        print("url OK:", url)
        content = r.text
        res.append((url, content))
    return res


def decrypt_text(content):
    """Fonction qui permet de craquer un code de Cesar 
    à partir d'une chaine contenant un contenu chiffré. 

    Elle détermine la valeur du décallage, construit les 
    chiffreur et déchiffreur et retourne la valeur du texte
    déchiffré. 
    """
    crypter, decrypter = build_cipher_from_text(content)
    decrypted = convert_all_text(decrypter, content)
    return decrypted


def main():
    urls = open("./urls.txt").readlines()
    exploitable = analyze_urls(urls)

    for (url, content) in exploitable:
        decrypted = decrypt_text(content)
        print("Le contenu décrypté de", url, "est")
        print(decrypted)


main()
