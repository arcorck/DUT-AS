import networkx
import matplotlib.pyplot as pyplot
pyplot.ion ()
pyplot.show ()
G= networkx.Graph() 
G.add_edge ( 6 , 4 )
G.add_edge ( 4 , 5 )
G.add_edge ( 4 , 3 )
G.add_edge ( 5 , 1 ) 
G.add_edge ( 5 , 2 )
G.add_edge ( 6 , 1 )
G.add_edge ( 3 , 2 )
G.add_edge ( 7 , 2 )
print(list(G[5].keys()))
networkx.draw(G,with_labels=True)
input()

def degre (g, s) :
    return(len(g[s]))

def relies (g, a, b) :
    return b in list(g[a].keys())

def nb_aretes (g):
    return len(g.edges)


#equipe 4 joue 3 matchs
degre(G, 4)

#equipe 5 n'affronte pas equipe 3
relies(G, 5, 3)

#8 rencontres
nb_aretes(G)