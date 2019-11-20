################################################
## Exercice de tri                           ##
################################################

def est_croissante (liste):
    """paramètre : liste = liste d'entiers ou de réels
    resultat : bouléen qui indique si la liste est croissante ou non"""
    res = None
    if liste != [] :
        res = True
        cpt = 0
        while cpt < len(liste) -1 and res == True:
            if liste[cpt]>liste[cpt+1] : 
                res = False
            else :
                cpt += 1
    return res
assert est_croissante([1,2,3,4,5,6,7]) == True, "Erreur"
assert est_croissante([1,2,3,4,5,7,6]) == False, "Erreur"
assert est_croissante([15,2,78,5,34,1]) == False, "Erreur"
assert est_croissante([]) == None, "Erreur"


def tribulle(liste):
    """
    tri une liste en suivant l'algorithme du tri à bulle
    parametre: liste : liste que l'on trie
    resultat: Attention cette fonction ne retourne aucun résultat mais modifie la liste
    N'oubliez le print(liste) à la fin de chaque itération de la grande boucle
    """
    aux = 0
    cpt = 0
    while cpt < len(liste) and not est_croissante(liste) :
        for indice_int in range(len(liste) -1 ):
            if liste[indice_int] > liste[indice_int+1] :
                aux = liste[indice_int]
                liste[indice_int] = liste[indice_int+1]
                liste[indice_int+1] = aux
        cpt += 1
        if not est_croissante(liste) :
            print(liste)

# A décommenter lorsque vous avez fini votre implémentation      
l=[15,2,78,5,34,1]
tribulle(l)
assert l==[1,2,5,15,34,78],"Pb Appel tribulle("+str(l)+")"
print("\n")
tribulle([12, 5, -7, 8, 14, -6])
print("\n")
tribulle([12, 4, 5, 7, 5, 6])