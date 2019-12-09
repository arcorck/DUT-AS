######################################################################
# Feuille de TP5
# NOM : Fabrice Bazire
#######################################################################

#######################################################################
print("==========================================")
print("Exercice 1 - Utilisation de max et sorted avec clés")


def chaine_la_plus_longue(liste):
    """
    parametre : une liste de str
    resultat : le str le plus long
    """
    res = max(liste, key = len)
    return res

assert chaine_la_plus_longue(['a','aaa', 'bb', 'ss','a']) == 'aaa'
assert chaine_la_plus_longue(['azertyu','aaa', 'bb', 'ss','a']) == 'azertyu'

def fct2 (tuple) :
    return tuple[1]

def tri_selon_deuxieme_composante(liste):
    """
    parametre : une liste de couples
    resultat : la liste triée dans l'ordre croissant de la deuxième composante des couples
    """
    return sorted(liste, key = fct2)

assert tri_selon_deuxieme_composante([(1,5), (2,4), (3,1),(4,2)]) == [(3,1), (4,2), (2,4),(1,5)]


print("   Bravo ! vous avez terminé l'exercice 1 !")


print("==========================================")
print("Exercice 2 -Ultimate Frisbee")

matches = {
    ('Orléans', 'Champignac') : (17,11),
    ('Tours', 'Orléans') : (7, 0),
    ('Champignac', 'Tours') : (10,8),
    ('Caen', 'Orléans') : (3, 13),
    ('Caen', 'Tours') : (6, 2),
    ('Champignac', 'Caen') : (0,0),
    ('Champignac', 'Orléans') : (0,0),
    ('Orléans', 'Tours') : (7, 5),
    ('Tours', 'Champignac') : (4, 0),
    ('Orléans', 'Caen') : (5, 4),
    ('Tours', 'Caen') : (8, 11),
    ('Caen', 'Champignac') : (11, 12),
}

# question 2.1 : 6-2 pour caen

# question 2.2
def vaincus(dico_matchs, equipe):
    """
    renvoie l'ensemble des équipes que 'equipe' a vaincues
    """
    equipes_vaincues = set()
    for (match, score) in dico_matchs.items() :
        if match[0] == equipe :
            if score[0] > score[1] :
                equipes_vaincues.add(match[1]) 
        if match[1] == equipe :
            if score[1] > score[0] :
                equipes_vaincues.add(match[0])
    return equipes_vaincues

assert vaincus(matches, 'Orléans') == {'Champignac', 'Caen', 'Tours'}
assert vaincus(matches, 'Champignac') == {'Caen', 'Tours'}
print('question 2 ok')

# question 2.3
def points_classement(dico_matchs, equipe):
    """
    renvoie le nombre de points de 'equipe' au classement
    """
    nb_points = 0
    for (match, score) in dico_matchs.items() :
        if equipe in match and score[0] == score[1] :
            nb_points += 1
    lesvictoires = vaincus(dico_matchs, equipe)
    nb_points += 3*len(lesvictoires)
    return nb_points

assert points_classement(matches, 'Orléans') == 10
assert points_classement(matches, 'Champignac') == 8
print('question 3 ok')

# question 2.4
def fct3 (t) :
    return max(t)

def match_spectaculaire(dico_matchs):
    """
    renvoie le match où il y a eu le plus de buts
    """
    best_score = max(dico_matchs.values(), key = fct3)
    for match, score in dico_matchs.items() : 
        if best_score == score :
            return match

assert match_spectaculaire(matches) == ('Orléans', 'Champignac')
print('question 4 ok')

# question 2.5  :  -7


# question 2.6
def difference_buts(dico_matchs):
    """
    renvoie dictionnaire dont les clés sont les équipes, 
    et la valeur associée à chaque équipe est sa
    différence de buts.
    """
    res = {}
    for match, score in dico_matchs.items() : 
        if match[0] in res :
            res[match[0]] += score[0]
            res[match[0]] -= score[1]
        else :
            res[match[0]] = score[0] - score[1]
        if match[1] in res :
            res[match[1]] += score[1]
            res[match[1]] -= score[0]
        else :
            res[match[1]] = score[1] - score[0]
    return res

print(difference_buts(matches))
print("question 6 ok")


print("==========================================")
print("Exercice 3 ")

def mystere(intervalle1, intervalle2):
    """
    paramètres : deux intervalles représentés par des tuples :
    renvoie ???
    """
    (debut1, fin1) = intervalle1
    (debut2, fin2) = intervalle2
    return debut1 < fin2 and debut2 < fin1

print(mystere((1, 4), (6, 8))) # == False
print(mystere((7, 9), (2, 4)))  # == False
print(mystere((1, 11), (6, 8))) # == True
print(mystere((8, 14), (5, 10))) # == True

#la fonction mystere verifie que les 2 intervalles se chevauchent 


print("==========================================")
print("Exercice 4- Planning pour un festival")


# Exemples de modélisation de spectacles :

s1 = {'nom': 'JL Aubert', 'debut': 8, 'fin': 10}
s2 = {'nom': '2Be3', 'debut': 11, 'fin': 15}
s3 = {'nom': 'Tyko Moon', 'debut': 5, 'fin': 11}

# Exemple de modélisation de programme :

