liste_pokemon = [('Bulbizarre', {'Plante', 'Poison'}, '001.png'), ('Herbizarre', {'Plante', 'Poison'}, '002.png'),('Abo', {'Poison'}, '023.png'),('Jungko', {'Plante'}, '024.png')]

def dico_pokemon (liste_pokemon) :
    res = {}
    for pokemon, types, _ in liste_pokemon :
        #print (types)
        for type_pok in types : 
            #print(type_pok)
            if type_pok in res :
                if pokemon not in res[type_pok] :
                    res[type_pok].add(pokemon)
                else : 
                    res[type_pok] = set()
                    res[type_pok].add(pokemon)
            else : 
                res[type_pok] = set()
                res[type_pok].add(pokemon)
    return res

assert dico_pokemon(liste_pokemon) == {'Poison': {'Herbizarre', 'Abo', 'Bulbizarre'}, 'Plante': {'Herbizarre', 'Bulbizarre', 'Jungko'}}, "Erreur"