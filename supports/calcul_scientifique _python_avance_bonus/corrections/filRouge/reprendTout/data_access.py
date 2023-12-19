import sqlite3

db = sqlite3.connect("./formation.sqlite")


def create_table():
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


def new_stagiaire(nom, nom_formation, note):
    try:
        with db:
            db.execute(
                """INSERT INTO stagiaires(name, formation_name, note)
                    VALUES(?,?,?)""",
                (nom, nom_formation, note),
            )
    except sqlite3.IntegrityError:
        print("Record already exists")


def unique_names():
    query = """SELECT DISTINCT name from stagiaires WHERE name IS NOT NULL ORDER BY name ASC;"""
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute(query)
    for row in cursor:
        yield row["name"]


def read_stagiaires(query=None, params=None):
    query = query or """SELECT * FROM stagiaires"""

    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    for row in cursor:
        if row["name"]:
            yield row["id"], row["name"], row["note"], row["formation_name"]
