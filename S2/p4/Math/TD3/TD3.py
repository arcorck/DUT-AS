import networkx
import matplotlib.pyplot as pyplot

def parcours_profondeur (g, depart) : 
    pile = [depart]
    atteint = {depart}
    while (len(pile) > 0): 
        noeud_courant = pile.pop()
        for i in g[noeud_courant] :
            if (i not in atteint) : 
                pile.append(i)
                atteint.add(i)
    return atteint

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

pyplot.ion ()
pyplot.show ()
G= networkx.Graph() 
G.add_edge ( 5 , 1 )
G.add_edge ( 1 , 2 )
G.add_edge ( 4 , 5 )
G.add_edge ( 2 , 3 )
G.add_edge ( 2 , 5 )
G.add_edge ( 3 , 4 )
G.add_edge ( 6 , 4 )
#Question 1
print("parcour en profondeur : ")
print(parcours_profondeur(G, 6))

networkx.draw (G)
input()