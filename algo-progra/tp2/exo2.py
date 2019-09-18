#Exercice 2
#1) pour l'entier 15 : on est l'apres-midi et il fais jour
#   pour l'entier 21 : on est la nuit et il fait nuit
#2) le seul paramètre de la fonction est l'entier t
#3) son résultat est un str qui dit dans quel period de la journée on est et si il fais jour ou nuit
#4) Jourounuit

def Jourounuit (heure):
	"""Cette fonction a pour objectif d'indiquer en fonction de l'heure passée en paramètre
    s'il fais jour ou nuit et si on est le matin, l'après-midi, le soir ou la nuit 
	paramètres : 
		t : de type int représente l'heure pour laquelle on veut tester la fonction """
	
	if (heure<0 or heure>23):
		return "Erreur l'heure doit être comprise entre 0 et 23"
	if (heure >= 6) :
		res = "on est le matin et "
	if heure >= 12 :
		res = "on est l'après-midi et "
	if heure >= 18 :
		res = "on est le soir et "
	if heure >= 21 or t < 6: 
		res = "on est la nuit et "
	if (heure>=7 and heure<19):
		res = res + "il fait jour"
	else:
		res = res + "il fait nuit"
	return res
assert Jourounuit(10)=="on est le matin et il fait jour", "erreur : on doit être le matin et il doit faire jour"
assert Jourounuit(15)=="on est l'après-midi et il fait jour", "erreur : on doit être l'après-midi et il doit faire jour"
assert Jourounuit(21)=="on est la nuit et il fait nuit", "erreur : on doit être la nuit et il doit faire nuit"

print("A 10h : ", Jourounuit(10), "\n")
print("A 15h : ", Jourounuit(15), "\n")
print("A 21h : ", Jourounuit(21), "\n")