from Voiture import Voiture
v1=Voiture("Volkswagen", "Jetta", "2024", 29478)
v1.afficher_info()

from crud_db import connecter_db
try:
    connexion = connecter_db()
    print("Connexion réussie !")
except Exception as e:
    print("Erreur de connexion :", e)
finally:
    if 'conn' in locals() and connexion.is_connected():
        connexion.close()