########################################################################
#   Feuille de TP1
#   NOM : Bazire Fabrice
########################################################################


# Exercice 1 - Mémoire
########################################################################
# Question 1
def f(a):
    a=a+1
    # ICI
    return a
x=3
y=f(x)
z=f(y)

# Question 2
liste1 = [1, 3, 5, 9]
liste2 = [0, 2, 4]
liste3 = liste1 + liste2
liste2.append (6) # ICI

# Questions 3 et 4
def augmenteTous (liste):
    """Cette fonction augmente de 1 les valeurs des élements de la liste
    paramètre : une liste de nombre
    resultat : rien du tout !!!"""
    for i in range (len(liste)):
        liste[i] = liste[i]+1 # ICI

maListe = [5, 3, 7, 9]
augmenteTous(maListe)
print(maListe)


# Exercice 2 - Fonction sur les chaînes de caractère
########################################################################
def deux_maj_cons (string):
    cpt = 0
    res = False
    if string != "" :
        while res == False and  cpt < len(string) - 1 :
            if string[cpt].isupper() and string[cpt+1].isupper():
                res = True
            cpt += 1
    return res
assert deux_maj_cons ("COUCOU") == True, "Erreur"
assert deux_maj_cons ("coucou") == False, "Erreur"
assert deux_maj_cons ("coucouTT") == True, "Erreur"
assert deux_maj_cons ("coUCou") == True, "Erreur"
assert deux_maj_cons ("TcoucouT") == False, "Erreur"


# Exercice 3 - Slicing
########################################################################
liste = [1,2,3,4,5,6,7,8,9]
print("Exercice 3\n liste : ", liste)
print(liste[:3])
print(liste[2:-2])
print(liste[:(len(liste)//2)])
print(liste[(len(liste)//2)])
print(liste[(len(liste)//2) : (len(liste)//2)+5])


# Exercice 4 - Suite de syracuse
########################################################################


# Exercice 5 - mot de passe
########################################################################
