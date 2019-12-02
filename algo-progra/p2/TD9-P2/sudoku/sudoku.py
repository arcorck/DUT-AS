from matriceAPI3 import *

# Affichage d'une matrice
# fonction annexe pour afficher les lignes séparatrices
def afficheLigneSeparatrice(matrice,tailleCellule=4):
    print()
    for i in range(getNbColonnes(matrice)+1):
        print('-'*tailleCellule+'+',end='')
    print()
   
def afficheMatrice(matrice,tailleCellule=4):
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
   


def chargeMatriceSudoku(nomFic) : 
# cas particulier matrice Sudoku car pas de -1
    fic = open(nomFic, 'r')
    ligneLinCol=fic.readline()
    listeLinCol=ligneLinCol.split(',')
    matrice=Matrice(int(listeLinCol[0]),int(listeLinCol[1]))
    i=0
    for ligne in fic:
        listeVal=ligne.split(",")
        j=0
        for elem in listeVal:
            print(elem)
            if elem=='' or elem=='\n':
                setVal(matrice,i,j,None)
            else:
                setVal(matrice,i,j,int(elem))
            j+=1
        i+=1
    return matrice    

#sauvegarder une matrice dans un fichier
def sauveMatriceSudoku(nomFic, mat) :
    fic = open(nomFic, 'w')
    fic.write(str(getNbLignes(mat)),str(getNbColonnes(mat)))
    for i in range(getNbLignes(mat)): 
        li = ''
        for j in range(getNbColonnes(mat)):
            if getVal(mat, i, j) == None : 
                li += str(-1)
            else :
                li += str(getVal(mat, i, j))
            if j < getNbColonnes(mat) - 1 : 
                li +=','
        li +='\n'
        fic.write(li)
    fic.close()


# teste si la taille est correcte
def tailleOk(sudo) : 
    return getNbLignes(sudo) == 9 and getNbColonnes(sudo) == 9

# teste qu'une valeur est bien un nombre entre 1 et 9 ou None
def bonneValeur(v) : 
    if type(var) = None :
        return True
    else : 
        if type(var) == int :
            if var > 0 and var < 10 :
                return True
            else : 
                return False
        else : 
            return False


# teste si les valeurs de la liste sont toutes des bonnes
# valeurs toutes différentes (sauf pour None qui peut apparaitre plusieurs fois)
def bonnesValeursListe(liste) :
    indice = 0
    res = True
    while indice < len(liste) and res == True :
        indice += 1
        res = bonneValeur(liste[indice])
    return res

#une colonne d'une matrice 
def getColonne(mat, col) : 
    pass

# une ligne d'une matrice
def getLigne(mat, lig) : 
    pass

# extrait un bloc carré de la matrice
# les valeurs de ce bloc sont retournés sous la forme d'une liste
def sousTab(mat, i, j, cote=3) :  
    
 
# teste si une matrice est un sudoku valide
def estSudoku(sudo):
    pass

#supprime une valeur dans une liste
def supprime(liste, v) : 
    pass

# retourne les coordonnée du coin supérieur gauche du block auquel
# appartient la case i,j du sudoku
def sousTabAutour(sudo, i, j) : 
    pass
# retourne la liste des valeurs encore possibles pour la case i,j du sudoku  
def listeValPos(sudo, i, j) :
    pass

# indique si un sudo est bloqué
# c'est à dire qu'une case non remplie n'a plus de possiblité 
def estBloque(sudo) :
    pass

# retourne une liste de couple indiquant les coordonnées des cases du sudoku
# pour lesquelles il ne reste qu'une valeur possible
def listeCaseUneValeur(sudo) : 
    pass

# programme de test du sudoku
# charge un sudoku, appelle les différentes fonctions et affiche le resultat obtenu
def testSudoku(nomFic):
    sudoku=chargeMatriceSudoku(nomFic)
    print(nomFic)
    print(sudoku)
    ok=estSudoku(sudoku)
    print('estSudoku =>',ok)
    if ok:
        print('estBloque =>',estBloque(sudoku))
        print('liste cases avec une seule valeur possible',listeCaseUneValeur(sudoku))
        for i in range(getNbLignes(sudoku)):
            for j in range(getNbColonnes(sudoku)):
                if getVal(sudoku,i,j)==None:
                    print('Valeurs possibles en ',i,j,'=>',listeValPos(sudoku, i, j))
    print('-'*20)
    
# exemple d'appel
#testSudoku('sudoku2.txt')