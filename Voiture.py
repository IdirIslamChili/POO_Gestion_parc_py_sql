class Voiture:
    def __init__(self, marque, modele, annee, prix, id=None):
        self.marque=marque
        self.modele=modele
        self.annee=annee
        self.prix=prix
    def afficher_info(self):
        print(f"Marque : {self.marque}, Modèle : {self.modele}, année : {self.annee}. Le prix : {self.prix} $ et l'ID : {self.id}")

