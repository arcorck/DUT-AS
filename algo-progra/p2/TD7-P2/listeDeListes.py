################################################
## Exercice sur les listes de listes          ##
################################################

# liste de listes pour le premier ascii art 
asciiart1=[[' ', '|', '\\', '/', '\\', '/', '\\', '/', '|', ' ', ' '],[' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' '],\
   [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' '], [' ', '|', ' ', '(', 'o', ')', '(', 'o', ')', ' ', ' '],\
   [' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', '_', ')', ' '], [' ', ' ', '|', ' ', ',', '_', '_', '_', '|', ' ', ' '],\
   [' ', ' ', '|', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' '], [' ', '/', '_', '_', '_', '_', '\\', ' ', ' ', ' ', ' '],\
   ['/', ' ', ' ', ' ', ' ', ' ', ' ', '\\']]

# liste de listes pour le deuxième ascii art 
asciiart2=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', 'n', 'n', 'n', 'n', '_'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', 'G', 'G', 'G', 'G', 'M', 'M', 'b'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', 'p', '~', 'q', 'p', '~', '~', 'q', 'M', 'b'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', '|', '@', '|', '|', '@', ')', ' ', 'M', '|'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', ',', '-', '-', '-', '-', '.', 'J', 'M', '|'],\
    [' ', ' ', ' ', ' ', ' ', ' ', 'J', 'S', '^', '\\', '_', '_', '/', ' ', ' ', 'q', 'K', 'L'],\
    [' ', ' ', ' ', ' ', ' ', 'd', 'Z', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', 'K', 'R', 'b'],\
    [' ', ' ', ' ', ' ', 'd', 'Z', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', 'K', 'K', 'b'],\
    [' ', ' ', ' ', 'f', 'Z', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', 'M', 'M', 'b'],\
    [' ', ' ', ' ', 'H', 'Z', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', 'M', 'M', 'M'],\
    [' ', ' ', ' ', 'F', 'q', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', 'M', 'M', 'M'],\
    [' ', '_', '_', '|', ' ', '"', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\\', 'd', 'S', '"', 'q', 'M', 'L'],\
    [' ', '|', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '`', "'", ' ', '\\', 'Z', 'q'],\
    ['_', ')', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '.', '_', '_', '_', '.', ',', '|', ' ', ' ', ' ', ' ', ' ', '.', "'"], \
    ['\\', '_', '_', '_', '_', ' ', ' ', ' ', ')', 'M', 'M', 'M', 'M', 'M', 'P', '|', ' ', ' ', ' ', '.', "'"],\
    [' ', ' ', ' ', ' ', ' ', '`', '-', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '-', '-', "'", ' ', 'h', 'j', 'm']]


def liste_de_listes_to_str(liste):
    """
    cette fonction transforme une liste de listes en une chaine de caractères
    où les éléments de la liste principale sont accolés sur une même ligne
    paramètre:
    résultat:
    """
    chaine=""
    for elem in liste :
        for elem2 in elem :
            chaine += str(elem2)
        chaine += "\n"
    return chaine

# A décommenter lorsque vous avez fini votre implémentation
assert liste_de_listes_to_str([])=='',"Pb appel liste_de_listes_to_str([])"
assert liste_de_listes_to_str([[0,1,2],[3,4,5],[6,7,8]])=='012\n345\n678\n', "Pb appel liste_de_listes_to_str([[0,1,2][3,4,5][6,7,8]])"
assert liste_de_listes_to_str([['X',' ','O'],['O','X',' '],['O',' ','X']])=='X O\nOX \nO X\n',"Pb appel liste_de_listes_to_str([['X',' ','O'],['O','X',' '],['O',' ','X']])"
print(liste_de_listes_to_str(asciiart1))
print(liste_de_listes_to_str(asciiart2))
# vos tests

def max_dans_liste_de_listes(liste):
    """
    retourne le plus grand élément d'une liste de listes
    paramètre:
    résultat:
    """
    max = None
    for elem in liste : 
        for elem2 in elem :
            if max == None or max < elem2 :
                max = elem2
    return max

# A décommenter lorsque vous avez fini votre implémentation
assert max_dans_liste_de_listes([[0,1,2],[3,4,5],[6,7,8]])==8,"Pb appel max_dans_liste_de_listes([[0,1,2],[3,4,5],[6,7,8]])"
assert max_dans_liste_de_listes([[0,11,25],[7,14,58],[26,17,8]])==58,"Pb appel max_dans_liste_de_listes([[0,11,25],[7,14,58],[26,17,8]])"
assert max_dans_liste_de_listes([])==None,"Pb appel max_dans_liste_de_listes([])"
print(print(max_dans_liste_de_listes([[0,1,2],[3,12,5],[6,7,8]])))
# vos tests

def max_liste (liste):
    max = None
    for elem in liste :
        if max == None or max < elem :
            max = elem
    return max

assert max_liste([1,2,3,9,4,5,6]) == 9, "Erreur"
assert max_liste([]) == None, "Erreur"
assert max_liste([1,2,3,9,4,5,12,6]) == 12, "Erreur"

def max_par_ligne_dans_liste_de_listes(liste):
    """
    retourne la liste des plus grands éléments de chaque ligne dans une liste de listes
    paramètre:
    résultat:
    """
    res = []
    for elem in liste :
        res.append(max_liste(elem))
    return res
# A décommenter lorsque vous avez fini votre implémentation
assert max_par_ligne_dans_liste_de_listes([[0,1,2],[3,4,5],[6,7,8]])==[2,5,8],\
       "Pb Appel max_par_ligne_dans_liste_de_listes([[0,1,2],[3,4,5],[6,7,8]])"
assert max_par_ligne_dans_liste_de_listes([[0,11,25],[7,14,58],[26,17,8]])==[25,58,26],\
       "Pb Appel max_par_ligne_dans_liste_de_listes([[0,11,25],[7,14,58],[26,17,8]])"
assert max_par_ligne_dans_liste_de_listes([[45,1,24],[],[47,85,2,14]])==[45,None,85],\
       "Pb Appel max_par_ligne_dans_liste_de_listes([[45,1,24],[],[47,85,2,14]])"
print(max_par_ligne_dans_liste_de_listes([[1,2,5], [10,8], [], [7,8,1]]))
