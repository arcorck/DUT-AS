#Exercice 3
#1) 15 au dessus et pas 50 : 68€, 1 point et aucune suspension
#   45 au dessus et zone 50 : 135€, 4points et 3 ans de suspension
#2) paramètres : vitesse au dessus de la limitation, et zone 50 ou non
#3) le reusltat est un str qui indique le prix de l'amende, le nombre de points retirés et la durée de suspension de permuis
#4) contravention

def Contravention (vitesse, limite_vitesse):
    """Cette fonction a pour objectif d'indiquer en fonction de la vitesse du contrevenant et s'il roulais dans une zone
    limitée à 50 ou non les peines encourues (amende, retrait de point et durée de suspension éventuelle)
	paramètres : 
		vitesse : de type int représente la vitesse à laquelle roulais le contrevenant 
        limite_vitesse : de type int représente la limite de vitesse autorisée """
    exces_vitesse = vitesse - limite_vitesse 
    if (exces_vitesse <= 20):
        if (limite_vitesse == 50):
            return ": 135€, Retrait de 1 point, Suspension de permis : aucune"
        else: #si la vitesse n'es pas limité à 50 km/h
            return ": 68€, Retrait de 1 point, Suspension de permis : aucune"
    if (exces_vitesse > 20 and exces_vitesse <= 30):
        return ": 135€, Retrait de 2 points, Suspension de permis : aucune"
    if (exces_vitesse > 30 and exces_vitesse <= 40):
        return ": 135€, Retrait de 3 points, Suspension de permis : 3 ans"   
    if (exces_vitesse > 40 and exces_vitesse <= 50):
        return ": 135€, Retrait de 4 points, Suspension de permis : 3 ans" 
    if (exces_vitesse > 50):
        return ": 1500€, Retrait de 6 points, Suspension de permis : 3 ans"

assert Contravention(25, True)==": 135€, Retrait de 2 points, Suspension de permis : aucune", "Erreur"
assert Contravention(15, False)==": 68€, Retrait de 1 point, Suspension de permis : aucune", "Erreur"
assert Contravention(45, True)==": 135€, Retrait de 4 points, Suspension de permis : 3 ans", "Erreur"

print ("25 au dessus, en zone 50 ", Contravention(25, True), "\n")
print ("15 au dessus, pas en zone 50 ", Contravention(15, False), "\n")
print ("45 au dessus, en zone 50 ", Contravention(45, True))
	