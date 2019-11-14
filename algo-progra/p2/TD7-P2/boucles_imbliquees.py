def boucles_imbliquees (n, m) :
    """ parametres : n = nombre de tours que va effectuer la boucle externe et m : nombre de tours qye va affectuer la boucle interne
    resultat : aucun mais affiche le nomnre de tours de la boucle externe, celui de la boucle externe et le nombre de passage total dans la boucle interne"""
    cpt = 0
    for i in range(n):
        print("- j'effectue le tour", i, "de la boucle externe")
        for j in range(m):
            print("++ j'effectue le tour", j, "de la boucle interne")
            cpt += 1
    return "l'instruction 5 est exécutée ", cpt, " fois"

#assert boucles_imbliquees(3,5) == "("l'instruction 5 est exécutée ", 15, ' fois')", "Erreur"
#assert boucles_imbliquees(2,3)  == "l'instruction 5 est exécutée 6 fois", "Erreur"
#assert boucles_imbliquees(3,2)  == "l'instruction 5 est exécutée 6 fois", "Erreur"

print(boucles_imbliquees(3,5))
