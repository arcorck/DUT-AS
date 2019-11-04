def est_symetrique (liste):
    """fonction retournant un booleen qui indique si oui ou non la liste passée en paramètre est symetrique"""
    sym = True
    deb = 0
    fin = len(liste) -1
    moitie_liste = len(liste) / 2
    if len(liste) != 0 : 
        while deb <= moitie_liste :
            if liste[deb] != liste[fin] :
                sym = False
            deb += 1
            fin -= 1
    else : 
        sym = False
    return sym

assert est_symetrique([1,2,3,2,1]) == True, "Erreur"
assert est_symetrique([1,2,3,1]) == False, "Erreur"
assert est_symetrique([]) == False, "Erreur"
assert est_symetrique([0,1,2,3,4,5,6,5,4,3,2,1,0]) == True, "Erreur"

print (est_symetrique([1,2,3,2,1]))
print (est_symetrique([1,2,3,1]))
print (est_symetrique([]))
print (est_symetrique([0,1,2,3,4,5,6,5,4,3,2,1,0]))
