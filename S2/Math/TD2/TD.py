import  networkx
import  matplotlib.pyplot  as  pyplot

def parcours (graphe, depart) :
    pile = [depart]
    while (len(pile) > 0) :
        noeud_courant = pile.pop()
        print(noeud_courant)
        for i in graphe[noeud_courant] :
            pile.append(i)


def parcours_profondeur (g, depart) : 
    pile = [depart]
    atteint = {depart}
    while (len(pile) > 0): 
        noeud_courant = pile.pop()
        print(noeud_courant)
        for i in g[noeud_courant] :
            if (i not in atteint) : 
                pile.append(i)
                atteint.add(i)
    return atteint


def accessible (graphe, sommet1, sommet2) : 
    return sommet2 in parcours_profondeur(graphe, sommet1)


def nb_sommets_accessibles(graphe, sommet): 
    return len(parcours_profondeur(graphe, sommet))


def cycle (g, depart) : 
    pile = [depart]
    atteint = {depart}
    while (len(pile) > 0): 
        noeud_courant = pile.pop()
        for i in g[noeud_courant] :
            if (i in pile) : 
                return True
            if (i not in atteint):
                pile.append(i)
                atteint.add(i)
    return False