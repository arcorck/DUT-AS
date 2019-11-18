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
assert Matrice(5,3,0) == (5,3,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), 'Erreur'

def getNbLignes(matrice):
    '''
    Permet de connaitre le nombre de lignes d'une matrice
    paramètre: une matrice donnée
    resultat: nombre de lignes que contient la matrice
    '''
    return matrice[0]
assert getNbLignes((5,3,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])) == 5, "Erreur"

def getNbColonnes(matrice):
    '''
    Permet de connaitre le nombre de colonnes d'une matrice
    paramètre: une matrice donnee
    resultat: nombre de colonnes que contient la matrice  
    '''
    return matrice[1]
assert getNbColonnes((5,3,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])) == 3, "Erreur"

def getVal(matrice,lig,col):
    '''
    retourne la valeur qui se trouve à la ligne lig colonne col de la matrice
    paramètres: matrice = une matrice donnée, lig = une ligne de la matrice, col = une colonne de la matrice
    resultat: la valeur contenu dans la case de la ligne et de la colonne indiquée         
    '''
    res = None
    if lig >= 0 and col >= 0 and lig <= matrice[0] and col <= matrice[1] :
        res = matrice[2][(lig*col) +col]
    return res 
print (getVal((5,3,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]), 4, 2))
assert getVal ((5,3,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]), 4, 2) == 14, "Erreur"

def setVal(matrice,lig,col,val):
    '''
    place la valeur val à la ligne lig colonne col de la matrice
    paramètres: matrice = matrice que l'on modifie, lig et col = emplacement de la case que l'on modifie et val = valeur de remplacement pour matrice[2][lig*col + lig]
    resultat: cette fonction ne retourne rien mais modifie la matrice
    '''
    matrice[2][lig*col + lig] = val

# === POUR L'EXERCICE 2
# === DU DEBUT JUSQU'ICI  A SAUVEGARDER DANS LE FICHIER matriceAP1.py
# === ET REMPLACER PAR from matriceAP1 import *

# Affichage d'une matrice
def afficheLigneSeparatrice(matrice,tailleCellule=4):
    ''' 
    fonction annexe pour afficher les lignes séparatrices
    paramètres: matrice la matrice à afficher
                tailleCellule la taille en nb de caractères d'une cellule
    résultat: cette fonction ne retourne rien mais fait un affichage
    '''
    print()
    for i in range(getNbColonnes(matrice)+1):
        print('-'*tailleCellule+'+',end='')
    print()

def afficheMatrice(matrice,tailleCellule=4):
    '''
    affiche le contenue d'une matrice présenté sous le format d'une grille
    paramètres: matrice la matrice à afficher
                tailleCellule la taille en nb de caractères d'une cellule
    résultat: cette fonction ne retourne rien mais fait un affichage
    '''

    nbColonnes=getNbColonnes(matrice)
    nbLignes=getNbLignes(matrice)
    print(' '*tailleCellule+'|',end='')
    for i in range(nbColonnes):
        print(str(i).center(tailleCellule)+'|',end='')
    afficheLigneSeparatrice(matrice,tailleCellule)
    for i in range(nbLignes):
        print(str(i).rjust(tailleCellule)+'|',end='')
        for j in range(nbColonnes):
            print(str(getVal(matrice,i,j)).rjust(tailleCellule)+'|',end='')
        afficheLigneSeparatrice(matrice,tailleCellule)
    print()

#-----------------------------------------
# AJOUTER ICI LE CODE DES FONCTIONS DEMANDEES DANS L'EXERCICE 1
#-----------------------------------------
