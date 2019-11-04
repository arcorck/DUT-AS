liste_mois = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novmebre', 'Decembre']
liste_releve = [0,1,2,3,4,5,6,7,8,9,10,11, 12]

def releveDuMois(nomMois,releve,mois) :
    """doit retourner la valeur du relevé du mois
passé en paramètre. Si le nom du mois ne correspond à aucun nom de la liste mois la
fonction retourne None"""
    res = None
    if nomMois != [] and mois != '':   
        if mois in nomMois :
            indice = 0
            while indice < len(nomMois) :
                if nomMois[indice] == mois :
                    res = releve[indice]
                indice += 1
    return res

assert releveDuMois(liste_mois, liste_releve, "Mars") == 2, "Erreur"
assert releveDuMois([], liste_releve, "Septembre") == None, "Erreur"
assert releveDuMois(liste_mois, liste_releve, '') == None, "Erreur"

print("releve du mois : ", releveDuMois(liste_mois, liste_releve, "Mars"))



def cumulPrecipitations(releve) :
    """qui doit retourner le cumul total sur l'année des précipitations"""
    indice = 0
    res = 0
    while indice < len(releve) :
        res += releve[indice]
        indice += 1
    return res

assert cumulPrecipitations([52, 44, 46, 49, 64, 45, 60, 50, 50, 64, 58, 58]) == 640, 'Erreur'
assert cumulPrecipitations(liste_releve) == 78, "Erreur"
assert cumulPrecipitations([]) == 0, 'Erreur'

print("\n\ncumul : ",cumulPrecipitations([52, 44, 46, 49, 64, 45, 60, 50, 50, 64, 58, 58]))
print(cumulPrecipitations(liste_releve))
print(cumulPrecipitations([]))



def cumulDepuisJanvier(releve) :
    """doit retourner une liste de douze nombres indiquant
pour chaque mois le cumul de précipitations depuis janvier"""
    res = None
    indice = 0
    if releve != []:
        res = [0]*len(releve)
        while indice < len(releve) :
            if (indice == 0) :
                res[indice] = releve[indice]
            else :
                res[indice] = (releve[indice]) + (res[indice-1])
            indice += 1
    return res

assert cumulDepuisJanvier([]) == None, "Erreur"
assert cumulDepuisJanvier([52, 44, 46, 49, 64, 45, 60, 50, 50, 64, 58, 58]) == [52, 96, 142, 191, 255, 300, 360, 410, 460, 524, 582, 640], "Erreur"
assert cumulDepuisJanvier(liste_releve) == [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78], 'Erreur'

print("\n\ncumul depuis janvier : ", cumulDepuisJanvier([]))
print(cumulDepuisJanvier([52, 44, 46, 49, 64, 45, 60, 50, 50, 64, 58, 58]))
print(cumulDepuisJanvier(liste_releve))



def differenciel(releve) :
    """doit retourner pour chaque mois le diérenciel avec le mois
précédent (en valeur absolue)"""
    res = None
    indice = 0
    if releve != []:
        res = [0]*len(releve)
        while indice < len(releve) :
            if (indice == 0) :
                if releve[indice] > releve[len(releve) -1] :
                    res[indice] = releve[indice] - releve[len(releve) -1]
                else : 
                    res[indice] = releve[len(releve) -1] - releve[indice] 
            else :
                if releve[indice] > releve[indice-1] :
                    res[indice] = releve[indice] - releve[indice-1]
                else : 
                    res[indice] = releve[indice -1] - releve[indice]
            indice += 1
    return res

assert differenciel([52, 44, 46, 49, 64, 45, 60, 50, 50, 64, 58, 58]) == [6, 8, 2, 3, 15, 19, 15, 10, 0, 14, 6, 0], "Erreur"
assert differenciel(liste_releve) == [12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "Erreur"
assert differenciel([]) == None, "Erreur"

print("\n\ndifferenciel : ", differenciel([52, 44, 46, 49, 64, 45, 60, 50, 50, 64, 58, 58]))
print(differenciel(liste_releve))
print(differenciel([]))


def indice_min_liste (liste) :
    """retourne l'indice du plus petit élément de la liste passé en paramètre"""
    res = 0
    if liste == [] :
        res = None
    else :
        min = liste[0]
        for indice in range(len(liste)) :
            if liste[indice] < min :
                min = liste[indice]
                res = indice
    return res

def moisLePlusSec(releve,mois) :
    """doit retourner le nom du mois le plus sec de l'année (si
il y en a plusieurs on retourne un seul de ces mois)"""
    res = None
    if releve != [] and mois != [] :
        res = mois[indice_min_liste(releve)]
    return res

assert moisLePlusSec([52, 44, 46, 49, 64, 45, 60, 50, 50, 64, 58, 58], liste_mois) == 'Fevrier', "Erreur"
assert moisLePlusSec(liste_releve, liste_mois) == 'Janvier', "Erreur"
assert moisLePlusSec([], liste_mois) == None, "Erreur"
assert moisLePlusSec(liste_releve, []) == None, "Erreur"
assert moisLePlusSec([], []) == None, "Erreur"

print("\n\nmois le plus sec :", moisLePlusSec([52, 44, 46, 49, 64, 45, 60, 50, 50, 64, 58, 58], liste_mois))
print(moisLePlusSec(liste_releve, liste_mois))
print(moisLePlusSec([], []))



def indice_max_liste (liste) :
    """retourne l'indice du plus grand élément de la liste passé en paramètre"""
    res = 0
    if liste == [] :
        res = None
    else :
        max = liste[0]
        for indice in range(len(liste)) :
            if liste[indice] > max :
                max = liste[indice]
                res = indice
    return res

def moisLePlusHumide(releve,mois) :
    """doit retourner le nom du mois le plus humide de l'année (si
il y en a plusieurs on retourne un seul de ces mois)"""
    res = None
    if releve != [] and mois != [] :
        res = mois[indice_max_liste(releve)]
    return res

assert moisLePlusHumide([52, 44, 46, 49, 64, 45, 60, 50, 50, 64, 58, 58], liste_mois) == 'Mai', "Erreur"
assert moisLePlusHumide([0,1,2,3,4,5,6,7,8,9,10,11], liste_mois) == 'Decembre', "Erreur"
assert moisLePlusHumide([], liste_mois) == None, "Erreur"
assert moisLePlusHumide(liste_releve, []) == None, "Erreur"
assert moisLePlusHumide([], []) == None, "Erreur"

print("\n\nmois le plus humide :", moisLePlusHumide([52, 44, 46, 49, 64, 45, 60, 50, 50, 64, 58, 58], liste_mois))
print(moisLePlusHumide([0,1,2,3,4,5,6,7,8,9,10,11], liste_mois))
print(moisLePlusHumide([], []))