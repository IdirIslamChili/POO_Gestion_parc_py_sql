from Voiture import Voiture
v1=Voiture("Volkswagen", "Jetta", "2024", 29478)
v1.afficher_info()

from crud_db import connecter_db
try:
    connexion = connecter_db()       # Tente de se connecter
    print("Connexion réussie !") # Si pas d'erreur, affichage
except Exception as e:
    print("Erreur de connexion :", e)  # Affiche l'erreur si ça ne marche pas
finally:
    # Vérifie si la connexion existe et est ouverte avant de fermer
    if 'conn' in locals() and connexion.is_connected():
        connexion.close()