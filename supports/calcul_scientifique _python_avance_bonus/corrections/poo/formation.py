from datetime import datetime


class Personne():
    AGE_MAJORITE = 18

    def __init__(self, nom, naissance):
        self.annee_naissance = naissance
        self.nom = nom
        self._age = None

        self.calcul_age()

    def calcul_age(self):
        annee = datetime.today().year
        self._age = annee - self.annee_naissance

    @property
    def age(self):
        self.calcul_age()
        return self._age

    @age.setter
    def ages(self, valeur):
        self._age = valeur
        self.annee_naissance = datetime.today().year - valeur

    def est_majeur(self):
        self.calcul_age()
        return self.age > self.AGE_MAJORITE

    def __str__(self):
        return "Bonjour, je suis {} et j'ai {} ans".format(
            self.nom, self.age
        )


class Eleve(Personne):
    def __init__(self, nom, naissance):
        super().__init__(nom, naissance)
        self.paye_frais_inscription = False

    def __repr__(self):
        s = "Bonjour, je suis un élève."
        if self.paye_frais_inscription:
            s += "J'ai payé mon inscription"
        else:
            s += "Je n'ai pas payé mon inscription."
            s += " Je vais le faire tout de suite"
        return s


class Prof(Personne):
    def __init__(self, nom, naissance, matieres):
        super().__init__(nom, naissance)
        self.matieres = matieres

    def __str__(self):
        m = ""
        if not self.matieres:
            m = "rien"
        elif len(self.matieres) == 1:
            m = self.matieres[0]
        else:
            m = ", ".join(self.matieres[:-1]) + " et " + self.matieres[-1]

        return "Je suis un prof. Trop fort en : {}".format(
            m
        )

    def can_teach_to(self, eleve):
        """Je ne sais pas si c'est du bon OOP
        """
        print(eleve)
        return eleve.est_majeur() and eleve.paye_frais_inscription


class Formation():
    def __init__(self, sujet, prof, eleves):
        self.prof = prof
        self.sujet = sujet
        self.eleves = []
        for eleve in eleves:
            self.enroll(eleve)

    def enroll(self, eleve):
        if self.prof.can_teach_to(eleve):
            self.eleves.append(eleve)


def main():
    bon_eleve = Eleve("bon eleve", 1990)
    bon_eleve.paye_frais_inscription = True

    mauvais_payeur = Eleve("mauvais payeur", 1990)

    jeune = Eleve("jeune", 2010)
    jeune.paye_frais_inscription = True

    p = Prof("P", 1950, ["Python"])

    formation = Formation(
        "Python", p, [bon_eleve, mauvais_payeur, jeune]
    )
    print("Eleves")
    print(formation.eleves)

    # un acte surnaturel ou illégal
    print("Fausse carte d'identité")
    jeune.age = 21
    formation.enroll(jeune)
    print(formation.eleves)
