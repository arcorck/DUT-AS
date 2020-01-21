import os.path

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
    if len(serpent) == 3 and serpent != (None, None, None):
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
    
assert serpent_to_str(("Python3",0.3,0))=="--------------------\nNom: Python3\nTaille: 0.3\nDanger: 0\n--------------------\n", 'Pb serpent_to_str(("Python3",0.3,0))'
assert serpent_to_str(("BOA",54.789,4))=="--------------------\nNom: BOA\nTaille: 54.789\nDanger: 4\n--------------------\n", 'Pb serpent_to_str'
assert serpent_to_str(("Python3", 0))== "", "pb serpent_to_str"


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

assert liste_serpents_to_str([("Python3",0.3,0),("Boa",3.5,4)])=="--------------------\nNom: Python3\nTaille: 0.3\nDanger: 0\n--------------------\n--------------------\nNom: Boa\nTaille: 3.5\nDanger: 4\n--------------------\n", 'Pb liste_serpents_to_str'
assert liste_serpents_to_str([("BOA",54.789,4),("vipere",3,2)])=="--------------------\nNom: BOA\nTaille: 54.789\nDanger: 4\n--------------------\n--------------------\nNom: vipere\nTaille: 3\nDanger: 2\n--------------------\n", 'Pb liste_serpents_to_str'
assert liste_serpents_to_str([]) == "", "pb liste_serpents_to_str"

def check_string_to_float(s):
     try:
             float(s)
             return True
     except:
             return False


def saisir_un_serpent():
    '''
    permet de demander à l'utilisateur les informations concernant un serpent
    paramètre: aucun
    resultat: retourne un serpent sous forme de tuple avec les infos saisies par l'utilisateur 
    '''
    res = (None, None, None)
    nom = input("Entrer le nom d'un serpent : ")
    size = input("Entrer la taille d'un serpent : ")
    danger = input("Entrer la dangerosité d'un serpent : ")
    if danger.isdigit() :
        danger = int(danger)
        if check_string_to_float(size) :
            size = float(size)
            res = (nom, size, danger)
    return res

# Le résultat de cette fonction dépend de ce qu'a saisi l'utilisateur 

def ajouter_serpents(liste_serpents):
    '''
    permet de demander à l'utilisateur des informations sur des nouveaux serpents
    et d'ajouter ces serpents au fur et à mesure à la liste de serpents
    paramètre: liste_serpents : liste des serpents à laquelle on ajoute les serpents crées par l'utilisateur
    resultat: pas de return mais la liste liste_serpents est mise à jour et comprend les serpents ajoutés par l'utilisateur
    '''
    nb_serp = input("Combien de serpents voulez vous ajouter ? ")
    while nb_serp.isdigit() == False :
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
    nb_serp = None
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

def charger_serpents(nom_fichier):
    '''
    charge une liste de serpents contenue dans un fichier en mémoire
    paramètre: nom_fichier : nom du fichier dans lequel on va recuperer une liste de serpents
    resultat: retourne une liste de serpents qu'on a recuperer dans le fichier passé en paramètre
    '''
    liste_serpents = []
    if os.path.isfile(nom_fichier) :
        fichier = open(nom_fichier, "r")
        for ligne in fichier :
            serpent = (None, None, None)
            liste = ligne.split(",")
            liste[2] = int(liste[2])
            liste[1] = float(liste[1])
            serpent = (liste[0], liste[1], liste[2])
            liste_serpents.append(serpent)
    else : 
        print("attention le fichier n'existe pas")
    return liste_serpents

sauver_serpents('test.txt',[("Python3",0.3,0),("Boa",3.5,4)])
assert charger_serpents('test.txt')==[("Python3",0.3,0),("Boa",3.5,4)], "PB sauver_serpents ou charger_serpents" 

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

assert rechercher_dangereux([("Python3",0.3,0),("Boa",3.5,5)]) == serpent_to_str(("Boa",3.5,5)), "Erreur avec rechercher_dangereux()"
assert rechercher_dangereux([]) == "", "Erreur avec rechercher_dangereux()"

def moyenne_taille_dangerosite(liste_serpents,dangerosite):
    '''
    calcule la taille moyenne des serpents pour une certaine dangerosité
    paramètre: liste_serpents : liste des serpents et dangerosite : dangerosite des serpents pour lesquels on va calculer la taille moyenne
    resultat: retourne la taille moyenne des serpents issus de liste_serpents dont la dangerosite est égale à dangerosité 
    '''
    taille_moyenne = 0
    nb = 0
    res = 0
    if liste_serpents != [] and dangerosite >= 0 and dangerosite <= 5: 
        for indice in range(len(liste_serpents)) :
            if liste_serpents[indice][2] == dangerosite :
                taille_moyenne += liste_serpents[indice][1]
                nb += 1
        res = taille_moyenne/nb
    return res   

assert moyenne_taille_dangerosite([("Python3",0.3,4),("Boa",3.5,4)], 4) == 1.9, "Erreur moyenne_taille_dangerosite()"
assert moyenne_taille_dangerosite([("Python3",0.3,4),("Boa",3.5,4)], 7) == 0, "Erreur moyenne_taille_dangerosite()"
assert moyenne_taille_dangerosite([("Python3",0.3,4),("Boa",3.5,4)], -4) == 0, "Erreur moyenne_taille_dangerosite()"
assert moyenne_taille_dangerosite([], 4) == 0, "Erreur moyenne_taille_dangerosite()"
    
def nb_serpents_par_danger(liste_serpents):
    '''
    donne le nombre de serpents pour chaque niveau de dangerosité
    paramètre: liste_serpents : liste des serpents
    resultat: retourne une chaine de caractere qui affiche le nombre de serpents par dangerosité de 0 à 5
    '''
    res = []
    cpt = 0
    if liste_serpents != [] :  
        for dangerosite in range(6) :
            for elem in liste_serpents :
                if elem[2] == dangerosite :
                    cpt += 1
            res.append(cpt)
            cpt = 0
    return res

assert nb_serpents_par_danger([("Python3",0.3,0),("Boa",3.5,4)]) == [1, 0, 0, 0, 1, 0], "Erreur avec nb_serpents_par_danger()"
assert nb_serpents_par_danger([]) == [], "Erreur avec nb_serpents_par_danger()"

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
