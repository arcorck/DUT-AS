def texte_to_liste_de_mot (texte) :
    """Cette fonction prend un texte en paramètre et retourne une liste de tout les mots qui composent le texte"""
    res = []
    mot = ""
    if len(texte) != 0 :
        for i in range(len(texte)) :
            if (texte[i].isalpha() or texte[i] == '-') :
                mot += texte[i]
            else :
                if mot != "" :
                    res.append(mot)
                mot = ""
        res.append(mot)
    return res

assert texte_to_liste_de_mot("le lundi, c'est le premier jour de la semaine") == ['le', 'lundi', 'c', 'est', 'le', 'premier', 'jour', 'de', 'la', 'semaine'], 'Erreur'
assert texte_to_liste_de_mot("les enfants vont à l'école") == ['les', 'enfants', 'vont', 'à', 'l', 'école'], 'Erreur'
assert texte_to_liste_de_mot("") == [], 'Erreur'

def lirefic(nomfic) :
    fic = open(nomfic, "r")
    res = ''
    for ligne in fic :
        res += ligne
    fic.close()
    res = res.lower()
    return res


def fic_to_liste_de_mot (nomfichier) :
    """fonction qui renvoie la liste des mots contenues dans le fichier nomfichier"""
    return texte_to_liste_de_mot(lirefic(nomfichier))

print(fic_to_liste_de_mot("toto.txt"))