def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    matrice = {}
    matrice['lignes'] = nbLignes
    matrice['colonnes'] = nbColonnes
    matrice['valeurs'] = [valeurParDefaut]*nbColonnes*nbLignes
    return matrice

def getNbLignes(matrice):
    return matrice['lignes']

def getNbColonnes(matrice) :
    return matrice['colonnes']

def getVal(matrice,lig,col):
    return matrice['valeurs'][matrice['colonnes']*lig+col]

def setVal(matrice,lig,col,val):
    matrice['valeurs'][matrice['colonnes']*lig+col] = val