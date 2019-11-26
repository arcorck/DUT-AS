#######################################################################
# Feuille de TP 2
# NOM : Bazire Fabrice AS1
#######################################################################



#######################################################################
print("==========================================")
print("Exercice : Dictionnaires")

def premiere_occurence (liste, elem) :
    indice = None
    cpt = 0
    while cpt < len(liste) and indice == None :
        if liste[cpt] == elem :
            indice = cpt
        else : 
            cpt += 1
    return indice
assert premiere_occurence(['a','b','b','a','!'], 'b') == 1, "Erreur"
assert premiere_occurence(['a','b','b','a','!'], 'a') == 0, "Erreur"
assert premiere_occurence(['a','b','b','a','!'], '!') == 4, "Erreur"

def premieres_occurences(liste):
    """ 
    résultat : un dictionnaire dont les clés sont les éléments de
    'liste' et les valeurs l'indice de la première occurence de chaque élément
    """
    dico = {}
    if liste != []:
        for elem in liste : 
            dico[elem] = premiere_occurence(liste, elem)
    return dico

# TESTS
liste=['a','b','b','a','!']
assert premieres_occurences(liste)=={'a':0, 'b':1, '!':4}
assert premieres_occurences([])=={}
print("Bravo ! Vous avez terminé la première question de cet exercice")

def derniere_occurence (liste, elem) :
    indice = None
    cpt = len(liste) - 1
    while cpt >0  and indice == None :
        if liste[cpt] == elem :
            indice = cpt
        else : 
            cpt = cpt - 1
    return indice
assert derniere_occurence(['a','b','b','a','!'], 'b') == 2, "Erreur"
assert derniere_occurence(['a','b','b','a','!'], 'a') == 3, "Erreur"
assert derniere_occurence(['a','b','b','a','!'], '!') == 4, "Erreur"

def dernieres_occurences(liste):
    """ 
    résultat : un dictionnaire dont les clés sont les éléments
    de 'liste' et les valeurs l'indice de la dernière occurence de chaque élément
    """
    dico = {}
    if liste != []:
        for elem in liste : 
            dico[elem] = derniere_occurence(liste, elem)
    return dico

# TESTS
liste=['a','b','b','a','!']
assert dernieres_occurences(liste)=={'a':3, 'b':2, '!':4}
assert dernieres_occurences([])=={}
print("Félicitation ! Vous avez brillamment terminé cet exercice")


#######################################################################
print("==========================================")
print("Exercice : les Avengers")



def intelligenceMoyenne(dico):
    """
    paramètre : un dictionnaire (non vide) dont les clefs sont le nom de personnages,
    et les valeurs des tuples contenant la force (int), 
    l'intelligence (int) et la description (str) de ce personnage
    résultat : l'intelligence moyenne des personnages (float)
    """
    intelligence_moyenne = 0.0
    for elem in dico.values() : 
        intelligence_moyenne += elem[1]
    intelligence_moyenne = intelligence_moyenne / len(dico)
    return intelligence_moyenne

superHero={ 
    'Spiderman' : (5, 5, 'araignée à quatre pattes'),
    'Hulk':(4,7,"Grand homme vert"),
    'Agent 13':(2,3,'agent 13'),
    'M Becker':(2, 9, 'Expert en graphes'),
}

assert intelligenceMoyenne(superHero) == 6.0, "Erreur"


def kikelplusfort(dico):
    """
    paramètre : un dictionnaire (non vide) dont les clefs sont le nom de personnages,
    et les valeurs des tuples contenant la force (int), 
    l'intelligence (int) et la description (str) de ce personnage
    résultat : le nom du personnage le plus fort (str)
    """
    force_max = 0
    plus_fort = ""
    for perso in dico.keys() :
        if dico[perso][0] > force_max:
            force_max = dico[perso][0]
            plus_fort = perso
    return plus_fort

assert kikelplusfort(superHero) == "Spiderman", "Erreur"


def combienDeCretins(dico):
    """
    paramètre : un dictionnaire (non vide) dont les clefs sont le nom de personnages,
    et les valeurs des tuples contenant la force (int), 
    l'intelligence (int) et la description (str) de ce personnage
    résultat : le nombre de personnages dont l'intelligence est inférieure à la moyenne.
    """
    nb_cretins = 0
    intelligence_moyenne = intelligenceMoyenne(dico)
    for perso in dico.keys() : 
        if dico[perso][1] <= intelligence_moyenne :
            nb_cretins += 1
    return nb_cretins

assert combienDeCretins(superHero) == 2, "Erreur"

print("Avez-vous pensé à écrire au moins un test par fonction ?")

#######################################################################
print("==========================================")
print("Exercice : la maison qui rend fou")


mqrf1 = {
    "Abribus":"Astus",
    "Jeancloddus":"Abribus",
    "Plexus":"Gugus",
    "Astus":None,
    "Gugus":"Plexus",
    "Saudepus":None
    }

mqrf2 = {
    "Abribus":"Astus",
    "Jeancloddus":None,
    "Plexus":"Jeancloddus",
    "Astus":"Gugus",
    "Gugus":"Plexus",
    "Saudepus":"Bielorus",
    }

mqrf3 = {
    "Abribus":"Astus",
    "Jeancloddus":None,
    "Plexus":"Saudepus",
    "Astus":"Gugus",
    "Gugus":"Plexus",
    "Saudepus":None,
    }
    
def verifieCoherence(mqrf):
    """
    cette fonction vérifie que chaque guichet donne le formulaire ou renvoie vers un guichet qui existe.
    paramètre : une "maison qui rend fou"
    résultat : un booleen
    """
    res = True
    for (guichet, versguichet) in mqrf.items() :
        if versguichet != None :
            if versguichet not in mqrf.keys() :
                res = False
    return res
assert verifieCoherence(mqrf1) == True, "erreur"
assert verifieCoherence(mqrf2) == False, "Erreur"
assert verifieCoherence(mqrf3) == True, "Erreur"




def conditionDeCesar(mqrf):
    """
    cette fonction vérifie que la mqrf vérifie la condition de César : un guichet qui ne donne pas le formulaire doit renvoyer vers un guichet dont le nom est plus loin dans l'ordre alphabétique
    paramètre : une "maison qui rend fou"
    résultat : un booleen
    """
    res = True
    for (guichet, versguichet) in mqrf.items() :
        if versguichet != None :
            if guichet > versguichet :
                res = False
    return res
print(conditionDeCesar(mqrf1))
print(conditionDeCesar(mqrf2))
print(conditionDeCesar(mqrf3))





def quelGuichet(mqrf, guichet):
    """
    paramètres :
      - mqrf est une maison qui rend fou qui vérifie la condition de César
      - guichet est le nom d'un guichet de la mqrf
    résultat : le nom du guichet qui finit par donner le formulaire
    """
    pass




def possible(mqrf, guichet):
    """
    paramètres :
      - mqrf est une maison qui rend fou
      - guichet est le nom d'un guichet de la mqrf
    résultat : un booléen indiquant s'il est possible d'obtenir le formulaire A-38 dans la mqrf en commençant par s'adresser au guichet
    """
    pass


print("Avez-vous pensé à écrire au moins un test par fonction ?")
