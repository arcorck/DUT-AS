################################################
## Exercice sur les facture                   ##
################################################

def factures(liste_commandes):
    '''
    paramètre:
    resultat:
    '''
    res = []
    total = 0
    for elem in liste_commandes :
        for articles in elem[2] :
            total += articles[2] * articles[1]
        res.append((elem[0], elem[1], total))
        total = 0
    return res

#print(factures([(123 , "Dupont", [("Verre", 6, 2.4), ("Assiette", 6, 1.5)]), (125, "Durand", [("vase", 1, 10.0)])]))

#assert(factures([(123,"Dupont",[("Verre",6,2.4),("Assiette",6,1.5)]),(125,"Durand",[("vase",1,10.0)])])==[(123, 'Dupont', 23.4), (125, 'Durand', 10.0)])
# vos tests

def affiche_factures(liste_commandes):
    '''
    paramètre:
    resultat:
    '''
    res = ""
    total = 0.0
    for elem in liste_commandes :
       res += ("---------------------\n")
       res += ("numéro : ")
       res += str(elem[0])
       res += ("nom : ").rjust(18)
       res += str(elem[1])
       res += ("\nproduit")        
       res += ("qté").rjust(15)    
       res += ("prix").rjust(7)
       res += ("total\n").rjust(7)
       for elem2 in elem[2]:
           res += elem2[0]
           res += (str(elem2[1])).rjust(15)
           res += (str(elem2[2])).rjust(7)
           total = elem2[1]*elem2[2]
           total = format(total, '5.2f')
           res += total.rjust(7)
           res += "\n"
           total = 0.0
    return res


print(affiche_factures([(123,"Dupont",[("Verre",6,2.4),("Assiette",6,1.5)]),(125,"Durand",[("vase",1,10.0)])]))
