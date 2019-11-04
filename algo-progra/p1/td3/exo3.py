def char_sur_n (mot, chiffre):
    """retourne le mot avec une lettre sur chiffre (une lettre sur deux par exemple)
    parametres : mot designe le mot pour lequel on applique la fonction et chiffre le chiffre pour lequel on applique la fonction"""
    res = ""
    if len(mot) != 0 and chiffre > 0 :
        for i in range (0, len(mot), chiffre) :
            res += mot[i]
    return res

assert char_sur_n ('bonjour', 6) == "br", "Erreur"
assert char_sur_n ('bonjour', 3) == "bjr", "Erreur"
assert char_sur_n ('bonjour', 2) == "bnor", "Erreur"
assert char_sur_n ('', 3) == "", "Erreur"
assert char_sur_n ('bonjour', -6) == "", "Erreur"

print("char_sur_n : ")
print(char_sur_n ('bonjour', 6))
print(char_sur_n ('bonjour', 3))
print(char_sur_n ('bonjour', 2))

print("\n\nsous_chaine : ")

def sous_chaine (mot, debut, long):
    """cette fonction renvoie une sous chaine de mot qui commence à l'indice debut du mot et de taille long"""
    res = ""
    cpt = 0
    if debut >= 0 and debut < len(mot) :
        if len(mot) != 0 :
            for i in range(debut, long+debut) :
                if i < len(mot) :
                    res += mot[i]
    return res

assert sous_chaine('bonjour', 4, 6)=='our', "Erreur"
assert sous_chaine('bonjour', 2, 3)=='njo', "Erreur"
assert sous_chaine('', 1, 5) == '', 'Erreur'
assert sous_chaine('bonjour', 4, 28)=='our', "Erreur"
assert sous_chaine('bonjour', 50, 3)=='', 'Erreur'
assert sous_chaine ('informatique', 2, 3)=="for", 'Erreur'
print(sous_chaine('bonjour', 4, 6))
print(sous_chaine('bonjour', 2, 3))
print(sous_chaine('bonjour', 4, 28))
print(sous_chaine ('informatique', 2, 3))

print("\n\nrenversement : ")

def renversement(mot):
    """cette fonction prend un mot et echange les lettres 2 par 2 (info --> niof)
    parametre : mot : mot sur lequel la fonction est testée"""
    res = ""
    cpt = 0
    if len(mot) != 0:
        while cpt < len(mot)-1 :
            res += mot[cpt+1]
            res += mot[cpt]
            cpt += 2
        if cpt < len (mot) :
            res += mot[cpt]
    return res 
assert renversement("informatique")=="niofmrtaqieu", "Erreur"
assert renversement("bonjour") == "objnuor", "Erreur"
assert renversement("")=="", "Erreur"
print(renversement("informatique"))
print(renversement("bonjour"))