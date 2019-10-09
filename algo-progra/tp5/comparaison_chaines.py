def compar_chaines (chaine1, chaine2) :
    """fonction qui compare deux chaines de caractere par leur ordre alphabétique
    resultat = -1 si chaine1 apparait avant chaine2 dans l'alphabet, 0 si elles sont égales et 1 sinon"""
    if chaine1 == chaine2 :
        res = 0
    else :     
        if chaine1 in chaine2 :
            res = -1
        else : 
            if chaine2 in chaine1 :
                res = 1
            else : 
                cpt = 0
                res = 0
                if len(chaine1) < len(chaine2) :
                    taille = len(chaine1)
                else :
                    taille = len(chaine2)
                while cpt < taille :
                    if chaine1[cpt] < chaine2[cpt] :
                        res = -1
                        cpt = taille
                    else : 
                        if  chaine1[cpt] > chaine2[cpt] :
                            res = 1
                            cpt = taille
                        else :
                            cpt += 1
    return res

assert compar_chaines ("bonjour", "bonjour") == 0, "Erreur"
assert compar_chaines ("bonjour", "bon") == 1, "Erreur"
assert compar_chaines ("bon", "bonjour") == -1, "Erreur"
assert compar_chaines ("bontour", "bonjour") == 1, "Erreur"
assert compar_chaines ("bonjour", "bontour") == -1, "Erreur"

print(compar_chaines ("bonjour", "bonjour"))
print(compar_chaines ("bontour", "bonjour"))
print(compar_chaines ("bonjour", "bontour"))
print(compar_chaines ("bonjour", "bon"))
print(compar_chaines ("bon", "bonjour"))
