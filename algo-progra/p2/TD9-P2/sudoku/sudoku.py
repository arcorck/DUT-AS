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

matrice = Matrice(9, 9, None)
#print(matrice)

# teste si la taille est correcte
def tailleOk(sudo) : 
    return getNbLignes(sudo) == 9 and getNbColonnes(sudo) == 9

#print(tailleOk(matrice))

# teste qu'une valeur est bien un nombre entre 1 et 9 ou None
def bonneValeur(v) : 
    if v is None :
        return True
    else : 
        if type(v) == int :
            if v > 0 and v < 10 :
                return True
            else : 
                return False
        else : 
            return False
            
setVal(matrice,5, 7, 8)
setVal(matrice,5, 4, 67)
#print(bonneValeur(getVal(matrice, 5, 4)))
#print(bonneValeur(getVal(matrice, 5, 7)))

# teste si les valeurs de la liste sont toutes des bonnes
# valeurs toutes différentes (sauf pour None qui peut apparaitre plusieurs fois)
def bonnesValeursListe(liste) :
    indice = 0
    res = True
    while indice < len(liste)-1 and res == True :
        indice += 1
        res = bonneValeur(liste[indice])
    return res
#print(bonnesValeursListe(matrice['valeurs']))
#matrice_null = Matrice(9, 9, None)
#afficheMatrice(matrice_null)
#print(bonnesValeursListe(matrice_null['valeurs']))

#une colonne d'une matrice 
def getColonne(mat, col) :
    colonne = [] 
    for i in range(matrice['colonnes']) :
        colonne.append(getVal(mat, i, col))
    return colonne
setVal(matrice,0, 7, 1)
setVal(matrice,1, 7, 8)
setVal(matrice,2, 7, 4)
setVal(matrice,3, 7, 8)
setVal(matrice,4, 7, 6)
setVal(matrice,5, 7, 8)
setVal(matrice,6, 7, 3)
setVal(matrice,7, 7, 2)
setVal(matrice,8, 7, 7)
#afficheMatrice(matrice)
#print(getColonne(matrice, 7))

# une ligne d'une matrice
def getLigne(mat, lig) : 
    ligne = [] 
    for i in range(matrice['lignes']) :
        ligne.append(getVal(mat, lig, i))
    return ligne
setVal(matrice,5, 0, 1)
setVal(matrice,5, 1, 8)
setVal(matrice,5, 2, 4)
setVal(matrice,5, 3, 8)
setVal(matrice,5, 4, 6)
setVal(matrice,5, 5, 8)
setVal(matrice,5, 6, 3)
setVal(matrice,5, 7, 2)
setVal(matrice,5, 8, 7)
#afficheMatrice(matrice)
#print(getLigne(matrice, 5))

# extrait un bloc carré de la matrice
# les valeurs de ce bloc sont retournés sous la forme d'une liste
def sousTab(mat, i, j, cote=3) :  
    sous_tab = []
    for indice_ligne in range(i, i+cote, 1) :
        for indice_colonne in range(j, j+cote, 1) :
            sous_tab.append(getVal(mat, indice_ligne, indice_colonne))
    return sous_tab
setVal(matrice,0, 0, 0)
setVal(matrice,0, 1, 1)
setVal(matrice,0, 2, 2)
setVal(matrice,1, 0, 3)
setVal(matrice,1, 1, 4)
setVal(matrice,1, 2, 5)
setVal(matrice,2, 0, 6)
setVal(matrice,2, 1, 7)
setVal(matrice,2, 2, 8)
#afficheMatrice(matrice)
#print(sousTab(matrice,6,6))
 
# teste si une matrice est un sudoku valide
def estSudoku(sudo):
    res = True
    if not tailleOk(sudo) :
        res = False
    else :
        for indice in range(getNbColonnes(sudo)):
            if not bonnesValeursListe(getColonne(sudo, indice)) :
                res = False
    return res
#afficheMatrice(matrice)
#print(estSudoku(matrice))
setVal(matrice,2, 2, 845)
#print(estSudoku(matrice))

#supprime une valeur dans une liste
def supprime(liste, v) :
    if v in liste :
        for ind in range(len(liste)-1) :
            if liste[ind] == v :
                liste.pop(ind)

#liste = [0,1,2,3,4,5]
#print(liste)
#supprime(liste, 3)
#print(liste)

# retourne les coordonnée du coin supérieur gauche du block auquel
# appartient la case i,j du sudoku
def sousTabAutour(sudo, i, j) : 
    return (i-i%3),(j-j%3)
#print(sousTabAutour(matrice, 2,8))
#print(sousTabAutour(matrice, 0, 0))
#print(sousTabAutour(matrice, 2,2))
#print(sousTabAutour(matrice, 7,5))

# retourne la liste des valeurs encore possibles pour la case i,j du sudoku  
def listeValPos(sudo, i, j) :
    liste = []
    ligne = getLigne(sudo, i)
    colonne = getColonne(sudo, j)
    coordonnes_carre = sousTabAutour(sudo,i,j)
    carre = sousTab(sudo,coordonnes_carre[0], coordonnes_carre[1])
    for indice in range(len(ligne)) :
        if indice not in ligne and indice not in colonne and indice not in carre : 
            liste.append(indice)
    return liste
#afficheMatrice(matrice)
#print(listeValPos(matrice, 7, 6))
#print(listeValPos(matrice, 1, 4))
#print(listeValPos(matrice, 4, 1))

# indique si un sudo est bloqué
# c'est à dire qu'une case non remplie n'a plus de possiblité 
def estBloque(sudo) :
    res = False
    for indice_ligne in range(getNbLignes(matrice)) :
        for indice_colonne in range(getNbColonnes(matrice)):
            if getVal(sudo, indice_ligne, indice_colonne) is None :
                if listeValPos(sudo, indice_ligne, indice_colonne) == [] :
                    res = True
    return res
setVal(matrice,6, 6, 1)
setVal(matrice,7, 6, 4)
setVal(matrice,8, 6, 6)
setVal(matrice,6, 8, 5)
setVal(matrice,7, 8, 8)
afficheMatrice(matrice)
#print(listeValPos(matrice, 8,8))
#print(estBloque(matrice))



# retourne une liste de couple indiquant les coordonnées des cases du sudoku
# pour lesquelles il ne reste qu'une valeur possible
def listeCaseUneValeur(sudo) : 
    res = []
    for indice_ligne in range(getNbLignes(matrice)) :
        for indice_colonne in range(getNbColonnes(matrice)):
            if getVal(sudo, indice_ligne, indice_colonne) is None :
                if len(listeValPos(sudo, indice_ligne, indice_colonne)) == 1 :
                    res.append((indice_ligne,indice_colonne))
    return res
print(listeCaseUneValeur(matrice))


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