#Exercice 2
#1) pour l'entier 15 : on est l'apres-midi et il fais jour
#   pour l'entier 21 : on est la nuit et il fait nuit
#2) le seul paramètre de la fonction est l'entier t
#3) son résultat est un str qui dit dans quel period de la journée on est et si il fais jour ou nuit
#4) Jourounuit

def Jourounuit (t):
	"""Cette fonction a pour objectif d'indiquer en fonction de l'heure passée en paramètre
    s'il fais jour ou nuit et si on est le matin, l'après-midi, le soir ou la nuit 
	paramètres : 
		t : de type int représente l'heure pour laquelle on veut tester la fonction """

	if (t<0 or t>23):
		return "Erreur l'heure doit être comprise entre 0 et 23"
	if (6<=t<12):
		s = "on est le matin et "
	else : 
		if (12<=t<18):
			s = "on est l'après-midi et " 
		else:
			if (18<=t<21):
				s = "on est le soir et "
			else:
				s = "on est la nuit et " 
	
	if (7<=t<19):
		s = s + "il fait jour"
	else:
		s = s + "il fait nuit"
	return s
assert Jourounuit(10)=="on est le matin et il fait jour", "erreur : on doit être le matin et il doit faire jour"
assert Jourounuit(15)=="on est l'après-midi et il fait jour", "erreur : on doit être l'après-midi et il doit faire jour"
assert Jourounuit(21)=="on est la nuit et il fait nuit", "erreur : on doit être la nuit et il doit faire nuit"

print("A 10h : ", Jourounuit(10), "\n")
print("A 15h : ", Jourounuit(15), "\n")
print("A 21h : ", Jourounuit(21), "\n")