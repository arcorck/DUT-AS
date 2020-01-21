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

assert int_to_liste_inverse(1234) == [4,3,2,1], "Erreur"
assert int_to_liste_inverse(5649*4841) == [9,0,8,6,4,3,7,2], "Erreur"
assert int_to_liste_inverse(1) == [1], "Erreur"
assert int_to_liste_inverse (-1234) == [4,3,2,1], "Erreur"

print (int_to_liste_inverse(1234))
print (int_to_liste_inverse(5649*4841))
print (int_to_liste_inverse(1))
print (int_to_liste_inverse (-1234))