################################################
## Exercice sur les facture                   ##
################################################

def factures(liste_commandes):
    '''
    paramètre: liste_commandes = liste des commandes 
    resultat: retourne la liste des clients avec le montant total de leur commande
    '''
    res = []
    total = 0
    for elem in liste_commandes :
        for articles in elem[2] :
            total += articles[2] * articles[1]
        res.append((elem[0], elem[1], total))
        total = 0
    return res
assert factures([(123 , "Dupont", [("Verre", 6, 2.4), ("Assiette", 6, 1.5)]), (125, "Durand", [("vase", 1, 10.0)])]) == [(123, 'Dupont', 23.4), (125, 'Durand', 10.0)], "Erreur"
assert factures([]) == [], "Erreur"



def taille_max_dans_liste_de_commandes(liste):
    """
    paramètre: liste = liste de commandes 
    résultat: renvoie la taille de l'article le plus long (assiette est plus long que verre par sa chaine de caractere)
    """
    max = None
    for elem in liste : 
        for elem2 in elem[2] :
            if max == None or max < len(elem2[0]) :
                max = len(elem2[0])
    return max
assert (taille_max_dans_liste_de_commandes([(123,"Dupont",[("Verre",6,2.4),("Assiette",6,1.5)]),(125,"Durand",[("vase",1,10.0)])])) == 8, "Erreur"
assert (taille_max_dans_liste_de_commandes([])) == None, "Erreur"



def affiche_factures(liste_commandes):
    '''
    paramètre: liste de commandes
    resultat: affiche une facture detaille pour chaque client avec les articles, leurs quantités, leurs prix unitaires et leur prix totaux
    '''
    taille_plus_long_mot = taille_max_dans_liste_de_commandes(liste_commandes)
    total = 0.0
    total_client = 0.0
    for elem in liste_commandes :
        print("--------------------------------------")
        print("numéro : " + str(elem[0]) + ("Nom : ").rjust(18) + str(elem[1]))
        print("produit" + ("qte").rjust(15) + ("prix").rjust(7) + ("total").rjust(7))
        for elem2 in elem[2]:
            print(elem2[0], end='')
            for i in range (taille_plus_long_mot + 14):
                if len(elem2[0]) + i == 20 :
                    print((str(elem2[1])).rjust(i) + "*", end='')
            prix = (elem2[2])
            prix = format(prix, '5.2f')
            print(str(prix).rjust(8) + "=", end='')
            total = elem2[1]*elem2[2]
            total = format(total, '5.2f')
            print(total.rjust(7))
            total_client += float(total)
            total = 0.0
        print("                               -------")
        total_client = format(total_client, '5.2f')
        print("total                          " + str(total_client))
        total_client = 0.0

print(affiche_factures([(123,"Dupont",[("Verre",6,2.4),("Assiette",6,1.5)]),(125,"Durand",[("vase",1,10.0)])]))
