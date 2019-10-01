def liste_multiply (liste, coeff):
    """retourne une liste dont tout les elements sont ceux de la liste qu'on passe en paramètre multupliés par le coeff ègalement en paramètre"""
    res = []
    if len(liste) != 0 :
        for elem in liste : 
            res.append(elem*coeff)
    return res

assert liste_multiply([5,2,8,1], 0.5) == [2.5,1.0,4.0,0.5], "'Erreur"
assert liste_multiply([4,2,6,1], 8) == [32,16,48,8], "Erreur"
assert liste_multiply([], 0)==[], "Erreur"

print("liste_multiply : ")
print(liste_multiply([5,2,8,1], 0.5))
print(liste_multiply([4,2,6,1], 8))