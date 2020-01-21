##########################################################
### IMPLEMENTEZ CI-DESSOUS VOS FONCTIONS               ###
### ATTENTION NE MODIFIEZ PAS LES NOMS DES FONCTIONS   ###
### COMPLETEZ LES DOCSTRINGS                           ###  
##########################################################

import os

# exercice 1
def affiche_classement(scores,joueurs):
    """affiche le classement des joueurs
    paramètres: scores = listes des scores (par ordre décroissant) et joueurs = liste des joueurs associés aux scores 
    pas de résultat"""
    if scores != [] and joueurs != [] and len(scores) == len(joueurs):
        for indice in range(len(scores)) :
            print(indice+1, ". ", joueurs[indice], " ", scores[indice])
    else :
        print ("Erreur : soit une des listes est vide soit les listes ne sont pas de la même taille")
    
# exercice 2
def decroissant(scores):
    """vérifie qu'une liste des scores est bien triées dans l'ordre décroissant
    paramètres: liste des scores pour laquelle on va verifier la décroissance
    résultat: booleen indiquant la decroissance (True) ou non (False) de la liste """
    res = True
    if scores != [] :
        for indice in range(1, len(scores)) :
            if scores[indice] >= scores[indice - 1] : 
                res = False
    return res
    
    
#exercice 3
def meilleur_score_joueur(nom_joueur,scores,joueurs):
    """retourne le meilleur score d'un joueur -1 si le joueur n'apparait pas dans 
    les meilleurs scores
    paramètres : nom_joueurs = nom du joueurs pour lequel on veut le meilleur score, scores = liste des meilleurs scores, joueurs = liste des joueurs associés aux meilleurs scores
    résultat : meilleur du joueur nom_joueur ou -1 si le joueur n'apparait pas dans la liste"""
    res = -1
    if scores != [] and joueurs != [] and len(scores) == len(joueurs):
        if nom_joueur in joueurs :
            for indice in range(len(scores)) :
                if joueurs[indice] == nom_joueur and res == -1:
                    res = scores[indice]
        else : 
            print(nom_joueur, "n'apparait pas dans la liste")
    return res
    
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
        print('Le meilleur classement de',nom_joueur,'est',meilleur_classement_joueur(nom_joueur,scores,joueurs))    
    
# exercice 5
def nb_fois_meilleur(nom_joueur,scores,joueurs):
    """calcule combien de fois un joueur (dont le nom est passé en paramètre) 
    apparaît dans les meilleurs scores
    paramètres : nom_joueurs = nom du joueur pour lequel on veut le nombre d'apparition, scores = liste des meilleurs scores, joueurs = liste des joueurs associés aux meilleurs scores
    résultat : nombre d'apparition du joueur dans la liste des scores, -1 s'il n'apparait pas"""
    res = 0
    if scores != [] and joueurs != [] and len(scores) == len(joueurs):
        if nom_joueur in joueurs :
            for indice in range(len(scores)) :
                if joueurs[indice] == nom_joueur:
                    res += 1
    return res
    
# exercice 6

# exercice 7
def meilleur_classement_joueur(nom_joueur,scores,joueurs):
    """donne le meilleur classement d'un joueur (-1 s'il n'apparait pas dans le classement)
    paramètres : nom_joueur = joueur pour lequel on veut le classement, scores = liste des meilleurs scores, joueurs = liste des joueurs associés aux meilleurs scores
    résultat : classement du joueur, -1 si le joueur n'est pas dans scores"""
    res = ""
    val_retour = -1
    if scores != [] and joueurs != [] and len(scores) == len(joueurs):
        if nom_joueur in joueurs : 
            for indice in range(len(scores)) :
                if (joueurs[indice] == nom_joueur) :
                    if val_retour == -1 :
                        val_retour = indice + 1
                    res += str(indice+1)
                    res += ". "
                    res += joueurs[indice]
                    res += " "
                    res += str(scores[indice])
                    res += "\n"
    print(res)
    return val_retour


# exercice 8
def placeScore(nouveau_score,scores):
    """donne l'indice ou placer le nouveau score dans la liste des scores
    paramètres : nouveau_score = score a inserer dans la liste des scores, scores = liste des scores
    résultat : indice ou le nouveau_score doit etre inséré dans scores"""
    indice = 0
    res = -1
    if scores != [] :
        while indice < (len(scores)) and res == -1 :  
            if nouveau_score > scores[indice] : 
                res = indice 
            if nouveau_score < scores[len(scores)-1] : 
                res = len(scores)
            indice += 1
    else :
        res = None
    return res

