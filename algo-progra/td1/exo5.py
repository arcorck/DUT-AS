def premiere_date (j1, m1, a1, j2, m2, a2):
    """Cette fonction a pour but en fonction de deux dates (jour/mois/année) de dire laquelle intervient avant l'autre
    paramètres : 
        j1 : jour de la premiere date
        m1 : mois de la premiere date
        a1 : annee de la premiere date
        j2 : jour de la deuxieme date
        m2 : mois de la deuxieme date
        a2 : annee de la deuxieme date"""
    if a1 > a2 : 
        return 1
    else :
        if a1 < a2 :
            return -1
        else :
            if m1 > m2 :
                return 1
            else :
                if m1 < m2 :
                    return -1
                else :
                    if j1 > j2 :
                        return 1
                    else :
                        if j1 < j2 :
                            return -1
                        else : 
                            return 0

assert premiere_date (12, 6, 2013, 10, 9, 2011) == 1, "Erreur"
assert premiere_date (12, 6, 2013, 14, 6, 2013) == -1, "Erreur"
assert premiere_date (28, 2, 2019, 28, 2, 2019) == 0, "Erreur"

print(premiere_date (12, 6, 2013, 10, 9, 2011), "\n")
print(premiere_date (12, 6, 2013, 14, 6, 2013), "\n")
print(premiere_date (28, 2, 2019, 28, 2, 2019), "\n")
print(premiere_date(27, 5, 2018, 20, 8, 2016))