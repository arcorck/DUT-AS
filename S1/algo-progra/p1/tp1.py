import math

def fonction1 (x,y):
    """ fonction1 fait l'addition de x et y
    parametres : x un nombre et y un autre nombre
    resultat : le resultat du calcul de x+y """
    return x + y

assert fonction1(3,4) == 7; "pb avec fonction1 (3,4)"
help(fonction1)

fonction1(3,4)


def algo1 (a,b,c,d):
    if (a < b) :
        res = a
    else :
        res = b
    if (c < res):
        res = c
    if (d < res):
        res = d
    return res

print("res de algo1 : ", algo1(4,3,2,1))


def algo2(m):
    res = 0
    for v in m:
        if v in ('aeiouy'):
            res = res+1
        else :
            res = res-1
    return res>0

if algo2("balou") :
    print("plus de voyelles que de consonnes dans balou")
else:
    print("plus de consonnes que de voyelles dans balou")
    
if algo2("manger") :
    print("plus de voyelles que de consonnes dans manger")
else:
    print("plus de consonnes que de voyelles dans manger")
         
         
         
def algo3(a,b,c):
    delta = (b*b)-(4*a*c)
    if (delta < 0):
        return ("pas de solutions")
    elif (delta == 0):
        return ("une seule solution : ", (-1*b)/(2*a))
    else:
        return ("deux solutions : ", ((-1*b)+(math.sqrt(delta))/(2*a)), " et ", ((-1*b)-(math.sqrt(delta))/(2*a)))

print(algo3(2,1,-2))
print(algo3(2,-4,2))
print(algo3(3,-2,10))
