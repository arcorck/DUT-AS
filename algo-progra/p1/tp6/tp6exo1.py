def strMois(numMois,nomsMois) :
    """return en fonction du numéro du mois le nom du mois que le programme va chercher dans la liste nomsMois"""
    res = None
    if nomsMois != [] and numMois < len(nomsMois) :
        res = nomsMois[numMois]
    return res

assert strMois(2, ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novmebre', 'decembre']) == 'mars', 'erreur'
assert strMois(2, ['january', 'february', 'march', 'april', 'may', 'june', 'julli', 'august', 'september', 'october', 'novmeber', 'december']) == 'march', 'error'
assert strMois(25, ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novmebre', 'decembre']) == None, 'erreur'
assert strMois(2, []) == None, 'erreur'

print(strMois(2, ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novmebre', 'decembre']))
print(strMois(2, ['january', 'february', 'march', 'april', 'may', 'june', 'julli', 'august', 'september', 'october', 'novmeber', 'december']))
print(strMois(2, []))



def ligneMois(nomsMois) :
    """Prends en paramètre une liste de mois de l'année et renvoie une chaine de caractères 
    composée des 3 premiers caractères de chacun des mois séparés d'un espace"""
    indice = 0
    res = ''
    while indice < len(nomsMois) :
        res += nomsMois[indice][0]
        res += nomsMois[indice][1]
        res += nomsMois[indice][2]
        res += ' '
        indice += 1
    return res

assert ligneMois(['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novmebre', 'Decembre']) == 'Jan Fev Mar Avr Mai Jui Jui Aou Sep Oct Nov Dec ', "Erreur"
assert ligneMois(['January', 'February', 'March', 'April', 'May', 'June', 'Julli', 'August', 'September', 'October', 'Novmeber', 'December']) == 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec ', "Error"
assert ligneMois([]) == '', "Erreur"

print(ligneMois(['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novmebre', 'Decembre']))
print(ligneMois(['January', 'February', 'March', 'April', 'May', 'June', 'Julli', 'August', 'September', 'October', 'Novmeber', 'December']))
print(ligneMois([]))