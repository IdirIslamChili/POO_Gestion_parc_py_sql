from voiture import Voiture
from crud_db import ajouter_voiture,connecter_db, supprimer_voiture

v1 = Voiture("Volkswagen", "Jetta", 2024, 29478)
v1.afficher_voiture()

connexion = None

try:
    connexion = connecter_db()
    print("Connexion réussie !")
except Exception as e:
    print("Erreur de connexion :", e)
finally:
    if 'connexion' in locals():
        connexion.close()

v2=Voiture("Toyota", "Corolla", 2022, 30587.15)
v3=Voiture("BMW", "M3", 2025, 89550.30)
v4=Voiture("Audi", "RS6", 2025, 100020.54)

ajouter_voiture(v1)
ajouter_voiture(v2)
ajouter_voiture(v3)
ajouter_voiture(v4)
supprimer_voiture(2)
