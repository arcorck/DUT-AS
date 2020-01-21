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
def syracuse (n) :
    res = []
    act = n
    if n > 0 :
        res.append(n)
        while act != 1 :
            if act % 2 == 0 :
                res.append(act//2)
                act = act // 2
            else : 
                res.append(3*act+1)
                act = 3*act+1
    else :
        res = None
    return res

assert syracuse(1) == [1], "Erreur"
assert syracuse(2) == [2,1], "Erreur"
assert syracuse(3) == [3,10,5,16,8,4,2,1], "Erreur"
assert syracuse(5) == [5,16,8,4,2,1], "Erreur"
assert syracuse(0) == None, "Erreur"


print("La longeur de syracuse de 27 est de :", len(syracuse(27)))


# Exercice 5 - mot de passe
########################################################################
def nb_char_sup_8 (mdp):
    return len(mdp)>=8
assert nb_char_sup_8("bonjour") == False, "Erreur"
assert nb_char_sup_8("bonjourbonjour") == True, "Erreur"
assert nb_char_sup_8("") == False, "Erreur"

def au_moins_un_chiffre(mdp) :
    cpt = 0 
    res = False
    while cpt < len(mdp) and res == False :
        if mdp[cpt].isdecimal() :
            res = True
        else :
            cpt += 1
    return res
assert au_moins_un_chiffre("bonjour1") == True, "Erreur"
assert au_moins_un_chiffre("bonjour") == False, "Erreur"
assert au_moins_un_chiffre("") == False, "Bonjour"

def aucun_espace (mdp) :
    cpt = 0
    res = True
    while cpt < len(mdp) and res == True : 
        if mdp[cpt] == ' ':
            res = False
        else : 
            cpt += 1
    return res
assert aucun_espace("bonjour") == True, "Erreur"
assert aucun_espace("bonjour toi") == False, "Erreur"
assert aucun_espace("") == True, "Erreur"

def au_moins1_majuscule(mdp):
    res = False
    cpt = 0
    while cpt < len(mdp) and res == False : 
        if mdp[cpt].isupper() :
            res = True
        else :
            cpt += 1
    return res
assert au_moins1_majuscule("Bonjour") == True, "Erreur"
assert au_moins1_majuscule("bonjour") == False, "Erreur"
assert au_moins1_majuscule("") == False, "Erreur"

def deux_maj_consecutives(mdp):
    res = False
    nb_maj = 0
    cpt = 0
    while cpt < len(mdp) and res == False :
        if nb_maj > 1 :
            res = True
        if mdp[cpt].isupper():
            nb_maj += 1
        else :
            cpt += 1
    return res
assert deux_maj_cons("BOnjour") == True, "Erreur"
assert deux_maj_cons("BonJour") == False, "Erreur"
assert deux_maj_cons("") == False, "Erreur"

def pas_de_ponctuation(mdp):
    res = True
    cpt = 0
    while cpt < len(mdp) and res == True :
        if mdp[cpt] in (",.?;:/!§-_") : 
            res = False
        else : 
            cpt += 1
    return res 
assert pas_de_ponctuation("bonjour,toi") == False, "Erreur"
assert pas_de_ponctuation("bonjourtoi") == True, "Erreur"
assert pas_de_ponctuation("") == True, "Erreur" 

def dialogue_mot_de_passe () :
    print ("Vous allez entrer un mot de passe, quelques indications : \n  - il doit etre long au moins de 8 caractères\n  - il ne doit pas contenir d'espaces\n  - il doit contenir au moins un chiffre et au moins une majuscule\n  - il ne doit pas contenir deux majuscules consecutives\n  - et enfin il ne doit pas contenir de signes de ponctuation (,.?;:/!§-_)")
    mdp = input("Veuillez entrer un mot de passe : ")
    while not nb_char_sup_8 (mdp) or not au_moins_un_chiffre(mdp) or not aucun_espace (mdp) or not au_moins1_majuscule(mdp) or not deux_maj_consecutives(mdp) or not pas_de_ponctuation(mdp) :
        mdp = input("Le Mot de passe est faux !!\nVeuillez entrer un mot de passe : ")
    print("Le mot de passe est validé")
    file = open("mdpUltraSecret.txt", "a")
    file.write(mdp)
    file.close()

dialogue_mot_de_passe()