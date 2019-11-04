####################################################
### IMPLEMENTEZ CI-DESSOUS VOS FONCTIONS         ###
### ATTENTION AUX NOMS DES FONCTIONS UTILISEES   ###
### DANS LA PARTIE PROGRAMME PRINCIPAL           ###
####################################################

def serpent_to_str(serpent):
    '''
    met en forme les informations d'un serpent sous la forme d'un str
    paramètre: serpent : tuple qui represente le serpent 
    resultat: aff : str qui contient la conversion du tuple serpent en str
    '''
    aff = ""
    if len(serpent) == 3 :
        aff += "--------------------\n"
        aff += "Nom: "
        aff += serpent[0]
        aff += "\n"
        aff += "Taille: "
        aff += str(serpent[1])
        aff += "\n"
        aff += "Danger: "
        aff += str(serpent[2])
        aff += "\n"
        aff += "--------------------\n"
    return aff
    

# A decommenter une fois la fonction implémentée
assert serpent_to_str(("Python3",0.3,0))=="--------------------\nNom: Python3\nTaille: 0.3\nDanger: 0\n--------------------\n", 'Pb serpent_to_str(("Python3",0.3,0))'
# ici rajoutez vos tests 


def liste_serpents_to_str(liste_serpents):
    '''
    met en forme une liste de serpent sous la forme d'un str
    paramètre: liste_serpents : la liste des serpents que l'on va afficher
    resultat: aff : la str qui contient l'affichage de la liste de serpents
    '''
    aff = ""
    if liste_serpents != []:
        for serp in liste_serpents :
            aff += serpent_to_str(serp)
    return aff

# A decommenter une fois la fonction implémentée
assert liste_serpents_to_str([("Python3",0.3,0),("Boa",3.5,4)])=="--------------------\nNom: Python3\nTaille: 0.3\nDanger: 0\n--------------------\n--------------------\nNom: Boa\nTaille: 3.5\nDanger: 4\n--------------------\n", 'Pb liste_serpents_to_str([("Python3",0.3,0),("Boa",3.5,4)])'
# ici rajoutez vos tests 

def saisir_un_serpent():
    '''
    permet de demander à l'utilisateur les informations concernant un serpent
    paramètre: aucun
    resultat: retourne un serpent sous forme de tuple avec les infos saisies par l'utilisateur 
    '''
    nom = input("Entrer le nom d'un serpent : ")
    size = input("Entrer la taille d'un serpent : ")
    danger = input("Entrer la dangerosité d'un serpent : ")
    return (nom, float(size), int(danger))

# Le résultat de cette fonction dépend de ce qu'a saisi l'utilisateur 

def ajouter_serpents(liste_serpents):
    '''
    permet de demander à l'utilisateur des informations sur des nouveaux serpents
    et d'ajouter ces serpents au fur et à mesure à la liste de serpents
    paramètre: liste_serpents : liste des serpents à laquelle on ajoute les serpents crées par l'utilisateur
    resultat: pas de return mais la liste liste_serpents est mise à jour et comprend les serpents ajoutés par l'utilisateur
    '''
    nb_serp = input("Combien de serpents voulez vous ajouter ? ")
    for indice in range(int(nb_serp)):
        liste_serpents.append(saisir_un_serpent())

# Le résultat de cette fonction dépend de ce qu'a saisi l'utilisateur 


def sauver_serpents(nom_fic,liste_serpents):
    '''
    sauvegarde une liste de serpents dans un fichier
    paramètres: nom_fic : nom du fichier dans lequel on sauvegarde la liste de serpents liste_serpents
    resultat: retourne le nombre de serpents sauvegardés dans le fichier (en theorie autant qu'il y en a dans liste_serpents)
    '''
    fichier = open(nom_fic, "a")
    nb_serp = 0
    for indice in range(len(liste_serpents)) :
        fichier.write(str(liste_serpents[indice][0]))
        fichier.write(",")
        fichier.write(str(liste_serpents[indice][1]))
        fichier.write(",")
        fichier.write(str(liste_serpents[indice][2]))
        fichier.write("\n")
        nb_serp += 1
    return nb_serp

# Il faut regarder le fichier nom_fic

def charger_serpents(nom_fichier):
    '''
    charge une liste de serpents contenue dans un fichier en mémoire
    paramètre: nom_fichier : nom du fichier dans lequel on va recuperer une liste de serpents
    resultat: retourne une liste de serpents qu'on a recuperer dans le fichier passé en paramètre
    '''
    liste_serpents = []
    fichier = open(nom_fichier, "r")
    for ligne in fichier :
        liste = ligne.split(",")
        serpent = (liste[0], float(liste[1]), int(liste[2]))
        liste_serpents.append(serpent)
    return liste_serpents


