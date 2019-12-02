'''
   -----------------------------------------
   Une implémentation des matrices 2D en python
   -----------------------------------------
'''

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    '''
    Crée une matrice de nbLignes lignes et nbColonnes colonnes
    contenant toute la valeur valeurParDefaut
    paramètres: nbLignes = nombre de lignes, nbColonnes = nombre de colonnes de la matrice et valeurParDefaut = valeur nulle par defaut qui rempli la matrice
    résultat: renvoie le tuple qui représente la matrice 
    '''
    return (nbLignes, nbColonnes, [valeurParDefaut]*nbColonnes*nbLignes)

def getNbLignes(matrice):
    '''
    Permet de connaitre le nombre de lignes d'une matrice
    paramètre: une matrice donnée
    resultat: nombre de lignes que contient la matrice
    '''
    if matrice[2] != []:
        return matrice[0]
    else : 
        return 0

def getNbColonnes(matrice):
    '''
    Permet de connaitre le nombre de colonnes d'une matrice
    paramètre: une matrice donnee
    resultat: nombre de colonnes que contient la matrice  
    '''
    if matrice[2] != []:
        return matrice[1]
    else : 
        return 0

def getVal(matrice,lig,col):
    '''
    retourne la valeur qui se trouve à la ligne lig colonne col de la matrice
    paramètres: matrice = une matrice donnée, lig = une ligne de la matrice, col = une colonne de la matrice
    resultat: la valeur contenu dans la case de la ligne et de la colonne indiquée         
    '''
    res = None
    if lig >= 0 and col >= 0 and lig <= matrice[0] and col <= matrice[1] :
        res = matrice[2][matrice[1]*lig+col]
    return res 

def setVal(matrice,lig,col,val):
    '''
    place la valeur val à la ligne lig colonne col de la matrice
    paramètres: matrice = matrice que l'on modifie, lig et col = emplacement de la case que l'on modifie et val = valeur de remplacement pour matrice[2][lig*col + lig]
    resultat: cette fonction ne retourne rien mais modifie la matrice
    '''
    matrice[2][matrice[1]*lig+col] = val