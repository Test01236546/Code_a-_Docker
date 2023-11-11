
import voiture as v


class VoitureElectrique(v.Voiture):
    def __init__(self, marque, modele, annee, autonomie):
        super().__init__(marque, modele, annee)
        self.autonomie = autonomie

    def afficher_autonomie(self):
        return f"Autonomie: {self.autonomie} km"