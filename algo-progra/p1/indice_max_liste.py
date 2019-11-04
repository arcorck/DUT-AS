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

assert indice_max_liste([18,4,25,2,5,3]) == 2, "Erreur"
assert indice_max_liste([]) == None, "Erreur"
assert indice_max_liste([25,4,2]) == 0, "Erreur"
assert indice_max_liste([18,8,99]) == 2, "Erreur"
assert indice_max_liste([1,11,3,11,8,11]) == 1, "Erreur"
assert indice_max_liste([-3,-25,-10,-2,-15]) == 3, "Erreur"

print(indice_max_liste([18,4,25,2,5,3]))
print(indice_max_liste([]))
print(indice_max_liste([25,4,2]))
print(indice_max_liste([18,8,99]))
print(indice_max_liste([1,11,3,11,8,11]))
print(indice_max_liste([-3,-25,-10,-2,-15]))