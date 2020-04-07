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


def parcours_prof_chaque_sommet (graphe):
    pile = graphe.nodes()
    atteint = set()
    while (len(pile) > 0): 
        noeud_courant = pile.pop()
        if noeud_courant not in atteint :
            for i in parcours_profondeur(graphe, noeud_courant) :
                atteint.add(i)
    return atteint


def nb_composante_connexe (graphe):
    pile = graphe.nodes()
    atteint = set()
    nb_comp = 0
    while (len(pile) > 0): 
        noeud_courant = pile.pop()
        if noeud_courant not in atteint :
            nb_comp += 1
            for i in parcours_profondeur(graphe, noeud_courant) :
                atteint.add(i)
    return nb_comp


def taille_max_composante_connexe (graphe):
    pile = graphe.nodes()
    atteint = set()
    taille_comp_con = 0
    taille_max_comp_con = 0
    while (len(pile) > 0): 
        noeud_courant = pile.pop()
        if noeud_courant not in atteint :
            taille_comp_con += len(parcours_profondeur(graphe, noeud_courant))
            for i in parcours_profondeur(graphe, noeud_courant) :
                atteint.add(i)
            if taille_comp_con > taille_max_comp_con : 
                taille_max_comp_con = taille_comp_con
            taille_comp_con = 0
    return taille_max_comp_con


def chemin (graphe, u, v):
    pile = [(u,[u])]
    atteint = {u}
    while pile :
        courant, chem = pile.pop()
        for vois in graphe[courant] :
            if not vois in atteint :
                atteint.add(vois)
                pile.append((vois, chem[vois]))
                if vois == v :
                    return chem+[vois]
    return None
    