def f1 ():
    res = 0 
    for x in 12,2,5,6,9 :
        res = res + x
    return res
#f1 : x prend la valeur 12 puis la valeur 2, puis la valeur 5, puis la valeur 6 et enfin la valeur 9
# elle retourne la somme de ces nombres soit 34
print("somme : ", f1())

def f2 ():
    res = ''
    for c in 'ce matin':
        res = c + res
    return res
#c prend la valeur 'c' puis la valeur 'e' puis la valeur ' ' puis la valeur 'm' puis ...
# elle retournera ce matin à l'envers
print("affichage : ", f2())

def f3 ():
    res = 0 
    for i in range(10):
        res = res + i
    return res
#f3 : i prend la valeur 0 puis la valeur 1, puis la valeur 2, puis la valeur 3 et ce jusqu'à 9
# elle retourne la somme des nombres de 0 à 9 soit 45
print("somme de 0 à 10 : ",f3())

def f4 ():
    res = 0 
    for i in range(2,10):
        res = res + i
    return res
#f4 : i prend la valeur 2 puis la valeur 3, puis la valeur 4, puis la valeur 5 et ce jusqu'à 9
# elle retourne la somme des nombres de 2 à 9 soit 44
print("somme de 2 à 10 : ",f4())

def f5 ():
    res = 0 
    for i in range(1,22,3):
        res = res + i
    return res
#f5 : i prend la valeur 1 puis la valeur 4, puis la valeur 7, puis la valeur 10 puis 13 puis 16 puis 19
# elle retourne la somme des nombres de 1 à 21 par pas de 3 soit 70
print("somme de 1 à 21 par pas de 3 : ",f5())

def f6 ():
    cpt = 0
    for c in 'ce matin':
        cpt = cpt+1
    return cpt
#c prend la valeur 'c' puis la valeur 'e' puis la valeur ' ' puis la valeur 'm' puis ...
#la valeur de retour est en fait la longueur de la chaîne car à chaque tour de boucle donc à chaque lettre, on incrémente un compteur, ici on va obtenir 8
print("longueur de la chaine : ", f6())