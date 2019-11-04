def next_letter (texte, i):
    """fonction qui renvoie la premiere lettre après le caractère situé à un indice i d'un texte
    paramètre : 
        - texte : texte pour lequel on teste la fonction 
        - i : indice à partir duquel on veut la prochaine lettre"""
    nextletter = 0
    if len(texte) != 0:
        if i >= 0 and i < len(texte)-1 :
            if texte[i+1].isalpha() :
                nextletter = i+1
            else :
                while texte[i].isalpha() == False:
                    i = i+1
                nextletter = i
    return nextletter

assert next_letter('ce, beau chaperon. ! rouge§;',24 ) == 25, "Erreur"
assert next_letter('azerty',5)==0, "Erreur"
assert next_letter('', 5)==0, "Erreur"
assert next_letter('azerty', 15)==0, "Erreur"

texte = 'ce, beau chaperon. ! rouge§;'
print(texte[24])
print (next_letter('ce, beau chaperon. ! rouge§;',24 ))
print(next_letter('azerty',5))


def next_word (texte, i):
    """cette fonction renvoie le mot qui suit la lettre située à l'indice i
    paramètre : 
        - texte : texte pour lequel on teste la fonction
        - indice : indice à partir duquel on veut le prochain mot"""
    nextword = ""
    if len(texte) != 0:
        if i >= 0 and i < len(texte)-1 :
            while texte[i].isalpha() :
                nextword = nextword + texte[i]
                i = i+1
    return nextword

assert next_word('texte pour lequel on teste la fonction', 0) == "texte", 'Erreur'
assert next_word('texte pour lequel on teste la fonction', 5) == "", 'Erreur'
assert next_word('', 5) == "", 'Erreur'
assert next_word('texte pour lequel on teste la fonction', 136) == "", 'Erreur'


print(next_word('texte pour lequel on teste la fonction', 0))
print(next_word('texte pour lequel on teste la fonction', 4))
print(next_word('texte pour lequel on teste la fonction', 5))