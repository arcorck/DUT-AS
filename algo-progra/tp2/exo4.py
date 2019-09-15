#Exercice 4
#1) sexe, temps au 100m, nombre de courses gagnées dans l'année et champion du monde ou non 
#2) homme, 18 sec, 3 courses gagnées, pas champion du monde --> non éligible
#   femme, 10, 3 courses gagnées, championne du monde --> éligible
#   femme, 16, 1 course gagnée, pas championne du monde --> non éligible


def Qualifsjo (s, tmp, coursesgagnees, champion):
    """Cette fonction a pour objectif d'indiquer en fonction de différents paramètres si une personne est ou non
        éligible à participer à l'épreuve du 100m des jeux olympiques 
		s : de type str indique si on a à faire à un homme ou à une femme
        tmp : de type int indique le record personnel au 100m de l'individu
        coursesgagnees : de type int indique le nombre de courses gagnées durant l'année par l'individu
        champion : de type bool indique si l'individu à déja été champion du monde """

    if (champion == True):
        return True
    else:
        if (s == "femme"):
            if tmp < 15 or coursesgagnees >= 3 :
                return True
            else:
                return False
        else:
            if tmp < 12 or coursesgagnees >= 3 :
                return True
            else:
                return False

assert Qualifsjo("homme", 18, 3, False)==True, "Erreur"
assert Qualifsjo("femme", 10, 3, True)==True, "Erreur"
assert Qualifsjo("femme", 16, 1, False)==False, "Erreur"

print(Qualifsjo("homme", 18, 3, False), "\n")
print(Qualifsjo("femme", 10, 3, True), "\n")
print(Qualifsjo("femme", 16, 1, False))
