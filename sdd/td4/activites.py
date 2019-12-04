#question 1 : oui on peut utiliser un ensemble comme clé de dictionnaire et et oui on peut aussi l'utiliser comme valeur

trois_amis = {'Camille' : {'Velo', 'Kayak', 'Boxe'}, 'Dominique' : {'Velo'}, 'Claude' : {'Lecture', 'Tricot', 'Boxe', 'Velo'}}

def activite_facvorite (amis) :
    dico_val = {}
    for activites in amis.values() :
        for act in activites :
            if act in dico_val :
                dico_val[act] += 1
            else : 
                dico_val[act] = 1
    max = None
    for nombre_amis in dico_val.values() :
        if max is None or nombre_amis > max : 
            max = nombre_amis
    return dico_val[max]

def activite_de_2_amis (amis, ami1, ami2) :
    activites_des_2_amis = set()
    for nom,activites in amis.items() :
        if nom == ami1 or nom == ami2 :
            for act in activites :
                activites_des_2_amis.add(act) #ici on ajoute sans verification car c'est un ensemble et n'ajoutera pas si il y a doublon
    return activites_des_2_amis

def activites_communes (amis, nom_personne) :
    dico = {}
    for nom, activite in amis.items() :
        if nom != nom_personne :
            dico[(nom_personne, nom)] = activite_de_2_amis(amis, nom_personne, nom)
    #a completer, ne fonctionne pas dans l'état
