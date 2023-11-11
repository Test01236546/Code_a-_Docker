import voiture as v

# Sous-classe pour une voiture de sport
class VoitureSport(v.Voiture):
    def __init__(self, marque, modele, annee, vitesse_max):
        super().__init__(marque, modele, annee)
        self.vitesse_max = vitesse_max

    def afficher_vitesse_max(self):
        return f"Vitesse Max: {self.vitesse_max} km/h"