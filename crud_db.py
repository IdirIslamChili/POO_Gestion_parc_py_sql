import mysql.connector
import json

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
    connexion=connecter_db()
    cursor=connexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voiture(
       id INT auto_increment primary key,
       marque VARCHAR(70),
       modele VARCHAR(70),
       annee int,
       prix decimal (10.2)
    );
    """)
    sql="INSERT INTO voiture values (%s,%s,%s,%s)"
    values=(voiture.id, voiture.marque, voiture.modele, voiture.annee, voiture.prix )
    cursor.execute(sql, values)
    connexion.commit()
    cursor.close()
    connexion.close()
