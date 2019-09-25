def char_n (mot, n) :
    """fonction qui renvoie le neme caractère d'un mot
    paramètres : 
        mot : mot pour lequel on veut retourner le n eme caractere
        n : indice du caractere a renvoyer"""
    cpt = 0
    charn = ' '
    if len(mot) != 0 :
        if n >= 0 and n < len(mot) :
            for char in mot :
                if cpt == n :
                    charn = char
                    n = len(mot)
                else :
                    cpt = cpt + 1
    return charn

assert char_n ('info', 2)=='f', 'Erreur'
assert char_n ('', 4)==' ', 'Erreur'
assert char_n ('mot', -4)==' ', 'Erreur'
 
print("on doit avoir f, on a : ", char_n ('info', 2))
print("on doit avoir ' ', on a : ", char_n ('', 4))
print("on doit avoir ' ', on a : ", char_n ('mot', -4))


