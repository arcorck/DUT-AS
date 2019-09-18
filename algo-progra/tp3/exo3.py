def somme_paire (liste):
    """ fonction qui prend une liste en paramètre et qui renvoi la somme de tout les nombres pairs
        parametre : liste, la liste des nombres"""
    somme = 0
    for elem in liste :
        if elem % 2 == 0 :
            somme += elem
    return somme

assert somme_paire([12,13,6,5,7])==18, "Erreur"
assert somme_paire([15,18,14,16,20,21,35,57])==68, "Erreur"
assert somme_paire([1,2,3,4,5,6,7,8,9])==20, "Erreur"

print(somme_paire([12,13,6,5,7]))
print(somme_paire([15,18,14,16,20,21,35,57]))
print(somme_paire([1,2,3,4,5,6,7,8,9]), "\n")



def somme_n_premiers_entiers (n):
    """cette fonction a pour but de retourner la somme des n premiers entiers (de 0 à n)
        parametre : n, le nombre jusqu'auquel on calcule la somme"""
    somme=0
    for elem in range(n+1):
        somme+=elem
    return somme

assert somme_n_premiers_entiers(4)==10, "Erreur"
assert somme_n_premiers_entiers(6)==21, 'Erreur'
assert somme_n_premiers_entiers(15)==120, 'Erreur'

print(somme_n_premiers_entiers(4))
print(somme_n_premiers_entiers(6))
print(somme_n_premiers_entiers(15), "\n")


def somme_n_premiers_entiers_pairs (n):
    """cette fonction a pour but de retourner la somme des n premiers entiers pairs (de 0 à n)
        parametre : n, le nombre jusqu'auquel on calcule la somme"""
    somme=0
    for elem in range(n+1):
        if elem % 2 == 0 :
            somme+=elem
    return somme

assert somme_n_premiers_entiers_pairs(4)==6, "Erreur"
assert somme_n_premiers_entiers_pairs(6)==12, 'Erreur'
assert somme_n_premiers_entiers_pairs(15)==56, 'Erreur'

print(somme_n_premiers_entiers_pairs(4))
print(somme_n_premiers_entiers_pairs(6))
print(somme_n_premiers_entiers_pairs(15), "\n")


def plusieurs_lettres_identiques_consecutives (mot):
    """on va ici tester si un mot contient au moins deux lettres identiques consecutives 
        param : mot, le mot sur lequel on veut tester s'il y a au moins deux lettres identiques consecutives"""
    lettres_consecutives = 1
    lettre_actuelle = ' '
    plusieurs_lettres_consecutives = False
    for char in mot :
        if char == lettre_actuelle :
            lettres_consecutives+=1
        else : 
            lettres_consecutives = 1
        lettre_actuelle = char
        if lettres_consecutives >= 2 :
            plusieurs_lettres_consecutives = True
    return plusieurs_lettres_consecutives

assert plusieurs_lettres_identiques_consecutives ("coucou")==False, 'Erreur'
assert plusieurs_lettres_identiques_consecutives("creee")==True, "Erreur"

print (plusieurs_lettres_identiques_consecutives("coucou"))
print(plusieurs_lettres_identiques_consecutives("cree"))
print(plusieurs_lettres_identiques_consecutives("bonjour"))
print(plusieurs_lettres_identiques_consecutives("boonjour"), "\n")


def plus_longue_suite (liste_de_nombre):
    """cette fonction va nous retourner la taille de la plus grande suite du même chiffre dans la liste
        paramètre : la liste de nombre pour laquelle on veut connaître la taille de la plus grande suite"""
    chiffres_consecutifs = 1
    chiffre_actuel = 0
    taille_plus_grande_suite = 0
    for chiffre in liste_de_nombre :
        if chiffre == chiffre_actuel :
            chiffres_consecutifs+=1
        else : 
            chiffres_consecutifs = 1
        chiffre_actuel = chiffre
        if chiffres_consecutifs > taille_plus_grande_suite :
            taille_plus_grande_suite = chiffres_consecutifs
    return taille_plus_grande_suite

assert plus_longue_suite( [6,6,3,4,2,2,2,4] )==3, "Erreur"
assert plus_longue_suite( [6,6,6,6,6,6,6,3,4,2,2,2,4] )==7, "Erreur"
assert plus_longue_suite( [6,6,3,4,2,2,2,4, 8, 8, 8, 8, 8] )==5, "Erreur"

print(plus_longue_suite( [6,6,3,4,2,2,2,4] ))
print(plus_longue_suite( [6,6,6,6,6,6,6,3,4,2,2,2,4] ))
print(plus_longue_suite( [6,6,3,4,2,2,2,4, 8, 8, 8, 8, 8] ))