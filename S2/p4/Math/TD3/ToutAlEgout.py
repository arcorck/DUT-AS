import networkx
import matplotlib.pyplot as pyplot

def est_couvrant(G,liste):
    pile = [0]
    atteint = {0}
    while (len(pile) > 0): 
        noeud_courant = pile.pop()
        print(noeud_courant)
        for i in G[noeud_courant] :
            if (i not in atteint) : 
                pile.append(i)
                atteint.add(i)
            if (noeud_courant,i) not in liste :
                return False
    return True

def couvrant(G):
    pile = [0]
    atteint = {0}
    arretes = []
    while (len(pile) > 0): 
        noeud_courant = pile.pop()
        print(noeud_courant)
        for i in G[noeud_courant] :
            if (i not in atteint) : 
                pile.append(i)
                atteint.add(i)
            arretes.append((noeud_courant, i))
    return arretes