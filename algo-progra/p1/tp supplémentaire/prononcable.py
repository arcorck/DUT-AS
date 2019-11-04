def est_prononcable(mot):
    """ fonction qui renvoie un booleen indiquant si le mot est prononcable ou non
    Il est prononcable si il ne contient pas de suite de plus de 4 voyelles ou 4 consonnes
    paramètre : 
        - mot : un mot pour lequel on test sa prononciabilité"""
    prononcable = True
    voyelle = 'aeiouy'
    suite_voyelle = 0
    suite_consonne = 0
    if len(mot) !=  0:
        for char in mot :
            if char in voyelle :
                suite_voyelle += 1
                suite_consonne = 0
            else:
                suite_consonne += 1
                suite_voyelle = 0 
            if suite_voyelle >= 4 or suite_consonne >= 4 :
                prononcable = False 
    else :
        prononcable = False
    return prononcable

assert est_prononcable ('informatique')==True, 'Erreur'
assert est_prononcable ('infoooormatique')==False, 'Erreur'

print(est_prononcable('informatique'))
print(est_prononcable('infoooormatique'))
