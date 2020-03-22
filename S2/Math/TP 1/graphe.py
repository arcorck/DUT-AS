import networkx
import matplotlib.pyplot as pyplot
pyplot.ion ()
pyplot.show ()
G= networkx.Graph() 
G.add_edge ( 0 , 1 )
G.add_edge ( 1 , 2 )
G.add_edge ( 2 , 3 )
G.add_edge ( 3 , 0 ) 
G.add_edge ( 3 , 4 )
G.add_edge(0,1,toto = "2")
#print(G.edges(data=True))
print(G.add_node(1, time = "5pm"))
G.nodes[3]['tata']=16
print(G.nodes(data=True))
print(G.edges(data=True))
networkx.draw (G)
input()