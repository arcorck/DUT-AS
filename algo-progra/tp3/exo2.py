def nb_espaces (phrase) :
    """Cette fonction a pour de renvoyer le nombre d'espace +1 contenu dans un str, 
    plus generalement c1 sert d'element de test, si on met dans phrase un long nombre et dans c1 un 0, 
    le programme va nous retourner le nombre de 0 + 1 contenu dans notre nombre  
        parametre : phrase : la phrase pour laquelle on veut connaitre le nombre d'espace"""
    nb_esp=0
    c1=' '
    for char in phrase : 
        if c1==" " and char!=" " : 
            nb_esp = nb_esp + 1
        c1=char
    return nb_esp

#assert nb_espaces(' il fait vraiment beau ce matin ')==6, "Erreur"
#assert nb_espaces(' tp programmation python ')==3, "Erreur"
#assert nb_espaces(" j'adore le python mais je prefere html ")==7, "Erreur"
#assert nb_espaces(" j'adore conduire surtout en musique avec de la musique")==9, "Erreur"
#assert nb_espaces(" bonjour ")==1, 'Erreur'

print("affichage de mystere : ", nb_espaces(' il fait vraiment beau ce matin '))
print("affichage de mystere : ", nb_espaces(' tp programmation python '))
print("affichage de mystere : ", nb_espaces(" j'adore le python mais je prefere html "))
print("affichage de mystere : ", nb_espaces(" j'adore conduire surtout en musique avec de la musique"))
print("affichage de mystere : ", nb_espaces(" bonjour "))
# 1) l'affichage renvoie 6 pour 'il fait vraiment beau ce matin '
# 2) l'affichage renvoie 3 pour ' tp programmation python'
# l'affichage renvoie 7 pour ' j'adore le python mais je prefere html '
# l'affichage renvoie 8 pour 'j'adore conduire surtout en musique avec de la musique'
# l'affichage renvoie 8 pour ' bonjour '
# 3) la fonction retourne le nombre d'espace (ou d'un autre char) + 1 contenu dans param



