class Observer:
    observers = []

    def __init__(self):
        self.observers.append(self)
        self._observables = {}

    def observe(self, event_name, callback):
        self._observables[event_name] = callback


class Event:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def fire(self):
        for observer in Observer.observers:
            if self.name in observer._observables:
                observer._observables[self.name](self.data)


class LogLectureEcriture(Observer):
    def ecriture_general(self, attr):
        print("nouvel événement écriture general sur : ", attr)

    def lecture_general(self, attr):
        print("nouvel événement de lecture general sur : ", attr)

    def lecture_attribut_inconnu(self, attr):
        print("nouvel événement de lecture d'attribut inconnu sur : ", attr)


class Surveillee:
    def __getattribute__(self, attr):
        Event("lecture", attr).fire()
        try:
            attribute = super().__getattribute__(attr)
        except AttributeError:
            Event("lecture_attribut_inconnu", attr).fire()
            raise AttributeError

        Event("lecture_acces_attribut", attr).fire()
        return attribute

    def __setattr__(self, name, value):
        Event("ecriture", name).fire()
        if not hasattr(self, name):
            Event("ecriture_acces_attribut", name).fire()
        elif getattr(self, name) != value:
            Event("ecriture_update_attribut", name).fire()
        super().__setattr__(name, value)


log = LogLectureEcriture()
log.observe("ecriture", log.ecriture_general)
log.observe("lecture", log.lecture_general)


ss = Surveillee()


ss.existe_maintenant = 1
try:
    ss.lol
except AttributeError:
    pass
ss.existe_maintenant

"""
Cela peut être utile pour surveiller les accès à des attributs.
On peut le mettre dans une classe mère pour le DRY...
"""

