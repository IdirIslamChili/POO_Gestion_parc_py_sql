from voiture import Voiture

v1 = Voiture("Volkswagen", "Jetta", 2024, 29478)
v1.afficher_voiture()

from crud_db import connecter_db

connexion = None

try:
    connexion = connecter_db()
    print("Connexion réussie !")
except Exception as e:
    print("Erreur de connexion :", e)
finally:
    if 'connexion' in locals():
        connexion.close()