################################################
## Exercice de tri                           ##
################################################

def est_croissante (liste):
    res = True
    if liste != [] :
        cpt = 0
        while cpt < len(liste) - 1 and liste[cpt] < liste[cpt+1]:
            cpt += 1
        if cpt == len(liste) - 2 :
            res = False
    return res


def tribulle(liste):
    """
    tri une liste en suivant l'algorithme du tri à bulle
    parametre: liste : liste que l'on trie
    resultat: Attention cette fonction ne retourne aucun résultat mais modifie la liste
    N'oubliez le print(liste) à la fin de chaque itération de la grande boucle
    """
    aux = 0
    cpt = 0
    trie = False
    for indice_ext in range(len(liste)) :
        while cpt < len(liste) -1 and not trie :
            if liste[cpt] > liste[cpt+1] :
                aux = liste[cpt]
                liste[cpt] = liste[cpt+1]
                liste[cpt+1] = aux
            cpt += 1
        cpt = 0
        print(liste)

# A décommenter lorsque vous avez fini votre implémentation      
l=[15,2,78,5,34,1]
tribulle(l)
assert l==[1,2,5,15,34,78],"Pb Appel tribulle("+str(l)+")"
tribulle([12, 5, -7, 8, 14, -6])