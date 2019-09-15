def moyenne (n1, c1, n2, c2, n3, c3, n4, c4):
    """Cette fonction a pour but de calculer la moyenne par UE d'un étudiant, sa moyenne globale et de d'indiquer le résultat de son année
    paramètres : 
        n1 : note de la premiere matiere
        c1 : coefficient de la premiere matiere
        n2 : note de la deuxieme matiere
        c2 : coefficient de la deuxieme matiere
        n3 : note de la troisieme matiere
        c3 : coefficient de la troisieme matiere
        n4 : note de la 4eme matiere
        c4 : coefficient de la 4eme matiere"""

    ue1 = ((n1*c1)+(n2*c2)) / (c1+c2)
    ue2 = ((n3*c3)+(n4*c4)) / (c3+c4)

    mg = ((n1*c1)+(n2*c2)+(n3*c3)+(n4*c4)) / (c1+c2+c3+c4)

    s = "l'étudiant a obtenu :\n   - ", str(ue1), " à l'UE1\n   - ", str(ue2), " à l'UE2\nIl a une moyenne générale de ", str(mg), "\n"
    
    if ue1 > 8 and ue2 > 8 :
        if mg > 10 :
            s = s, "L'étudiant valide son année"
        else :
            s = s, "L'étudiant peut compenser son année"
    else :
        s = s, "L'étudiant est en attente de barre"
    return s

assert moyenne(7, 3.5, 5, 3.5, 16, 2.5, 17, 2.0) != "L'étudiant est en attente de barre", "Erreur"
assert moyenne(9, 3.5, 13, 3.5, 8.5, 2.5, 8.5, 2.0) != "L'étudiant valide son année", "Erreur"
    
print(moyenne(7, 3.5, 5, 3.5, 16, 2.5, 17, 2.0), "\n")
print(moyenne(9, 3.5, 13, 3.5, 8.5, 2.5, 8.5, 2.0), "\n")
print(moyenne(19, 3.5, 13, 3.5, 14, 2.5, 12, 2.0), "\n")
print(moyenne(8, 3.5, 14, 3.5, 5, 2.5, 18, 2.0), "\n")
print(moyenne(16, 3.5, 1, 3.5, 19, 2.5, 2, 2.0), "\n")