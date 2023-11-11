
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = 0

    def afficher_description(self):
        return f"{self.marque} {self.modele} ({self.annee})"

    def ajouter_kilometrage(self, km):
        if km > 0:
            self.kilometrage += km

    def afficher_kilometrage(self):
        return f"Kilométrage: {self.kilometrage} km"