# exercice 9
def ajouter_score(nouveau_score, nom_joueur, scores,joueurs):
    """ajoute le nouveau score d'un joueur dans la liste des scores 
    (et la liste des joueurs)
    paramètres : nouveau_score = score qu'on ajoute dans la liste, nom_joueur = joueur ayant effectué le score, scores = liste des scores et joueurs = liste des joueurs 
    résultat cette fonction modifie directement scores et joueurs mais ne retourne rien"""
    if scores != [] and joueurs != []:
        rang = placeScore(nouveau_score, scores)
        if rang == len(scores) : 
            scores.append(nouveau_score)
            joueurs.append(nom_joueur)
        else : 
            scores.insert(rang, nouveau_score)
            joueurs.insert(rang, nom_joueur)
    if scores == [] and joueurs == [] : 
            scores.append(nouveau_score)
            joueurs.append(nom_joueur)

# exercice 10
def ajouter_score_limite(nouveau_score, nom_joueur, scores,joueurs,taille_max):    
    """ajoute le nouveau score d'un joueur dans la liste des scores 
    (et la liste des joueurs) en limitant le nombre de places à taille_max
    paramètres : nouveau_score = score a ajouter dans la liste des scores, nom_joueur = joueur ayant effectué le score, scores = liste des scores, joueurs = liste des joueurs, taille_max = taille maxi de la liste des scores
    résultat cette fonction modifie directement scores et joueurs mais ne retourne rien"""
    ajouter_score(nouveau_score, nom_joueur, scores,joueurs)
    while (len(scores) > taille_max):
        scores.pop()
        joueurs.pop()
    
# exercice 11
def sauver_score(nom_fic,scores,joueurs):
    """
    sauvegarde dans un fichier texte les scores (avec le nom de joueur associé)
    paramètres : 
    résultat aucun mais créer un fichier"""
    mon_fichier = open(nom_fic, "w")
    if scores != [] and joueurs != [] and len(scores) == len(joueurs):
        for indice in range(len(scores)) : 
            mon_fichier.write(str(scores[indice]))
            mon_fichier.write(",")
            mon_fichier.write(joueurs[indice])
            mon_fichier.write("\n")
    else : 
        print("erreur dans les listes")
    mon_fichier.close()
    
# exercice 12
def restaurer_score(nom_fic,scores,joueurs):
    """charge la liste des scores et des noms de joueurs à partir d'un fichier texte
    paramètres:
    résultat aucun mais la fonction stocke les informations dans scores et joueurs"""
    if os.path.isfile(nom_fic) :
        mon_fichier = open(nom_fic, "r")
        joueur = ""
        score = ""
        for ligne in mon_fichier : 
            for indice in range(len(ligne)):
                if ligne[indice].isalpha() or ligne[indice] == " ": 
                    joueur += ligne[indice]
                if ligne[indice].isdecimal() :
                    score += ligne[indice]
            if score.isdecimal():
                joueurs.append(joueur)
                scores.append(int(score))
            joueur = ""
            score = ""
        mon_fichier.close()
    else : 
        print("le fichier ", nom_fic, " n'existe pas")
    
# exercice 13
def scores_HTML(nom_fic,scores,joueurs):
    """sauvegarde dans un fichier HTML sous la forme d'un tableau
    les scores (avec le nom de joueur associé)
    paramètres : nom_fic = nom du fichier html généré par la fonction, scores = liste des scores et joueurs = liste des joueurs
    résultat aucun mais créer un fichier"""
    mon_fichier = open(nom_fic, "w")
    mon_fichier.write("<table>\n<tr> <td> Rang </td> <td> Nom </td> <td> Score </td> </tr>\n")
    if scores != [] and joueurs != [] :
        for indice in range(len(scores)):
            mon_fichier.write("<tr> <td>")
            mon_fichier.write(str(indice+1))
            mon_fichier.write(". </td> <td>")
            mon_fichier.write(joueurs[indice])
            mon_fichier.write("</td> <td>")
            mon_fichier.write(str(scores[indice]))
            mon_fichier.write("</td> </tr> \n")
        mon_fichier.write("</table>")
        mon_fichier.close()
    else : 
        print('erreur : au moins une des liste est vide')