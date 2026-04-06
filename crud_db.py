import mysql.connector
import json
from voiture import Voiture
def connecter_db():
    with open ("config.json") as f:
        config=json.load(f)

    connexion=mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )
    return connexion

def ajouter_voiture(voiture):
    connexion = connecter_db()
    cursor = connexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voiture(
       id INT auto_increment primary key,
       marque VARCHAR(70),
       modele VARCHAR(70),
       annee int,
       prix decimal (10.2)
    );
    """)
    sql="INSERT INTO voiture values (%s,%s,%s,%s,%s)"
    values=(voiture.id, voiture.marque, voiture.modele, voiture.annee, voiture.prix )
    cursor.execute(sql, values)
    connexion.commit()
    cursor.close()
    connexion.close()
def supprimer_voiture(id):
    connexion = connecter_db()
    cursor = connexion.cursor()

    cursor.execute("DELETE FROM voiture WHERE id = %s", (id,))
    connexion.commit()

    cursor.close()
    connexion.close()

def recuperer_voitures():
    connexion = connecter_db()
    cursor = connexion.cursor()

    cursor.execute("SELECT * FROM voiture")
    resultats = cursor.fetchall()

    voitures = []
    for row in resultats:
        voitures.append(Voiture(row[1], row[2], row[3], row[4], row[0]))

    cursor.close()
    connexion.close()

    return voitures