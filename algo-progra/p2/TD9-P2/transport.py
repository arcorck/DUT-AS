#! /usr/bin/python3
from math import *
def Personne(nom,age,moyen):
    """
    creer une personne qui doit être représentée par un dictionnaire
    paramètres: nom:
                age:
                moyen:
    resultat:
    """
    dico = {}
    dico['nom_pers'] = nom
    dico['age_pers'] = age
    dico['moyen_transport'] = moyen
    return dico

def get_nom(pers):
    """
    retourne le nom de la personne
    """
    return pers['nom_pers']

def get_age(pers):
    """
    retourne l'age de la personne
    """
    return pers['age_pers']
        
def get_moyen_transport(pers):
    """
    retourne le moyen de transport utilisé par la personne
    """
    return pers['moyen_transport']

def set_nom(pers,nom):
    """
    change le nom de la persone
    """
    pers['nom_pers'] = nom

def set_age(pers,age):
    """
    change l'age de la personne
    """
    pers['age_pers'] = age

def set_moyen_transport(pers,moyen):
    """ 
    change le moyen de transport de la personne
    """
    pers['moyen_transport'] = moyen

def affiche_personne(pers):
    """
    affiche une personne
    """
    print('-'*10)
    print('Nom:',get_nom(pers))
    print('Age:',get_age(pers))
    print('Moyen de transport:', get_moyen_transport(pers))
    print('-'*10)


def lire_fichier_personnes(nom_fic):
    """
    lit une liste de personnes contenue dans un fichier
    """
    fic=open(nom_fic)
    liste_pers=[]
    for ligne in fic:
        [nom,age,moyen_trans]=ligne[:len(ligne)-1].split(',')
        liste_pers.append(Personne(nom,age,moyen_trans))
    fic.close()
    return liste_pers

def affiche_liste_personnes(liste_pers):
    """
    affiche une liste de personnes
    """
    for personne in liste_pers :
        affiche_personne(personne)

def age_moyen_utilisateur_transport(liste_pers,nom_moyen_transport):
    """
    retourne l'age moyen des personnes qui utilise comme moyen de transport
    celui passé en paramètres. Si aucune personne n'utilise ce moyen de transport
    la fonction doit retourner -1
    """
    moyenne_age = 0
    nb_pers = 0
    for personne in liste_pers :
        if get_moyen_transport(personne) == nom_moyen_transport : 
            nb_pers +=1
            moyenne_age += get_age(personne)
    if nb_pers != 0 :
        moyenne_age = moyenne_age / nb_pers
    else :
        moyenne_age = -1
    return moyenne_age


def liste_moyens_transport(liste_pers):
    """
    retourne sous la forme d'une liste de chaines de caractères la liste des 
    moyens de transport utilisés par les personne de listePers
    """
    liste_moyens_transport = []
    for personne in liste_pers : 
        if get_moyen_transport(personne) not in liste_moyens_transport : 
            liste_moyens_transport.append(get_moyen_transport(personne))
    return liste_moyens_transport

### programme principal
if __name__=='__main__':
    lire_fichier_personnes('personnes.txt')
    #ajoutez vos appels aux fonctions sur les personnes
