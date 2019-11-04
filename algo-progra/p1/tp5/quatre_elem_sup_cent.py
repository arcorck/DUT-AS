def quatre_elem_sup_cent (liste):
    """Cette fonction retourne une liste des 4 premiers éléments supérieurs à 100 dpuis liste passé en paramètre"""
    res = []
    cpt = 0
    if liste != [] :
        while len(res) < 4 and cpt < len(liste):
            if liste[cpt] > 100 :
                res.append(liste[cpt])
            cpt += 1
    return res

assert quatre_elem_sup_cent([]) == [], "Erreur"
assert quatre_elem_sup_cent([1,102,365,14,201,8,471,365]) == [102,365,201,471], "Erreur"
assert quatre_elem_sup_cent([0,1,0,120,54,64,8496]) == [120, 8496], "Erreur"

print(quatre_elem_sup_cent([]))
print(quatre_elem_sup_cent([1,102,365,14,201,8,471,365]))
print(quatre_elem_sup_cent([0,1,0,120,54,64,8496]))

