def liste_multiply (liste, coeff):
    """retourne une liste dont tout les elements sont ceux de la liste qu'on passe en paramètre multupliés par le coeff ègalement en paramètre"""
    res = []
    if len(liste) != 0 :
        for elem in liste : 
            res.append(elem*coeff)
    return res

assert liste_multiply([5,2,8,1], 0.5) == [2.5,1.0,4.0,0.5], "'Erreur"
assert liste_multiply([4,2,6,1], 8) == [32,16,48,8], "Erreur"
assert liste_multiply([], 0)==[], "Erreur"

print("liste_multiply : ")
print(liste_multiply([5,2,8,1], 0.5))
print(liste_multiply([4,2,6,1], 8))


def contient_combien (liste, elem):
    """Cette fonction renvoi le nombre d'occurence d'elem dans liste"""
    cpt = 0
    if len(liste) != 0 :
        for element in liste : 
            if element == elem :
                cpt += 1
    return cpt

assert contient_combien([1,2,1,3,4,1,5,6,1,7,8,1,9,0], 1) == 5, "Erreur"
assert contient_combien("bonjourno", 'o') == 3, "Erreur"
assert contient_combien("", 'r') == 0, "Erreur"
assert contient_combien([], 6) == 0, "Erreur"
assert contient_combien("bonjour", 'w') == 0, "Erreur"

print("\n\ncontient_combien : ")
print(contient_combien([1,2,1,3,4,1,5,6,1,7,8,1,9,0], 1))
print(contient_combien("bonjourno", 'o'))
print(contient_combien("bonjour", 'w'))


def max (liste) :
    """Cette fonction a pour but de retourner le maximum d'une liste
    parametre : liste : la liste dont on va determiner le max"""
    max = 0
    if len(liste) != 0:
        for elem in liste :
            if elem > max :
                max = elem
    return max


def nb_occurences_chaque_element (liste):
    """Cette fonction renvoi une liste composé du nombre d'occurences de chacun des chiffres de 0 au max de la chaine"""
    res = []
    if len(liste) != 0 :
        for i in range(max(liste)+1) : 
            res.append(contient_combien(liste, i))
    return res

assert nb_occurences_chaque_element([1,0,1,3,3,1,1]) == [1,4,0,2], "Erreur"
assert nb_occurences_chaque_element([1,0,1,3,3,1,1,2,4,5,4,3,2,1,3,2,4,2,4]) == [1,5,4,4,4,1], "Erreur"
assert nb_occurences_chaque_element([]) == [], "Erreur"

print("\n\nnb_occurences_chaque_element : ")
print(nb_occurences_chaque_element([1,0,1,3,3,1,1]))
print(nb_occurences_chaque_element([1,0,1,3,3,1,1,2,4,5,4,3,2,1,3,2,4,2,4]))