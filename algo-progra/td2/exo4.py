def est_prononcable (mot) :
    """on cherche à savoir ici si un mot est prononcable
    paramètre : 
        - mot pour lequel on veut savoir s'il est prononçable ou non"""
    nb_voyelles = 0
    nb_consonnes = 0
    res = True
    if len(mot) != 0 :
        for lettre in mot :
            if lettre in 'aeiouy' :
                nb_voyelles += 1
                nb_consonnes = 0
            else :
                nb_consonnes += 1
                nb_voyelles = 0
            if nb_voyelles > 3 or nb_consonnes > 3 :
                res = False
    return res

assert est_prononcable("phrase")==True, "Erreur"
assert est_prononcable("schwimmen")==False, "Erreur"

print (est_prononcable("phrase"))
print(est_prononcable("schwimmen"))


def nb_syllabe (mot) :
    """on veut dans cette fonction retourner le nombre de syllabe d'un mot
    paramètre : mot : mot pour lequel on veut comtper le nombre de syllabe"""
    nbsyllabe = 0
    # a finir
assert nb_syllabe("ecouteur") == 3, "Erreur"
assert nb_syllabe("tableau") == 2, "Erreur"