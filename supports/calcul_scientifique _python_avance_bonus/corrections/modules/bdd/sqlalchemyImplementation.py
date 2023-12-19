import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Stagiaire(Base):
    """On défini une classe stagiaire que l'on va manipuler.
    On n'écrit plus le sql, c'est elle qui s'en charge.

    C'est également une classe python "classique", donc on peut surcharger
    les méthodes magiques pour faire ce que l'on veut sur les instances.
    C'est souvent encouragé de garder les concepts liés aux modèles à un seul endroit.
    """

    __tablename__ = "stagiaire"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    formation_name = Column(String(50))
    note = Column(Integer())

    def __str__(self):
        return "{} - {} : {}".format(self.name, self.formation_name, self.note)

    @classmethod
    def add(cls, engine, nom, nom_formation, note):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        s1 = cls(name=nom, formation_name=nom_formation, note=note)
        session.add(s1)
        session.commit()

    @classmethod
    def list_all(cls, engine):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        for stagiaire in session.query(cls).all():
            print(stagiaire)

    @classmethod
    def not_passing(cls, engine):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session.query(cls).filter(cls.note < 10).all()


def create_tables(engine):
    Base.metadata.create_all(engine)


def main():
    engine = create_engine("sqlite:///sqlalchemy_example.db")
    Base.metadata.bind = engine
    create_tables(engine)
    Stagiaire.add(engine, "Matthieu", "STA", 20)
    Stagiaire.add(engine, "Matthieu", "DBA", 8)

    print("tous les stagiaires")
    Stagiaire.list_all(engine)

    print("ceux qui passent pas")
    for not_passing in Stagiaire.not_passing(engine):
        print(not_passing)


if __name__ == "__main__":
    main()
