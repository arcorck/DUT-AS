######################################################################
# Feuille de TP 4
# NOM : Bazire Fabrice
#######################################################################

#######################################################################
print("==========================================")
print("Exercice 1 - Echauffement - Fan-club")

groupePrefere={'Florent':'Chantal Goya','Celine':'SuperBus', 'Julien':'ACDC','Denys':'ACDC','Caroline':'Chantal Goya'}
  
def fansde (lesgroupesprefs, groupe) :
    les_fans = set()
    for f,g in lesgroupesprefs.items() :
        if g == groupe :
            les_fans.add(f)
    return les_fans

assert fansde(groupePrefere, 'Chantal Goya') == {'Caroline', 'Florent'}, 'Erreur'
assert fansde(groupePrefere, 'SuperBus') == {'Celine'}, 'Erreur'


print("==========================================")
print("Exercice 2 - Naturalistes en herbe")


regimeAlimentaire={
  'Requin':{'Nageur','Sac Plastique','Poisson'},
  'Nageur':{'Poisson','Noisette'},
  'Lion':{'Gazelle'},
  'Ecureuil':{'Noisette'}}
nourritureDisponible={
  'Ocean':{'Poisson','Sac Plastique','Nageur'},
  'Savane':{'Gazelle'},
  'Jardin avec piscine':{'Nageur','Noisette'}
}

def inverse(dico) :
    res = {}
    for animal, aliments in dico.items() :
        for a in aliments :
            if a not in res :
                res[a] = set()
                res[a].add(animal)
            else :
                res[a].add(animal)
    return res
assert inverse(regimeAlimentaire) == {'Poisson': {'Nageur', 'Requin'}, 'Nageur': {'Requin'}, 'Sac Plastique': {'Requin'}, 'Noisette': {'Nageur', 'Ecureuil'}, 'Gazelle': {'Lion'}}, "Erreur"
assert inverse(nourritureDisponible) == {'Nageur': {'Jardin avec piscine', 'Ocean'}, 'Sac Plastique': {'Ocean'}, 'Poisson': {'Ocean'}, 'Gazelle': {'Savane'}, 'Noisette': {'Jardin avec piscine'}}, "Erreur"


def peutSurvivre(regimeAlimentaire,nourritureDisponible) :
    res = {}
    for region in nourritureDisponible.keys() :
        for animal, ensaliment in regimeAlimentaire.items() :
            for aliment in ensaliment :
                if aliment in nourritureDisponible[region] : 
                    if region not in res :
                        res[region] = set()
                    res[region].add(animal)
    return res

assert peutSurvivre(regimeAlimentaire, nourritureDisponible) == {'Ocean': {'Nageur', 'Requin'}, 'Savane': {'Lion'}, 'Jardin avec piscine': {'Ecureuil', 'Nageur', 'Requin'}}, "Erreur"
            

print("==========================================")
print("Exercice 3 - Rapide et furieux, une série qui se répète un peu")


#Version 1
def nombre_apparition(chaine, caractere):
    cpt=0
    for char in chaine: 
        # ICI
        if caractere == char:
            cpt=cpt+1
    return cpt

def caracteres_en_double(chaine):
    """
    resultat : l'ensemble des caractères qui apparaissent au
    moins 2 fois dans la chaine
    """
    caracteresRepetees = set() 
    for caractere in chaine:
        if nombre_apparition(chaine, caractere) > 1:
            caracteresRepetees.add(caractere)
    return caracteresRepetees


print(caracteres_en_double("Yolo"))

print(caracteres_en_double("Tu lui brises le coeur, je te brise la tête !")) # 45 caractères

#Version 2
def caracteres_en_double(chaine):
    """
    resultat : la liste des caractères qui apparaissent au
    moins 2 fois dans la chaine
    """
    dejaVu=[]
    caracteres_repetes=[]
    for caractere in chaine:
        if caractere not in dejaVu:
            dejaVu.append(caractere)
        else:
            caracteres_repetes.append(caractere)
    return caracteres_repetes


