def liste_bool (n) :
    """fonction qui crée une liste de booléen de 0 à n avec tout les booléens a True sauf ceux aux indices 0 et 1"""
    res = []
    for i in range(n+1) :
        res.append(True)
    res [0] = False
    if n > 0 :
        res [1] = False
    return res

#print(liste_bool(5))
assert liste_bool(5) == [False, False, True, True, True, True]
assert liste_bool(0) == [False]



def false_multiple (liste, n) :
    """Cette fonction prend une liste de booleens en parametre et retourne la meme liste avec tout les booleens dont l'indice est multiple de n valent False (sauf celui à l'indice n lui meme)"""
    for i in range(len(liste)) :
        if i != n and i%n == 0 :
            liste[i] = False
    return liste

#print (false_multiple(liste_bool(6), 2))
assert false_multiple(liste_bool(6), 2) == [False, False, True, True, False, True, False], "Erreur"
assert (false_multiple([False], 5)) == [False], 'Erreur'



def impl_crible_era (n) :
    """renvoie la liste des nombres premiers entre 0 et n"""
    res = []
    if n >= 0 :
        liste = liste_bool(n)
        for i in range(2,10) :
            liste =  false_multiple(liste, i)
        for i in range(len(liste)) :
            if liste[i] == True :
                res.append(i)
    return res

assert impl_crible_era(6) == [2,3,5], "Erreur"
assert impl_crible_era(0) == [], "Erreur"
assert impl_crible_era(-6) == [], "Erreur"

print (impl_crible_era(6))
print (impl_crible_era(28))
print(impl_crible_era(1000))