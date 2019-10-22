##########################################################
### IMPLEMENTEZ CI-DESSOUS VOS FONCTIONS               ###
### ATTENTION NE MODIFIEZ PAS LES NOMS DES FONCTIONS   ###
### COMPLETEZ LES DOCSTRINGS                           ###  
##########################################################

# exercice 1
def affiche_classement(scores,joueurs):
    """
    affiche le classement des joueurs
    paramètres:
    pas de résultat
    """
    ...
    
# exercice 2
def decroissant(scores):
    """
    vérifie qu'une liste des scores est bien triées dans l'ordre décroissant
    paramètres:
    résultat:
    """
    ...
    
    
#exercice 3
def meilleur_score_joueur(nom_joueur,scores,joueurs):
    """
    retourne le meilleur score d'un joueur -1 si le joueur n'apparait pas dans 
    les meilleurs scores
    paramètres:
    résultat:    
    """
    ...
    
# exercice 4 6 et 7bis
def consulter_joueur(scores,joueurs):
    """
    Petit menu permettant de d'afficher différentes information sur un joueur
    """
    nom_joueur=input('Entrez un nom de joueur ')
    print('Pour afficher son meilleur score tapez 1')
    print('Pour afficher le nombre de fois où il apparait dans les meilleurs scores tapez 2')
    rep=''
    while rep not in ['1','2','3']:
        rep=input('Veuillez entrez votre réponse ')
    if rep=='1':
        print('Le meilleur score de',nom_joueur,'est',meilleur_score_joueur(nom_joueur,scores,joueurs))
    elif rep=='2':
        print(nom_joueur,'apparait',nb_fois_meilleur(nom_joueur,scores,joueurs),'fois dans les meilleurs scores')
    else:
        print('Le meilleur classement de',nomJoueur,'est',meilleurClassementJoueur(nomJoueur,scores,joueurs))    
    
# exercice 5
def nb_fois_meilleur(nom_joueur,scores,joueurs):
    """
    calcule combien de fois un joueur (dont le nom est passé en paramètre) 
    apparaît dans les meilleurs scores
    paramètres:
    résultat:    
    """
    ...
    
# exercice 6

# exercice 7
def meilleur_classement_joueur(nom_joueur,scores,joueurs):
    """
    donne le meilleur classement d'un joueur (-1 s'il n'apparait pas dans le classement)
    paramètres:
    résultat:    
    """
    ...    

# exercice 8
def placeScore(nouveau_score,scores):
    """
    donne l'indice ou placer le nouveau score dans la liste des scores
    paramètres:
    résultat:    
    """
    ...   

# exercice 9
def ajouter_score(nouveau_score, nom_joueur, scores,joueurs):
    """
    ajoute le nouveau score d'un joueur dans la liste des scores 
    (et la liste des joueurs)
    paramètres:
    résultat cette fonction modifie directement scores et joueurs mais ne retourne rien    
    """
    ...

# exercice 10
def ajouter_score_limite(nouveau_score, nom_joueur, scores,joueurs,taille_max):    """
    ajoute le nouveau score d'un joueur dans la liste des scores 
    (et la liste des joueurs) en limitant le nombre de places à taille_max
    paramètres:
    résultat cette fonction modifie directement scores et joueurs mais ne retourne rien    
    """
    ...
    

# exercice 11
def sauver_score(nom_fic,scores,joueurs):
    """
    sauvegarde dans un fichier texte les scores (avec le nom de joueur associé)
    paramètres:
    résultat aucun mais créer un fichier    
    """
    ...
    
# exercice 12
def restaurer_score(nom_fic,scores,joueurs):
    """
    charge la liste des scores et des noms de joueurs à partir d'un fichier texte
    paramètres:
    résultat aucun mais la fonction stocke les informations dans scores et joueurs
    """
    ...
    
# exercice 13
def scores_HTML(nom_fic,scores,joueurs):
    """
    sauvegarde dans un fichier HTML sous la forme d'un tableau
    les scores (avec le nom de joueur associé)
    paramètres:
    résultat aucun mais créer un fichier    
    """
    ...
    