#Version 3
def caracteres_en_double(chaine):
    """
    resultat : l'ensemble des caractères qui apparaissent au
    moins 2 fois dans la chaine
    """
    dejaVu=set()
    caracteres_repetes=set()
    for caractere in chaine:
        if caractere not in dejaVu:
            dejaVu.add(caractere)
        else:
            caracteres_repetes.add(caractere)
    return caracteres_repetes

print("==========================================")
print("Exercice 4 - Oh les amoureux !")

ATM={'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida', 
     'Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri',
     'Gaston':'Beatrice','Henri':'Firmin'}

def reciproque(dicoAmoureux):
    """ 
    renvoie les couples dont l'amour est reciproque
    """
    res = set()
    for membre_atm, amoureux in dicoAmoureux.items() :
        if amoureux in dicoAmoureux.values() : 
            if dicoAmoureux[amoureux] == membre_atm and (membre_atm,amoureux) not in res and (amoureux, membre_atm) not in res:
                res.add((membre_atm, amoureux))
    return res
assert reciproque(ATM) == {('Cesar', 'Dalida'), ('Firmin', 'Henri')}, 'Erreur'
assert len(reciproque(ATM))==2, "Il y a très certainement des couples en double"
assert ('Henri','Firmin') in reciproque(ATM) or ('Firmin','Henri') in reciproque(ATM)
assert ('Dalida','Cesar')  in reciproque(ATM) or ('Cesar','Dalida') in reciproque(ATM)


def soupirants(dicoAmoureux, nom_pers) :
    res = set()
    for membre_atm, amoureux in dicoAmoureux.items() :
        if amoureux == nom_pers :
            res.add(membre_atm)
    return res
assert soupirants(ATM, 'Beatrice') == {'Etienne', 'Gaston', 'Armand'}, 'Erreur'


print("==========================================")
print("Exercice 6 - Le retour des timides maladifs")

amoursATM={
  'Armand':{'Beatrice','Dalida'},
  'Beatrice':{'Cesar','Armand'},
  'Cesar':{'Dalida','Gaston'}, 
  'Dalida':{'Cesar','Armand'},
  'Etienne':{'Beatrice','Firmin'},
  'Firmin':{'Henri','Beatrice','Armand','Dalida'},
  'Gaston':{'Beatrice','Dalida','Cesar'},
  'Henri':{'Firmin','Armand','Cesar','Henri'}}

def reciproque(dicoAmoureux):
    """ 
    renvoie les couples dont l'amour est reciproque
    """
    res = set()
    for membre_atm, amoureux in dicoAmoureux.items() :
        for amoureu in amoureux : 
            if amoureu in dicoAmoureux.keys() :
                if membre_atm in dicoAmoureux[amoureu] and (membre_atm,amoureu) not in res and (amoureu, membre_atm) not in res and membre_atm != amoureu:
                    res.add((membre_atm, amoureu))
    return res
assert reciproque(amoursATM) == {('Firmin', 'Henri'), ('Armand', 'Beatrice'), ('Armand', 'Dalida'), ('Cesar', 'Gaston'), ('Cesar', 'Dalida')}, 'Erreur'

def hippies (dicoAmoureux, ensemble_des_amoureux) :
    res = True
    est_aime = 0
    les_couples = reciproque(dicoAmoureux)
    for amoureu in ensemble_des_amoureux :
        for amoureux1, amoureux2 in les_couples :
            if amoureux1 == amoureu or amoureux2 == amoureu :
                est_aime += 1
        if est_aime == 0 : 
            res = False
        else : 
            est_aime = 0
    return res

ensemble_des_amoureux1 = { 'Armand', 'Beatrice', 'Cesar', 'Dalida', 'Etienne', 'Firmin', 'Gaston', 'Henri'}
ensemble_des_amoureux2 = { 'Armand', 'Beatrice', 'Cesar', 'Dalida', 'Firmin', 'Gaston', 'Henri'}
print(hippies(amoursATM, ensemble_des_amoureux1))
print(hippies(amoursATM, ensemble_des_amoureux2))
