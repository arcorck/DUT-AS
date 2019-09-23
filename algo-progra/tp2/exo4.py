#Exercice 4
#1) sexe, temps au 100m, nombre de courses gagnées dans l'année et champion du monde ou non 
#2) homme, 18 sec, 3 courses gagnées, pas champion du monde --> non éligible
#   femme, 10, 3 courses gagnées, championne du monde --> éligible
#   femme, 16, 1 course gagnée, pas championne du monde --> non éligible


def Qualifsjo (sexe, meilleur_temps_100m, coursesgagnees, champion):
    """Cette fonction a pour objectif d'indiquer en fonction de différents paramètres si une personne est ou non
        éligible à participer à l'épreuve du 100m des jeux olympiques 
		s : de type str indique si on a à faire à un homme ou à une femme
        tmp : de type int indique le record personnel au 100m de l'individu
        coursesgagnees : de type int indique le nombre de courses gagnées durant l'année par l'individu
        champion : de type bool indique si l'individu à déja été champion du monde """
    if (champion == True):
        etre_qualifie = True
    else:
        if (sexe == "femme"):
            if meilleur_temps_100m < 15 or coursesgagnees >= 3 :
                etre_qualifie = True
            else:
                etre_qualifie = False
        else:
            if meilleur_temps_100m < 12 or coursesgagnees >= 3 :
                etre_qualifie = True
            else:
                etre_qualifie = False
    return etre_qualifie

assert Qualifsjo("homme", 18, 3, False)==True, "Erreur"
assert Qualifsjo("femme", 10, 3, True)==True, "Erreur"
assert Qualifsjo("femme", 16, 1, False)==False, "Erreur"

print(Qualifsjo("homme", 18, 3, False))
print(Qualifsjo("femme", 10, 3, True))
print(Qualifsjo("femme", 16, 1, False))