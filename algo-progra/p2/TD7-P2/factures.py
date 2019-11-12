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

print(factures([(123 , "Dupont", [("Verre", 6, 2.4), ("Assiette", 6, 1.5)]), (125, "Durand", [("vase", 1, 10.0)])]))

#assert(factures([(123,"Dupont",[("Verre",6,2.4),("Assiette",6,1.5)]),(125,"Durand",[("vase",1,10.0)])])==[(123, 'Dupont', 23.4), (125, 'Durand', 10.0)])
# vos tests

def affiche_factures(liste_commandes):
    '''
    paramètre:
    resultat:
    '''
    pass

# affiche_factures([(123,"Dupont",[("Verre",6,2.4),("Assiette",6,1.5)]),(125,"Durand",[("vase",1,10.0)])])
