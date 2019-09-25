def nb_occ (mot, lettre):
    """on retourne ici le nombre d'occurences de lettre dans mot
    paramètres : 
        - mot : mot dans lequel on chercher le nombre d'occurences d'une lettre
        - lettre : lettre pour laquelle on cherche dans mot le nombre de ses occurences"""
    occ = 0
    if len(mot) != 0 and len(lettre) == 1:
        for char in mot :
            if char == lettre :
                occ = occ + 1
    return occ

assert nb_occ ('informatisation', 'i') == 3, "Erreur"
assert nb_occ ('informatisation', 'w') == 0, "Erreur"
assert nb_occ ('', 'i') == 0, "Erreur"
assert nb_occ ('informatisation', 'info') == 0, "Erreur"
assert nb_occ ('informatisation', '') == 0, "Erreur"

#print(nb_occ ('informatisation', 'w'))
#print(nb_occ ('informatisation', 'i'))


def first_occ (mot, lettre) : 
    """retourne la place de la premiere occurence d'une lettre dans un mot
    paramètres : 
        - mot : mot dans lequel on chercher la place de la premiere occurence de lettre
        - lettre : lettre pour laquelle on cherche la place de sa premiere occurence"""
    position = 0
    occ1 = 0
    if len(mot) != 0 and len(lettre) == 1:
        if lettre in mot :
            if lettre != mot[0] :
                for char in mot :
                    if char == lettre and occ1 == 0:
                        occ1 = position
                    else : 
                        position = position + 1
    return occ1

assert first_occ ('informatisation', 'i') == 0, "Erreur"
assert first_occ ('informatisation', 'w') == 0, "Erreur"
assert first_occ ('methodologie', 'o') == 4, "Erreur"
assert first_occ ('', 'i') == 0, "Erreur"
assert first_occ ('informatisation', 'info') == 0, "Erreur"
assert first_occ ('informatisation', '') == 0, "Erreur"

print(first_occ ('informatisation', 'w'))
print(first_occ ('informatisation', 'i'))
print(first_occ ('formatisation', 'i'))

