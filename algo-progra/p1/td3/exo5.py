def mystere (liste_mots, lettre) : 
    """Cette fonction va renvoyer la liste de tous les mots qui commencent par lettre parmi liste_mots"""
    res = []
    if len(liste_mots) != 0 and len(lettre) == 1 :
        for mot in liste_mots : 
            if mot[0] == lettre :
                res.append(mot)
    return res

assert mystere(["oui", "non", "peut-être", "yes", "no"], "n") == ["non", "no"], "Erreur"
assert mystere(["bleu", "blanc", "rouge"], "b") == ["bleu", "blanc"], "Erreur"
assert mystere(["M1101", 'M1102', 'M1103'], '1') == [], "Erreur"

print("mystere : ")
print(mystere(["oui", "non", "peut-être", "yes", "no"], "n"))
print(mystere(["bleu", "blanc", "rouge"], "b"))
print(mystere(["M1101", 'M1102', 'M1103'], '1'))

print("\n\nmystere_bis : ")


def mystere_bis (liste_mots, lettre) : 
    """Cette fonction va renvoyer la liste de tous les mots qui commencent par lettre parmi liste_mots"""
    res = []
    if len(liste_mots) != 0 and len(lettre) == 1 :
        for indice in range(len(liste_mots)) : 
            if liste_mots[indice][0] == lettre :
                res.append(liste_mots[indice])
    return res

assert mystere_bis(["oui", "non", "peut-être", "yes", "no"], "n") == ["non", "no"], "Erreur"
assert mystere_bis(["bleu", "blanc", "rouge"], "b") == ["bleu", "blanc"], "Erreur"
assert mystere_bis(["M1101", 'M1102', 'M1103'], '1') == [], "Erreur"

print(mystere_bis(["oui", "non", "peut-être", "yes", "no"], "n"))
print(mystere_bis(["bleu", "blanc", "rouge"], "b"))
print(mystere_bis(["M1101", 'M1102', 'M1103'], '1'))