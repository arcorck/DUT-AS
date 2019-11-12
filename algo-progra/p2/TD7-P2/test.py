def max_dans_liste_de_listes(liste):
    """
    retourne le plus grand élément d'une liste de listes
    paramètre:
    résultat:
    """
    max = None
    for elem in liste : 
        for elem2 in elem :
            if max == None or max < elem2 :
                max = elem2
    return max

print(max_dans_liste_de_listes([[0,1,2],[3,4,5],[6,7,8]]))
print(max_dans_liste_de_listes([[0,1,2],[3,12,5],[6,7,8]]))