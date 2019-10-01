def mystere (mot) :
    """renvoie le meme mot que celui passé en paramètre en otant les lettres multiples successives
    parametre : mot : mot sur lequel on applique la fonction"""
    res = ""
    prec = ""
    if len(mot) != 0 :
        for char in mot :
            if prec != char :
                res += char
            prec = char
    return res

assert mystere ("appelee")=="apele", "Erreur"
assert mystere ("belle")=="bele", "Erreur"
assert mystere ("creee")=="cre", "Erreur"
assert mystere ("")=="", "Erreur"

print(mystere("appelee"))
print(mystere("belle"))
print(mystere("creee"))


def mystere_bis (mot) :
    """renvoie le meme mot que celui passé en paramètre en otant les lettres multiples successives
    parametre : mot : mot sur lequel on applique la fonction"""
    res = ""
    prec = ""
    if len(mot) != 0 :
        for i in range(len(mot)) :
            if prec != mot[i] :
                res += mot[i]
            prec = mot[i]
    return res

assert mystere_bis ("appelee")=="apele", "Erreur"
assert mystere_bis ("belle")=="bele", "Erreur"
assert mystere_bis ("creee")=="cre", "Erreur"
assert mystere_bis ("")=="", "Erreur"

print(mystere_bis("appelee"))
print(mystere_bis("belle"))
print(mystere_bis("creee"))
