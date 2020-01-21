def int_to_liste_inverse (nombre) :
    """cette fonction prend un chiffre en parametre et renvoie une liste en mettant les unités
dans le premier élément de cette liste"""
    res = []
    if nombre < 0 :
        nombre = nombre * (-1)
    while nombre > 9:
        res.append(nombre%10)
        nombre = nombre // 10
    res.append(nombre)
    return res


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


def nombre_symetrique (nombre) : 
    """fonction retournant un booleen qui indique si oui ou non le nombre passé en paramètre est symetrique"""
    return est_symetrique(int_to_liste_inverse(nombre))

assert nombre_symetrique (12321) == True, "Erreur"
assert nombre_symetrique (3) == True, "Erreur"
assert nombre_symetrique (21) == False, 'Erreur'

print(nombre_symetrique(12321))
print(nombre_symetrique(3))
print(nombre_symetrique(21))