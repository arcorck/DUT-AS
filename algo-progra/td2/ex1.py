l = [12,8,6,4,78,61,35]

def somme (liste) :
    """Cette fonction a pour but de retourner la somme de tous les elements d'une liste
    parametre : liste : la liste dont on va calculer la somme"""
    somme = 0
    if liste != None:
        for elem in liste :
            somme += elem
    return somme

assert somme(l) == 204, "Erreur dans la somme"
assert somme([]) == 0, "Erreur liste vide"
print("somme l : ", somme(l))
print("somme de liste vide : ", somme([]))


def max (liste) :
    """Cette fonction a pour but de retourner le maximum d'une liste
    parametre : liste : la liste dont on va determiner le max"""
    max = 0
    if liste != None:
        for elem in liste :
            if elem > max :
                max = elem
    return max
assert max(l) == 78, "Erreur dans le max"
assert max([]) == 0, "Erreur liste vide"
print("max de l : ", max(l))
print("max de liste vide : ", somme([]))


def nb_voyelles (mot) :
    """Cette fonction a pour but de retourner le nombre de voyelles dans un mot
    parametre : mot : la chaine de caractere dont on va determiner le nombre de voyelle"""
    voyelles = 0
    if mot != None:
        for char in mot :
            if char in 'aeiouy' :
                voyelles += 1
    return voyelles
assert nb_voyelles("informatique") == 6, "Erreur dans le nombre de voyelles"
assert nb_voyelles("") == 0, "Erreur liste vide"
print("nombre de voyelles dans informatique : ", nb_voyelles("informatique"))
print("nombre de voyelles dans liste vide : ", nb_voyelles(""))