def consecutifs (nombre) :
    """cette fonction prend un chiffre en parametre et renvoie un booleen indiquant si oui ou non le nombre contient
    des chiffres égaux successifs"""
    res = False
    if nombre < 0 :
        nombre = nombre * (-1)
    while nombre > 9:
        if ((nombre // 10)%10) == (nombre % 10) :
            res = True
        nombre = nombre // 10 
    return res

assert consecutifs(1234) == False, "Erreur"
assert consecutifs(5649*4841) == False, "Erreur"
assert consecutifs(1) == False, "Erreur"
assert consecutifs(-1234) == False, "Erreur"
assert consecutifs(2005) == True, "Erreur"
assert consecutifs(56479847126553) == True, "Erreur"
assert consecutifs(1997) == True, "Erreur"

print (consecutifs(1234))
print (consecutifs(5649*4841))
print (consecutifs(1))
print (consecutifs(-1234))
print (consecutifs(2005))
print (consecutifs(56479847126553))
print (consecutifs(1997))