nikopol = [
    {'nom': 'JL Aubert', 'debut': 8, 'fin': 10}, 
    {'nom': 'JL Aubert', 'debut': 13, 'fin': 17}, 
    {'nom': 'JL Aubert', 'debut': 21, 'fin': 24}, 
    {'nom': 'C Goya', 'debut': 6, 'fin': 9}, 
    {'nom': 'C Goya', 'debut': 10, 'fin': 14}, 
    {'nom': 'C Goya', 'debut': 17, 'fin': 18}, 
    {'nom': '2Be3', 'debut': 11, 'fin': 15}, 
    {'nom': '2Be3', 'debut': 18, 'fin': 21}, 
    {'nom': 'Warhole', 'debut': 8, 'fin': 13}, 
    {'nom': 'Warhole', 'debut': 20, 'fin': 22}, 
    {'nom': 'Tyko Moon', 'debut': 5, 'fin': 11}, 
    {'nom': 'Tyko Moon', 'debut': 13, 'fin': 16}, 
    {'nom': 'Horus', 'debut': 7, 'fin': 18}, 
    {'nom': 'KKDZO', 'debut': 10, 'fin': 12}
    ]


exemple1 = [
    {'nom': 'A', 'debut': 10, 'fin': 14}, 
    {'nom': 'B', 'debut': 12, 'fin': 15}, 
    {'nom': 'C', 'debut': 11, 'fin': 16}, 
    {'nom': 'D', 'debut': 15, 'fin': 17}, 
    {'nom': 'E', 'debut': 13, 'fin': 21}, 
    {'nom': 'F', 'debut': 14, 'fin': 20}, 
    {'nom': 'G', 'debut': 16, 'fin': 16.5}, 
    {'nom': 'H', 'debut': 17, 'fin': 24}, 
]

###########################################
# QUELQUES FONCTIONS UTILES
###########################################

#4.1 : car on peut les trier plus facilement avec une liste

def compatibles(spectacle1, spectacle2):
    """ détermine si les deux spectacles sont compatibles """
    return not mystere((spectacle1['debut'],spectacle1['fin']), (spectacle2['debut'],spectacle2['fin']))

assert compatibles(s1, s2)
assert compatibles(s2, s1)
assert not compatibles(s1, s3)
assert not compatibles(s3, s1)

def tous_compatibles(selection, spectacle):
    """ détermine si spectacle est compatible avec tous les spectacles de la sélection """
    res = True
    for spect in selection :
        if not compatibles(spect, spectacle) :
            res = False
    return res 

assert not tous_compatibles(nikopol, {'nom': '', 'debut': 17, 'fin': 19})
assert tous_compatibles(nikopol, {'nom': '', 'debut': 4, 'fin': 5})


###########################################
# ALGO 1
###########################################
#j'en suis la !!!!

# TRI SELON HEURE DE DEBUT

def tri_selon_debut(programme):
    """ trie les spectacles du programme selon leur heure de début """
    pass

assert tri_selon_debut(exemple1) == [{'nom': 'A', 'debut': 10, 'fin': 14}, {'nom': 'C', 'debut': 11, 'fin': 16}, {'nom': 'B', 'debut': 12, 'fin': 15}, {'nom': 'E', 'debut': 13, 'fin': 21}, {'nom': 'F', 'debut': 14, 'fin': 20}, {'nom': 'D', 'debut': 15, 'fin': 17}, {'nom': 'G', 'debut': 16, 'fin': 16.5}, {'nom': 'H', 'debut': 17, 'fin': 24}]


def prochain_spectacle1(programme, heure = 5):
    """ 
    'programme' est un programme dont les spectacles sont triés par heure de début croissante
    Cette fonction renvoie le premier spectacle qui commence après l'heure indiquée. 
    """
    pass

exemple_trié = tri_selon_debut(exemple1)
assert prochain_spectacle1(exemple_trié, 5) == {'nom': 'A', 'debut': 10, 'fin': 14}
assert prochain_spectacle1(exemple_trié, 12.4) == {'nom': 'E', 'debut': 13, 'fin': 21}
assert prochain_spectacle1(exemple_trié, 18) is None


def selection1(programme):
    pass

proposition1 = selection1(nikopol)
print("Proposition 1 : ", proposition1)


###########################################
# ALGO 2
###########################################


# TRI SELON LA DUREE

def tri_selon_duree(programme):
    """ trie les spectacles du programme selon leur heure de début """
    pass

assert tri_selon_duree(exemple1) == [{'nom': 'G', 'debut': 16, 'fin': 16.5}, {'nom': 'D', 'debut': 15, 'fin': 17}, {'nom': 'B', 'debut': 12, 'fin': 15}, {'nom': 'A', 'debut': 10, 'fin': 14}, {'nom': 'C', 'debut': 11, 'fin': 16}, {'nom': 'F', 'debut': 14, 'fin': 20}, {'nom': 'H', 'debut': 17, 'fin': 24}, {'nom': 'E', 'debut': 13, 'fin': 21}]


def prochain_spectacle(programme, selection):
    """ 
    'programme' est un programme dont les spectacles sont triés (selon un certain critère)
    Cette fonction renvoie le premier spectacle compatible avec tous les autres spactacles de la sélection
    """
    pass


def selection2(programme):
    pass

proposition2 = selection2(nikopol)
print("Proposition 2 : ", proposition2)


###########################################
# ALGO 3
###########################################

def selection3(programme):
    pass
    
proposition3 = selection3(nikopol)
print("Proposition 3 : ", proposition3)


###########################################
# (DEFI) REFACTORISATION
###########################################

def selection(programme, fonction_de_tri):
    pass
    

#  print("Proposition 1 : ", selection(nikopol, tri_selon_debut))
#  print("Proposition 2 : ", selection(nikopol, tri_selon_duree))
#  print("Proposition 3 : ", selection(nikopol, ???))
