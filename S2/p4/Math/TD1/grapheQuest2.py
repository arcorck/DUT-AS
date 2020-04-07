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
networkx.draw (G)
input()

#pour chaque sommet (équipe), on lui ajoute un dico 
#avec pour clés la liste des noms des jours 
#et pour valeur la liste des numéros des joueurs