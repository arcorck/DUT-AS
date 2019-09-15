#Exercice 3
#1) 15 au dessus et pas 50 : 68€, 1 point et aucune suspension
#   45 au dessus et zone 50 : 135€, 4points et 3 ans de suspension
#2) paramètres : vitesse au dessus de la limitation, et zone 50 ou non
#3) le reusltat est un str qui indique le prix de l'amende, le nombre de points retirés et la durée de suspension de permuis
#4) contravention

def Contravention (v, zc):
    """Cette fonction a pour objectif d'indiquer en fonction de la vitesse du contrevenant et s'il roulais dans une zone
    limitée à 50 ou non les peines encourues (amende, retrait de point et durée de suspension éventuelle)
	paramètres : 
		v : de type int représente la vitesse dépassant la limite autorisée
        zc : de type bool indique si le contrevenant roulais dans une zone limitée à 50km/h ou non """

    if (v <= 20):
        if (zc == True):
            return ": 135€, Retrait de 1 point, Suspension de permis : aucune"
        else:
            return ": 68€, Retrait de 1 point, Suspension de permis : aucune"
    if (v > 20 and v <= 30):
        return ": 135€, Retrait de 2 points, Suspension de permis : aucune"
    if (v > 30 and v <= 40):
        return ": 135€, Retrait de 3 points, Suspension de permis : 3 ans"   
    if (v > 40 and v <= 50):
        return ": 135€, Retrait de 4 points, Suspension de permis : 3 ans" 
    if (v > 50):
        return ": 1500€, Retrait de 6 points, Suspension de permis : 3 ans"

assert Contravention(25, True)==": 135€, Retrait de 2 points, Suspension de permis : aucune", "Erreur"
assert Contravention(15, False)==": 68€, Retrait de 1 point, Suspension de permis : aucune", "Erreur"
assert Contravention(45, True)==": 135€, Retrait de 4 points, Suspension de permis : 3 ans", "Erreur"

print ("25 au dessus, en zone 50 ", Contravention(25, True), "\n")
print ("15 au dessus, pas en zone 50 ", Contravention(15, False), "\n")
print ("45 au dessus, en zone 50 ", Contravention(45, True))
	