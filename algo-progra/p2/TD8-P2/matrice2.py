from matriceAPI2 import *

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

def isNulle (matrice) :
    res = True
    l = 0
    c = 0
    while res == True and l < getNbLignes(matrice) and c < getNbColonnes(matrice) :
        if getVal(matrice, l, c) == 0 :
            if c <  getNbColonnes(matrice) - 1 :
                c += 1
            else :
                c = 0
                l += 1
        else : 
            res = False
            
    return res
assert isNulle ((0,0,[])) == True, "Erreur"
assert isNulle ((2,2,[0,1,2,3])) == False, "Erreur"

def isCarre (matrice):
    nbLignes = getNbLignes(matrice)
    nbColonnes = getNbColonnes(matrice)
    return nbLignes == nbColonnes
assert isCarre ((1,3,[0,1,2])) == False, "Erreur"
assert isCarre ((2,2,[0,1,2,3])) == True, "Erreur la matrice n'est pas carrée"

def moyenne (matrice):
    res = 0
    nbLignes = getNbLignes(matrice)
    nbColonnes = getNbColonnes(matrice)
    if not isNulle(matrice):
        for i in range(nbLignes) :
            for j in range(nbColonnes):
                res += getVal(matrice, i, j)
        res = res / (nbLignes*nbColonnes)
    return res
assert moyenne((2,2,[0,1,2,3])) == 1.5, "Erreur"
assert moyenne((0,0,[])) == 0, 'Erreur'
assert moyenne((3,3,[0,1,2,3,4,5,6,7,8])) == 4.0, "Erreur"
