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

pyplot.ion ()
pyplot.show ()
G = networkx.Graph() 
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

#Question 2.1
print (chemin(G, 1, 6)!=None)

#Question 2.2
print (len(parcours_profondeur(G,6)))
print (len(parcours_profondeur(G,1)))

#Question 2.3
print(nb_composante_connexe(G))

#Question 3.1
print(chemin(G, 1, 2))
print(chemin(G, 1, 3))
print(chemin(G, 1, 4))
print(chemin(G, 1, 5))
print(chemin(G, 1, 6))

#Question 3.2
print(cycle(G, 1))

networkx.draw (G)
input()