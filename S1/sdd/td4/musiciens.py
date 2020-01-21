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
assert groupe_clavier_modele1(exemple_modele1) == 2, 'Erreur'

def musicien_pink_floyd_modele1 (dico_musiciens) :
    res = 0
    for groupe, instruments in dico_musiciens.keys() :
        if groupe == 'Pink Floyd' :
            res += 1
    return res
assert musicien_pink_floyd_modele1(exemple_modele1) == 3, 'Erreur'


exemple_modele2 = {'Beatles' : {'Batterie':'Ringo Starr', 'Chant':'John Lennon',
'Clavier':'John Lennon'}, 'Pink Floyd' : {'Chant':'Syd Barrett', 'Guitare':'Syd Barrett', 
'Clavier':'Richard Wright'}, 
'Téléphone' : {'Chant':'Jean-Louis Aubert', 'Guitare':'Louis Bertignac',
'Basse':'Corine Marienneau'}, 'The Eagles' : {'Chant':'Glenn Frey',
'Batterie':'Don Henley', 'Guitare':'Joe Walsh'}}

def groupe_clavier_modele2 (dico_groupes) :
    res = 0
    for instruments in dico_groupes.values() :
        if 'Clavier' in instruments.keys() : 
            res += 1
    return res 
assert groupe_clavier_modele2(exemple_modele2) == 2, "Erreur"

def musicien_pink_floyd_modele2 (dico_groupes) :
    return len(dico_groupes['Pink Floyd'])
assert musicien_pink_floyd_modele2(exemple_modele2) == 3, 'Erreur'



exemple_modele3 = {'Batterie' : {'Beatles' : 'Ringo starr', 'The Eagles' : 'Don Henley'},
'Chant' : {'Beatles' : 'John Lennon', 'The Eagles' : 'Glenn Frey', 'Pink Floyd' : 'Sid Barrett', 'Telephone' : 'Jean-Louis Aubert'},
'Clavier' : {'Beatles' : 'John Lennon', 'Pink Floyd' : 'Richard Wright'},
'Guitare' : {'The Eagles' : 'Joe Walsh', 'Pink Floyd' : 'Syd Barrett', 'Telephone' : 'Louis Bertignac'},
'Basse' : {'Telephone' : 'Corine Marienneau'}}

def groupe_clavier_modele3 (dico_instruments) :
    return len(dico_instruments['Clavier'])
assert groupe_clavier_modele3(exemple_modele3) == 2, "Erreur"

def musicien_pink_floyd_modele3 (dico_instruments) :
    res = 0
    for groupes in dico_instruments.values() :
        if 'Pink Floyd' in groupes.keys() :
            res += 1
    return res
assert musicien_pink_floyd_modele3(exemple_modele3) == 3, 'Erreur'