"""
Modélisation d'une base de donnée simple stockant les
notes d'un stagiaires à une formation.

Une modélisation plus poussée normaliserai mieux les données.
Il faudrait découpler les informations :
 * extraire les formation dans une autre table qui stockent le nom, la date et la note
 * mettre une clef étrangère entre les stagiaires et les formations
"""

import sqlite3


def create_table(db):
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS
            stagiaires(
                id INTEGER PRIMARY KEY,
                name TEXT,
                formation_name TEXT,
                note INTEGER
            )
    """
    )
    db.commit()


def new_stagiaire(db, nom, nom_formation, note):
    try:
        with db:
            db.execute(
                """INSERT INTO stagiaires(name, formation_name, note)
                    VALUES(?,?,?)""",
                (nom, nom_formation, note),
            )
    except sqlite3.IntegrityError:
        print("Record already exists")


def read_stagiaires(db):
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM stagiaires""")
    for row in cursor:
        print("{0} : {1}, {2}".format(row["name"], row["formation_name"], row["note"]))


def main():
    db = sqlite3.connect("./formation.sqlite")
    try:
        new_stagiaire(db, "Seb", "PYA", 16)
        read_stagiaires(db)
    finally:
        db.close()


if __name__ == "__main__":
    main()
