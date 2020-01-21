#question 1 : oui on peut utiliser un ensemble comme clé de dictionnaire et et oui on peut aussi l'utiliser comme valeur

trois_amis = {'Camille' : {'Velo', 'Kayak', 'Boxe'}, 'Dominique' : {'Velo'}, 'Claude' : {'Lecture', 'Tricot', 'Boxe', 'Velo'}}

def activite_favorite (amis) :
    dico_val = {}
    for activites in amis.values() :
        for act in activites :
            if act in dico_val :
                dico_val[act] += 1
            else : 
                dico_val[act] = 1
    max = None
    act_fav = ''
    for act,nombre_amis in dico_val.items() :
        if max is None or nombre_amis > max : 
            max = nombre_amis
            act_fav = act
    return act_fav
assert activite_favorite(trois_amis) == 'Velo', 'Erreur'

def activite_de_2_amis (amis, ami1, ami2) :
    activites_des_2_amis = set()
    for nom,activites in amis.items() :
        if nom == ami1 :
            for act in activites :
                if act in amis[ami2] :
                    activites_des_2_amis.add(act) #ici on ajoute sans verification car c'est un ensemble et n'ajoutera pas si il y a doublon
        if nom == ami2 :
            for act in activites :
                if act in amis[ami1] :
                    activites_des_2_amis.add(act) #ici on ajoute sans verification car c'est un ensemble et n'ajoutera pas si il y a doublon
    return activites_des_2_amis
assert activite_de_2_amis(trois_amis, 'Camille', 'Claude') == {'Velo', 'Boxe'}, 'Erreur'

def activites_communes (amis, nom_personne) :
    dico = {}
    for nom, activite in amis.items() :
        if nom != nom_personne :
            dico[(nom_personne, nom)] = activite_de_2_amis(amis, nom_personne, nom)
    #a completer, ne fonctionne pas dans l'état
