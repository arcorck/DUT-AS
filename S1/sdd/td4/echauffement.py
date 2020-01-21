exemple1 = {'The Pokemon Lego Movie' : (1000, 3000), 'Avengers Vs Predators' : (4000, 20), 'My Atomic Little Pony' : (2000, 2000), 'Z II' : (3, 5)}

def films_plutot_japonnais (box_office) :
    res = ''
    for (film, (entrees_jp, entrees_us)) in box_office.items() :
        if entrees_jp > entrees_us :
            res = film
    return res
assert films_plutot_japonnais(exemple1) == 'Avengers Vs Predators', "Erreur"

def no_famous_in_us (box_office) :
    min = None
    film_no_famous_in_us = None
    for film,(entrees_jp, entrees_us) in box_office.items() :
        if min is None or entrees_us < min :
            min = entrees_us
            film_no_famous_in_us = film
    return film_no_famous_in_us
assert no_famous_in_us(exemple1) == 'Z II', 'Erreur'

