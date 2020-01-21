l2 = [12,8,6,4,78,61,35]
l1 = [6,10,-5,8,-9,5]
l0 = [12,16,18,6,3,5]

def max (liste) :
    """Cette fonction a pour but de retourner le maximum d'une liste
    parametre : liste : la liste dont on va determiner le max"""
    max = 0
    if len(liste) != 0:
        for elem in liste :
            if elem > max :
                max = elem
    return max


def min (liste) :
    """Cette fonction a pour but de retourner le minimum d'une liste
    parametre : liste : la liste dont on va determiner le min"""
    if len(liste) != 0:
        min = max(liste)
        for elem in liste :
            if elem < min :
                min = elem
    else :
        min = "Liste vide"
    return min
assert min(l0) == 3, "Erreur dans le min"
assert min(l1) == -9, "Erreur dans le min"
assert min(l2) == 4, "Erreur dans le min"
assert min([]) == "Liste vide", "Erreur liste vide"
print("min de l0 : ", min(l0))
print("min de l1 : ", min(l1))
print("min de l2 : ", min(l2))
print("min de liste vide : ", min([]))


def moyenne (liste) :
    """Cette fonction a pour but de retourner la moyenne d'une liste
    parametre : liste : la liste dont on va determiner la moyenne"""
    moyenne = 0
    if len(liste) != 0:
        for elem in liste :
            moyenne += elem
        moyenne = moyenne / len(liste)
        moyenne = round(moyenne,2)
    return moyenne 
assert moyenne(l0) == 10, "Erreur dans la moyenne"
assert moyenne(l1) == 2.5, "Erreur dans la moyenne"
assert moyenne(l2) == 29.14, "Erreur dans la moyenne"
assert moyenne([]) == 0, "Erreur liste vide"
print("moyenne de l0 : ", moyenne(l0))
print("moyenne de l1 : ", moyenne(l1))
print("moyenne de l2 : ", moyenne(l2))
print("moyenne de liste vide : ", moyenne([]))


def ecart_min_max (liste, min, max) :
    """Cette fonction a pour but de retourner l'écart entre le min et le max d'une liste
    parametre : 
        liste : la liste dont on va determiner l'écart
        min : minimum de la liste
        max : maximum de la liste"""
    print("min : ", min, " et max : ", max)    
    if len(liste) != 0:
        if max > 0 and min > 0 :
            res = max - min
        if max > 0 and min < 0 :
            res = max - min
        if max < 0 and min < 0 :
            res = -1 * min + max
        if max < 0 and min > 0 :
            res = "Erreur"
    else : 
        res = "Liste vide"
    return res 
assert ecart_min_max(l0, min(l0), max(l0)) == 15, "Erreur dans ecart_min_max"
assert ecart_min_max(l1, min(l1), max(l1)) == 19, "Erreur dans ecart_min_max"
assert ecart_min_max(l2, min(l2), max(l2)) == 74, "Erreur dans ecart_min_max"
assert ecart_min_max([],0,0) == "Liste vide", "Erreur liste vide"
print("ecart_min_max de l0 : ", ecart_min_max(l0, min(l0), max(l0)), "\n")
print("ecart_min_max de l1 : ", ecart_min_max(l1, min(l1), max(l1)), "\n")
print("ecart_min_max de l2 : ", ecart_min_max(l2, min(l2), max(l2)), "\n")
print("ecart_min_max de liste vide : ", ecart_min_max([], 0, 0))


def negatifs (liste) :
    """fonction qui retourne le nombre d'elements négatifs dans une liste
    param : liste : liste pour laquelle on retourne le nombre d'elements negatifs"""
    neg = 0 
    if len(liste) != 0:
        for elem in liste :
            if elem < 0 :
                neg += 1
    else :
        neg = "Liste vide"
    return neg

assert negatifs(l0) == 0, "Erreur de nombre negatifs"
assert negatifs(l1) == 2, "Erreur de nombre negatifs"
assert negatifs(l2) == 0, "Erreur de nombre negatifs"
assert negatifs([]) == "Liste vide", "Erreur de nombre negatifs"
print("nb de neg dans l0 : ", negatifs(l0))
print("nb de neg dans l1 : ", negatifs(l1))
print("nb de neg dans l2 : ", negatifs(l2))
print("nb de neg dans liste vide : ", negatifs([]))