def recherche_dichotomique(liste,elem):
    bas = 0
    haut = len(liste)-1
    while(bas<haut):
        milieu = (bas+haut)//2
        if(liste[milieu]<elem):
            bas = milieu+1
        else:
            haut = milieu
    return bas < len(liste) and elem == liste[bas]