"""
"""


def est_palindrome(nb):
    return str(nb) == str(nb)[::-1]


def contient_2_ou_7(nb):
    str_nb = str(nb)
    return "2" in str_nb or "7" in str_nb


def commence_par_1(nb):
    return str(nb)[0] == 1


# Organiser les pipelines de générateurs est plutôt embêtant.
origine = range(1000)
commencent_par_un = (i for i in origine if commence_par_1(i))
nombres_divisibles_par_3 = (i for i in commencent_par_un if i % 3 == 0)
palindromes = (i for i in nombres_divisibles_par_3 if est_palindrome(i))
contient_deux_ou_sept = (i for i in palindromes if contient_2_ou_7(i))


# on peut organiser le code dans une classe
# il s'agit en fait du design pattern "chain of responsability"
# un peu modifié...
class Pipeline:
    def __init__(self, iterable):
        self.filtres = []
        self.iterable = iterable

    def ajout_filtre(self, nouveau_filtre):
        """On ajoute le filtre à la liste des filtres.
        """
        self.filtres.append(nouveau_filtre)

    def process(self):
        """Là où tout se fait.
        On applique les filtres les uns à la suite des autres.
        Comme on peut le faire à la main précédemment.
        """
        pipeline = self.iterable
        for nouveau_filtre in self.filtres:
            pipeline = nouveau_filtre(pipeline)
        return pipeline


def create_pipeline(iterable):
    """Fonction qui va créer le pipeline et
    le retourner.

    Si l'on veut changer l'ordre des filtres,
    il suffit que l'on change l'ordre des "ajout_filtre"
    """

    def filter_divisible_par_3(nbs):
        for nb in nbs:
            if nb % 3 == 0:
                yield nb

    def filter_palindrome(nbs):
        for nb in nbs:
            if est_palindrome(nb):
                yield nb

    def map_fois_deux(nbs):
        for nb in nbs:
            yield nb * 2

    pipeline = Pipeline(iterable)
    pipeline.ajout_filtre(filter_divisible_par_3)
    pipeline.ajout_filtre(map_fois_deux)
    pipeline.ajout_filtre(filter_palindrome)
    return pipeline


def main():
    for i in contient_deux_ou_sept:
        print(i)

    pipeline = create_pipeline(range(1000))
    for element in pipeline.process():
        print(element)


if __name__ == "__main__":
    main()
