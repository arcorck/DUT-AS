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

print (texte_to_liste_de_mot("le lundi, c'est le premier jour de la semaine"))
print (texte_to_liste_de_mot("les enfants vont à l'école"))
print (texte_to_liste_de_mot("ci-dessus est l'erreur"))



def indice_dans_texte (texte, mot) :
    """Cette fonction prend un texte en paramètre et retourne une liste de tout les indices auxquels apparaissent le mot"""
    res = []
    mot2 = ""
    if len(texte) != 0 :
        for i in range(len(texte)) :
            if (texte[i].isalpha()) :
                mot2 += texte[i]
            else :
                if mot2 == mot :
                    res.append(i-len(mot))
                mot2 = ""
        if mot2 == mot :
            res.append(len(texte) - (len(mot)+1))
    return res

assert indice_dans_texte("le lundi, c'est le premier jour de la semaine", "le") == [0,16], 'Erreur'
assert indice_dans_texte("les les les enfants vont à l'école les", "les") == [0,4,8,34], 'Erreur'
assert indice_dans_texte("", "") == [], 'Erreur'


print ("\n\n",indice_dans_texte("le lundi, c'est le premier jour de la semaine le", "le"))
print (indice_dans_texte("les les les enfants vont à l'école les", "les"))