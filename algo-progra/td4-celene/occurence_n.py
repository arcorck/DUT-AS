def neme_occurence (liste, n, occ):
    """retourne la n eme occurence de occ dans liste"""
    res = -1
    cpt = 0
    occ_n = 0
    if liste != [] :
        while cpt < len(liste) and res == -1 :
            if liste[cpt] == occ :
                occ_n += 1
            if occ_n == n :
                res = cpt
            cpt += 1
    return res

assert neme_occurence([12,3,4,12,8,12,5,12], 3, 12) == 5, "erreur"
assert neme_occurence([12,3,4,12,8,12,5,12], 5, 12) == -1, "erreur"
assert neme_occurence([12,3,4,12,8,12,5,12,8,5,6,4,8,9564,54,541,8], 4, 8) == 16, "erreur"
assert neme_occurence([12,3,4,12,8,12,5,12], 3, 36) == -1, "erreur"
assert neme_occurence([], 3, 36) == -1, "erreur"

print (neme_occurence([12,3,4,12,8,12,5,12], 3, 12))
print (neme_occurence([12,3,4,12,8,12,5,12], 5, 12))
print (neme_occurence([12,3,4,12,8,12,5,12,8,5,6,4,8,9564,54,541,8], 4, 8))
print (neme_occurence([12,3,4,12,8,12,5,12], 3, 36))
print (neme_occurence([], 3, 36))
