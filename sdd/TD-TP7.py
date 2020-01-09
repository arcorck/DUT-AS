club_sportif = { 'Aurélien' : {'Saut à la perche', 'Lancer du marteau'},
'Elsa' : {'Lancer du marteau', 'Lancer du Javelot'},
'Usain' : {'110 mètres haies', '100 mètres'}}

def pratiquants(club_sportif, discipline) :
    pratique = set()
    for (nom, disciplines) in club_sportif.items() :
        if discipline in disciplines :
            pratique.add(nom)
    return pratique

print(pratiquants(club_sportif, 'Lancer du marteau'))


def discipline_populaire(club_sportif) :
    disciplines = {}
    for (_, les_disciplines) in club_sportif.items() :
        for discipline in les_disciplines :
            if discipline in disciplines :
                disciplines[discipline] += 1
            else : 
                disciplines[discipline] = 1
    def nb_part_disc (discipline) :
        return disciplines[discipline]
    return max(disciplines, key=nb_part_disc)

print(discipline_populaire(club_sportif))


def disciplines_groupe(club_sportif, groupe) :
    les_disciplines = set()
    for (nom, disciplines) in club_sportif.items() :
        if nom in groupe :
            for discipline in disciplines :
                les_disciplines.add(discipline)
    return les_disciplines

print(disciplines_groupe(club_sportif, ['Elsa', 'Aurélien']))
    

def constituer_equipe(club_sportif, epreuves) :
    les_participants = set()
    for (nom, disciplines) in club_sportif.items() :
        for discipline in disciplines :
            if discipline in epreuves :
                les_participants.add(nom)
                epreuves.remove(discipline)
        if epreuves == [] :
            return les_participants
    return None

print(constituer_equipe(club_sportif, ['Lancer du Javelot', 'Lancer du marteau', 'Saut à la perche']))