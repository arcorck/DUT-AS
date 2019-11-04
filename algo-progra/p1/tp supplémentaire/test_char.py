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

def test_char (mot, n , l):
    """fonction qui renvoie vrai si le caractere l est a la position n du mot
    parametre : 
        - mot : mot pour lequel on teste la position d'une lettre
        - n : indice de la lettre qu'on veut tester
        - l : lettre dont on teste l'indice"""
    bonne_position = False
    if len(mot) != 0:
        if l in mot :
            if char_n(mot, n) == l :
                bonne_position = True
    return bonne_position

assert test_char('info', 2, 'f')==True, "Erreur"
assert test_char('', 6, 'g')==False, "Erreur"
assert test_char('info', 2, 'w')==False, "Erreur"

print(test_char('info', 2, 'f'))
print(test_char('', 6, 'g'))
print(test_char('info', 2, 'w'))