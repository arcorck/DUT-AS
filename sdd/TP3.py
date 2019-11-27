from timeit import timeit

######################################################################
# Feuille de TP 3
# NOM : Fabrice Bazire
#######################################################################

#######################################################################
print("==========================================")
print("Exercice 1 - Performance")
def elements_en_commun_v1(liste1, liste2):
    """
    resultat : la liste des éléments communs à 'liste1' et 'liste2'
    """
    en_commun=[]
    for element in liste1:
        if element in liste2:
            en_commun.append(element)
    return en_commun
    
    
def elements_en_commun_v2(liste1, liste2):
    """
    resultat : l'ensemble des éléments communs à 'liste1' et 'liste2'
    """
    ensemble1 = set(liste1)
    ensemble2 = set(liste2)
    en_commun=set()
    for element in ensemble1:
        if element in ensemble2:
            en_commun.add(element)
    return en_commun


from timeit import timeit

taille_des_listes =30
liste1 = [2*n for n in range(taille_des_listes)]
liste2 = [2*n+1 for n in range(taille_des_listes)]

temps1 = timeit('elements_en_commun_v1(liste1, liste2)', globals=globals(),number=100)*1000
temps2 = timeit('elements_en_commun_v2(liste1, liste2)', globals=globals(),number=100)*1000

print("avec n=",taille_des_listes)
print(temps1)
print(temps2)

print("==========================================")
print("Exercice 2 - Fanfare")


candidatures= [("Kim Gordon", "Apito"), ("Superman", "Trompette"), ("Franck Zappa", "Banjo"), ("Chico Science", "Apito"), ("Franck Zappa", "Trompette")] 

def premier_candidat(candidatures, instrument):
    """
    param:
     - candidatures est une liste de tuples (nom, instrum) où nom et instrum sont des str
     - instrument est un str
    return: le nom (str) de la première personne qui a candidaté pour cet instrument
    """
    for (candidat, instru) in candidatures :
        if instru == instrument : 
            return candidat
    return None

assert premier_candidat(candidatures, 'Banjo')== "Franck Zappa","Erreur"
assert premier_candidat(candidatures, 'Apito')== "Kim Gordon", "Erreur"
assert premier_candidat(candidatures, 'Guitarron')== None
print("    Bravo, vous avez terminé la question 2.3 :)")

def tous_candidats(candidatures):
    """
    param: candidatures est une liste de tuples (nom, instrum) où nom et instrum sont des str
    renvoie l'ensemble de toutes les personnes qui ont candidaté pour faire partie de la fanfare.
    """
    res = set()
    for (candidat, instrument) in candidatures :
        res.add(candidat)
    return res


assert tous_candidats(candidatures)== {"Kim Gordon", "Superman", "Franck Zappa", "Chico Science"}

print("    Bravo, vous avez terminé la question 2.4 :)")


def compose_fanfare(candidatures):
    """
    param: candidatures est une liste de tuples (nom, instrun) où nom et instrum sont des str
    renvoie un dictionnaire dont les clés sont les personnes qui seront invitées à faire partie de la fanfare, et les valeurs sont les instruments dont ils joueront.
    Pour cela, nous prenons pour chaque instrument la personne qui a candidaté en premier, sauf si elle joue déjà d'un autre instrument dans la fanfare.
    """
    res = {}
    for (candidat, instrument) in candidatures :
        if candidat not in res.keys():
            res[candidat] = instrument
    return res

# Un petit lien pour les complexités des opérateurs en Python
# https://wiki.python.org/moin/TimeComplexity

# TESTS A COMPLETER ET/OU CORRIGER
assert compose_fanfare(candidatures)== {"Kim Gordon":"Apito"}

#  candidatures2=[('Albert','Apito'), ('Bernard','Trompette'), ('Etienne','Trompette'), ('Carole','Apito'), ('Fanny', 'Apito'), ('Albert','Saxophone'),('Etienne','Trompette'), ('Dalida','Saxophone'), ('Bernard','Piano'), ('Carole','Piano')]
#  assert compose_fanfare(candidatures2) == ??
#  print("    Très bien ! Vous avez terminé la question 2.6")

def candidats_malheureux(candidatures):
    """
    param: candidatures est une liste de tuples (nom, instrun) où nom et instrum sont des str
    renvoie l'ensemble des candidats qui n'ont pas été retenus pour la fanfare
    """
    pass

# TESTS A COMPLETER ET/OU CORRIGER
#  assert candidats_malheureux(candidatures)== ??
#  assert candidats_malheureux(candidatures2)== ??
#  print("    Parfait !! Vous pouvez passer à l'exercice suivant")

print("==========================================")
print("Exercice 3 - Cuisine")

# EXEMPLES A COMPLETER ET/OU CORRIGER
#  recetteCrepe={ ?? } # A COMPLETER
magasin1={'oeufs':0.52, 'farine':1.15, 'lait':5, 'sucre':4}
magasin2={'oeufs':1,  'lait':15, 'sucre':6}


def recette_possible(recette, magasin):
	""" 
	Indique si on peut se procurer dans le 'magasin' les ingrédients nécessaires à la 'recette'
	'recette' est un dictionnaire clés=nom des ingrédients valeurs=quantité nécessaire
	'magasin' est un dictionnaire clés=ingrédients disponibles valeurs=prix d'une quantité unitaire de l'ingrédient
	"""
	pass
    
    
# TESTS A COMPLETER ET/OU CORRIGER SUIVANT VOS DONNÉES
#  assert recette_possible(recetteCrepe,magasin1)
#  assert not recette_possible(recetteCrepe,magasin2) 
print("   Bravo, vous avez terminé la première question de cet exercice ")

def prix_recette(recette, magasin):
	""" 
	Calcule et retourne le prix total pour acheter les ingredients de la 'recette' dans un 'magasin'
	Rque : on suppose que recette_possible(recette,magasin)
	'recette' est un dictionnaire clés=nom des ingrédients valeurs=quantité nécessaire
	'magasin' est un dictionnaire clés=ingrédients disponibles valeurs=prix d'une quantité unitaire de l'ingrédient
	"""
	pass

# TESTS A COMPLETER ET/OU CORRIGER SUIVANT VOS DONNÉES
# ATTENTION ! ON NE FAIT PAS DE TEST D'ÉGALITÉ AVEC DES FLOTTANTS

#  assert abs(prix_recette(recetteCrepe, magasin1)-4.35)<=0.01

print("   Parfait :) Vous pouvez passer à l'exercice suivant ! ")
print("========================================================\n")

########################################################################
# Exercice : La fanfare fait un rappel
########################################################################

print("==========================================")
print("Exercice 4 - Le retour de la fanfare")

#  besoins= ??

exemple_candidatures = [ ('Albert','Triangle'), ('Fanny','Triangle'), ('Gérard','Clarinette'), ('Albert','Clarinette'), ('Gérard','Hélicon'), ('Basile','Triangle'), ('Carole','Triangle'), ('David','Triangle'), ('Henri','Hélicon'), ('Basile','Clarinette'), ('Isaline', 'Clarinette')]


# proposition de modélisation de la fanfare

#  exemple_fanfare= ??


    



