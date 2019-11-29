'''
   -----------------------------------------
   Une deuxième implémentation des matrices 2D en python
   -----------------------------------------
'''

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    '''
    Crée une matrice de nbLignes lignes et nbColonnes colonnes
    contenant toute la valeur valeurParDefaut
    paramètres:
    résultat:
    '''
    matrice = []
    for indice_ext in range(nbLignes):
        matrice.append([valeurParDefaut]*nbColonnes)
    return matrice

assert Matrice(3, 5, 5) == [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], "Erreur"


def getNbLignes(matrice):
    '''
    Permet de connaitre le nombre de lignes d'une matrice
    paramètre:
    resultat:
    '''
    return len(matrice)
assert getNbLignes(Matrice(3, 5, 5)) == 3, "Erreur"

def getNbColonnes(matrice):
    '''
    Permet de connaitre le nombre de colonnes d'une matrice
    paramètre:
    resultat:    
    '''
    return len(matrice[0])
assert getNbColonnes(Matrice(3, 5, 5)) == 5, "Erreur"

def getVal(matrice,lig,col):
    '''
    retourne la valeur qui se trouve à la ligne lig colonne col de la matrice
    paramètres:
    resultat:        
    '''
    return matrice[lig][col]
assert getVal([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 18, 5, 5, 5]], 2, 1) == 18, "Erreur"

def setVal(matrice,lig,col,val):
    '''
    place la valeur val à la ligne lig colonne col de la matrice
    paramètres:
    resultat: cette fonction ne retourne rien mais modifie la matrice
    '''
    matrice[lig][col] = val

matrice = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 18, 5, 5, 5]]
setVal(matrice, 0, 3, 576)
print(matrice)