# A decommenter une fois les deux fonctions charger et sauver implémentées
sauver_serpents('test.txt',[("Python3",0.3,0),("Boa",3.5,4)])
assert charger_serpents('test.txt')==[("Python3",0.3,0),("Boa",3.5,4)], "PB sauver_serpents ou charger_serpents" 

#ici rajoutez vos tests

def rechercher_dangereux(liste_serpents):
    '''
    recherche la liste des serpent dangereux dans une liste de serpents
    paramètre: liste_serpents : liste des serpents pour laquelle on retourne les serpents les plus dangereux 
    '''
    aff = ""
    if liste_serpents != [] : 
        for indice in range(len(liste_serpents)) :
            if liste_serpents[indice][2] == 5 :
                aff += serpent_to_str(liste_serpents[indice])
    return aff

#ici rajoutez vos tests
    
def moyenne_taille_dangerosite(liste_serpents,dangerosite):
    '''
    calcule la taille moyenne des serpents pour une certaine dangerosité
    paramètre: liste_serpents : liste des serpents et dangerosite : dangerosite des serpents pour lesquels on va calculer la taille moyenne
    resultat: retourne la taille moyenne des serpents issus de liste_serpents dont la dangerosite est égale à dangerosité 
    '''
    taille_moyenne = 0.0
    nb = 0
    if liste_serpents != [] : 
        for indice in range(len(liste_serpents)) :
            if liste_serpents[indice][2] == dangerosite :
                taille_moyenne += liste_serpents[indice][1]
                nb += 1
    return taille_moyenne / nb    

#ici rajoutez vos tests
    
def nb_serpents_par_danger(liste_serpents):
    '''
    donne le nombre de serpents pour chaque niveau de dangerosité
    paramètre: liste_serpents : liste des serpents
    resultat: retourne une chaine de caractere qui affiche le nombre de serpents par dangerosité de 0 à 5
    '''
    aff = ""
    cpt = 0
    if liste_serpents != [] : 
        for dangerosite in range(6) : 
            for indice in range(len(liste_serpents)) :
                if liste_serpents[indice][2] == dangerosite :
                    cpt += 1
            print (str(cpt), " serpents correspondent au niveau de dangerosite ", str(dangerosite))
            cpt = 0
    return aff

#ici rajoutez vos tests

####################################################
### PROGRAMME PRINCIPAL                          ###
####################################################
if __name__=='__main__':
    rep=input('Voulez-vous charger une liste de serpents (O/N)? ')
    if rep=='O' or rep=='o':
        nom_fichier=input('Donnez le nom du fichier ')
        liste_serpents=charger_serpents(nom_fichier)
    else:
        liste_serpents=[]
    fini=False
    while not fini:
        print('-'*20)
        print('1. Afficher la liste des serpents')
        print('2. Ajouter de nouveaux serpents')
        print('3. Sauvegarder votre liste de serpents')
        print('4. Rechercher les serpents les plus dangereux')
        print('5. Calculer la taille moyenne des serpents de dangerosité 4')
        print('6. Afficher le nombre de serpents par niveau de danger')
        print('7. Quitter')
        rep=input('Tapez votre choix ')
        if rep=='1':
            print(liste_serpents_to_str(liste_serpents))
        elif rep=='2':
            ajouter_serpents(liste_serpents)
        elif rep=='3':
            nom_fic=input("Donnez le nom du fichier SVP ")
            nbSerpents=sauver_serpents(nom_fic,liste_serpents)
            print(nbSerpents,"sauvegardés")
        elif rep=='4':
            lesDangereux=rechercher_dangereux(liste_serpents)
            print('Voici leurs noms:',lesDangereux)
        elif rep=='5':
            danger=input("Entrez le niveau de dangerosité recherchée ")
            if danger in ["0","1","2","3","4","5"]:
                taille=moyenne_taille_dangerosite(liste_serpents,int(danger))
                print('Voici le résultat',taille)
            else:
                print("Dangerosité inconnue!!!!")
        elif rep=='6':
            nbParNiv=nb_serpents_par_danger(liste_serpents)
            for i in range(len(nbParNiv)):
                print('niveau',i,'nb serpents',nbParNiv[i])
        elif rep=='7':
            fini=True
        else:
            print('Réponse incorrecte!!!')
