from matriceAPI3 import *
import copy

#-----------------------------------------
# entrées sorties sur les matrices
#-----------------------------------------
def sauveMatrice(matrice,nomFic):
    '''
    '''
    fic=open(nomFic,'w')
    ligne=str(getNbLignes(matrice))+','+str(getNbColonnes(matrice))+'\n'
    fic.write(ligne)
    for i in range(getNbLignes(matrice)):
        ligne=''
        for j in range(getNbColonnes(matrice)-1):
            val=getVal(matrice,i,j)
            if val==None:
                ligne+=','
            else:
                ligne+=str(val)+','
                val=getVal(matrice,i,j+1)
            if val==None:
                ligne+='\n'
            else:
                ligne+=str(val)+'\n'
    fic.write(ligne)
    fic.close()

def chargeMatrice(nomFic,typeVal='int'):
    '''
    '''
    fic=open(nomFic,'r')
    ligneLinCol=fic.readline()
    listeLinCol=ligneLinCol.split(',')
    matrice=Matrice(int(listeLinCol[0]),int(listeLinCol[1]))
    i=0  
    for ligne in fic:
        listeVal=ligne.split(",")
        j=0
        for elem in listeVal:
            if elem=="" or elem=="\n":
                setVal(matrice,i,j,None)
            elif typeVal=='int':
                setVal(matrice,i,j,int(elem))
            elif typeVal=='float':
                setVal(matrice,i,j,float(elem))
            elif typeVal=='bool':
                setVal(matrice,i,j,bool(elem))
            else:
                setVal(matrice,i,j,elem)
            j+=1
        i+=1
    return matrice

def afficheLigneSeparatrice(matrice,tailleCellule=4):
    '''
    Affichage d'une matrice
    fonction annexe pour afficher les lignes séparatrices
    '''
    print()
    for i in range(getNbColonnes(matrice)+1):
        print('-'*tailleCellule+'+',end='')
    print()
   
def afficheMatrice(matrice,tailleCellule=4):
    '''
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
   
#--------------------------------
# fonctions sur les labyrinthes
#--------------------------------

def marquageDirect(calque,mat,val,marque):
    '''
    marque avec la valeur marque les éléments du calque tel que la valeur 
    correspondante n'est pas un mur (de valeur differente de 1) et 
    qu'un de ses voisins dans le calque à pour valeur val
    la fonction doit retourner True si au moins une case du calque a été marquée
    '''
    calque_marqué = False
    if getNbLignes(calque) == getNbLignes(mat) and getNbColonnes(calque) == getNbColonnes(calque):
        for lig in range(getNbLignes(calque)) : 
            for col in range(getNbColonnes(calque)) :
                if getVal(mat, lig, col) != 1:
                    if (lig > 0) :
                        if getVal(calque, lig-1, col) == val :
                            setVal(calque, lig, col, marque)
                            calque_marqué == True
                    if (lig < getNbLignes(calque) - 1) :
                        if getVal(calque, lig+1, col) == val :
                            setVal(calque, lig, col, marque)
                            calque_marqué == True
                    if (col > 0) :
                        if getVal(calque, lig, col-1) == val :
                            setVal(calque, lig, col, marque)
                            calque_marqué == True
                    if (col < getNbColonnes(calque)-1) :
                        if getVal(calque, lig, col+1) == val :
                            setVal(calque, lig, col, marque)
                            calque_marqué == True
    return calque_marqué

def estAccessible(mat,pos1,pos2):
    '''
    verifie qu'il existe un chemin entre pos1 et pos2 dans la matrice mat
    '''
    if getVal(mat, pos1[0], pos1[1]) != 1 and getVal(mat, pos2[0], pos2[1]) != 1 and getVal(mat, 0, 0) != 1 :
        calque = Matrice(getNbLignes(mat), getNbColonnes(mat))
        setVal(calque, pos1[0], pos1[1], 1)
        res = marquageDirect(calque, mat, 1, 1)
        while res :
           res = marquageDirect(calque, mat, 1, 1)
        afficheMatrice(calque)
        return getVal(calque, pos2[0], pos2[1]) == 1 
    else : 
        return False

matrice = {'lignes': 9, 'colonnes': 9, 'valeurs': [2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3]}
afficheMatrice(matrice)
def labyrintheValide(mat):
    '''
    verifie qu'il existe un chemin entre la case en haut à gauche et la case
    en bas à droite de la matrice
    '''
    return estAccessible(mat, (0,0), ((getNbLignes(mat) - 1), (getNbColonnes(mat) - 1)))

def estAccessible2(mat,pos1,pos2):
    '''
    vérifie l'accessibilité entre deux positions mais en calculant le nombre de cases
    depuis le point de départ
    la fonction retourne le calque si les deux cases sont accessibles et None sinon
    '''
    calque = Matrice(getNbLignes(mat), getNbColonnes(mat))
    setVal(calque, pos1[0], pos1[1], 1)
    while marquageDirect(calque, mat, 1, 1) and getVal(calque, (getNbLignes(mat) - 1),(getNbColonnes(mat) - 1)) != 1:
        marquageDirect(calque, mat, 1, 1)
    marque = 0
    for ligne in range(getNbLignes(calque)) :
        for colonne in range(getNbColonnes(calque)) :
            if getVal(calque, ligne, colonne) == 1 :
                marque += 1
                setVal(calque, ligne, colonne, marque)
    if getVal(calque, pos2[0], pos2[1]) == 1 and getVal(calque, pos1[0], pos1[1]) == 1 :
        return calque
    else : 
        return None

def cheminDecroissant(calque,pos1,pos2):
    '''
    recherche un chemin décroissant à partir de pos1 vers pos2
    le chemin est une liste de positions
    la fonction suppose que le calque contient effectivement les valeurs permettant
    de retrouver ce chemin
    '''
    pass

def plusCourtChemin(matrice,pos1,pos2):
    '''
    recherche le plus court chemin entre pos1 et pos2. 
    s'il n'y pas de chemin entre ces deux positions la fonction retourne None
    sinon elle retourne le chemin
    '''
    pass
