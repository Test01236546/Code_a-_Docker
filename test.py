import voiture as v
import voiture_e as ve
import voiture_s as vs

# Exemple d'utilisation
voiture1 = v.Voiture("Peugeot", "508", 2021)
voiture_elec = ve.VoitureElectrique("Tesla", "Model 3", 2022, 500)
voiture_sport = vs.VoitureSport("Ferrari", "F8", 2020, 340)

print(voiture1.afficher_description())
print(voiture_elec.afficher_description(), voiture_elec.afficher_autonomie())
print(voiture_sport.afficher_description(), voiture_sport.afficher_vitesse_max())