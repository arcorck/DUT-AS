def exo1 (liste, nb) :
    cpt = 0 #compte le nombre d'elements dans la liste plus grands que nb
    for elem in liste : #elem prend a chaque tour de boucle une valeur differente de liste 
        if elem > nb :
            cpt += 1
    return cpt >= 2

print(exo1([10,5,3,8,2], 5))
print(exo1([10,5,3,8,2], 9))

#1) exo1([10,5,3,8,2], 5) : True
#   exo1([10,5,3,8,2], 9) : False

#2) invariant : cpt = nombre d'elemnts de liste superieur à nb 

#3) En une phrase, cette fonction calcule le nombre d'elements dans la liste supérieur à nb, si il y'en a plus de 1, alors la fonction retourne Vrai

#4) avec indice 
def exo1_indice (liste, nb) :
    cpt = 0 #compte le nombre d'elements dans la liste plus grands que nb
    for indice in range(len(liste)) : #elem prend a chaque tour de boucle une valeur differente de liste 
        if liste[indice] > nb :
            cpt += 1
    return cpt >= 2

print("\n",exo1_indice([10,5,3,8,2], 5))
print(exo1_indice([10,5,3,8,2], 9))


#4) avec while 
def exo1_while (liste, nb) :
    cpt = 0 #compte le nombre d'elements dans la liste plus grands que nb
    indice = 0
    while indice < (len(liste)) and cpt < 2 : #elem prend a chaque tour de boucle une valeur differente de liste 
        if liste[indice] > nb :
            cpt += 1
        indice += 1
    return cpt >= 2

print("\n",exo1_while([10,5,3,8,2], 5))
print(exo1_while([10,5,3,8,2], 9))