def boucles_imbliquees (n, m) :
    cpt = 0
    for i in range(n):
        print("- j'effectue le tour", i, "de la boucle externe")
        for j in range(m):
            print("++ j'effectue le tour", j, "de la boucle interne")
            cpt += 1
    print ("l'instruction 5 est exécutée ", cpt, " fois")

boucles_imbliquees(3,5)
boucles_imbliquees(2,3)
boucles_imbliquees(3,2)
