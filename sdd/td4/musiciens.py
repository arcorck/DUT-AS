exemple_modele1 = {('Beatles','Batterie'):'Ringo Starr', ('Beatles','Chant'):'John Lennon',
('Beatles','Clavier'):'John Lennon', ('Pink Floyd','Chant'):'Syd Barrett', ('Pink Floyd','Guitare'):'Syd Barrett', 
('Pink Floyd','Clavier'):'Richard Wright', 
('Téléphone','Chant'):'Jean-Louis Aubert', ('Téléphone','Guitare'):'Louis Bertignac',
('Téléphone','Basse'):'Corine Marienneau', ('The Eagles','Chant'):'Glenn Frey',
('The Eagles','Batterie'):'Don Henley', ('The Eagles','Guitare'):'Joe Walsh',}

def groupe_clavier_modele1 (dico_musiciens) : 
    res = 0
    for groupe,instruments in dico_musiciens.keys() :
        if instruments == 'Clavier' :
            res += 1
    return res

def musicien_pink_floyd_modele1 (dico_musiciens) :
    res = 0
    for groupe, instruments in dico_musiciens.keys() :
        if groupe == 'Pink Floyd' :
            res += 1
    return res