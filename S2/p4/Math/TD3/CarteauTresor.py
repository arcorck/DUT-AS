import networkx
import matplotlib.pyplot as pyplot

G1 = networkx.Graph()
G1.add_edges_from([("a","f") , ("a","b") , ("f","c") , ("f","e") ,("f","d") ,("c","e") ,("c","b") ,("c","d") ,("e","d")])
G1.nodes["a"]["tresor"] = 3
G1.nodes["f"]["tresor"] = 4
G1.nodes["c"]["tresor"] = 5
G1.nodes["e"]["tresor"] = 1 
G1.nodes["d"]["tresor"] = 2 
G1.nodes["b"]["tresor"] = 0
print(G1.nodes["a"])

def tresor (g,n) :
    return g.nodes[n]["tresor"]

def parcours_tresor (g,n) :
    lesnoeuds = g.nodes
    lesnoeudsatteints = []
    noeudavectresormax = 0
    tresormax = 0
    while (len(lesnoeuds) != 0):
        for i in len(lesnoeuds) :
            if lesnoeuds[i] not in lesnoeudsatteints :
                if lesnoeuds[i]["tresor"] > tresormax :
                    tresormax = lesnoeuds[i]["tresor"]
                    noeudavectresormax = lesnoeuds[i]
        lesnoeudsatteints.append(noeudavectresormax)
        lesnoeuds.remove(noeudavectresormax)
        tresormax = 0
        noeudavectresormax = 0
    return lesnoeudsatteints 