"""
On réimplémente le design pattern property
source : https://docs.python.org/2/howto/descriptor.html#properties
"""


class Property(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, getter=None, setter=None):
        print("__init__", getter, setter)
        self.fonction_getter = getter
        self.fonction_setter = setter

    def __get__(self, instance, owner=None):
        """
        On utilise le protocole de description (descriptor).
        Donc on surcharge __get__.

        Si le getter n'a pas été défini, on renvoie une erreur, sinon
        on utilise la fonction.
        """
        if self.fonction_getter is None:
            raise AttributeError("l'attribut n'est pas accessible")
        return self.fonction_getter(instance)

    def __set__(self, instance, value):
        """
        On utilise le protocole de description (descriptor).
        Donc on surcharge __set__.

        Si le setter n'a pas été défini, on renvoie une erreur, sinon
        on utilise la fonction.
        """
        if self.fonction_setter is None:
            raise AttributeError("on ne peut pas modifier l'attribut")
        self.fonction_setter(instance, value)

    def getter(self, fonction_getter):
        """
        Appeler .getter renvoie une nouvelle instance de l'objet
        dans lequel, on a surchargé la methode getter.
        """
        nouvelle_p = type(self)(fonction_getter, self.fonction_setter)
        return nouvelle_p

    def __call__(self, f):
        """Permet d'éviter d'écrire le p.getter pour
        enregistrer le getter.
        On peut décorer uniquement avec l'instance de la propriété
        """
        return self.getter(f)

    def setter(self, fonction_setter):
        """
        Appeler .setter renvoie une nouvelle instance de l'objet
        dans lequel, on a surchargé la methode setter.
        """
        return type(self)(self.fonction_getter, fonction_setter)


def main():
    p = Property()

    class MyClass(object):
        def __init__(self):
            self._x = 0

        @p.getter
        def my_attr(self):
            return str(self._x) + "!"

        @my_attr.setter
        def my_attr(self, value):
            self._x = value

    m = MyClass()
    print(m.my_attr)
    m.my_attr = 3
    print(m.my_attr)


if __name__ == "__main__":
    main()
