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

def max_tresor (G, l):
    tresor_max = 0
    for elem in l :
        if tresor(G, elem) > tresor_max :
            tresor_max = tresor(G, elem)
            noeud_max = elem
    return noeud_max

def parcours_tresor (g, depart) : 
    pile = [depart]
    atteint = [depart]
    res = []
    while (len(pile) > 0): 
        noeud_courant = max_tresor(g, pile)
        pile.remove(noeud_courant)
        print(noeud_courant)
        res.append(noeud_courant)
        for i in g[noeud_courant] :
            if (i not in atteint) : 
                pile.append(i)
                atteint.append(i)
    return res