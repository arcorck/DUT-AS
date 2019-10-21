drop table BdHabitantVoiture;

create table BdHabitantVoiture(
Identinfiant Number(2),
Prenon Varchar2(20),
Nom Varchar2(20),
Sexe Varchar2(1),
Rue Varchar2(20),
Num Number(2),
Ville Varchar2(10),
MarqueV Varchar2(10),
NomV Varchar2(10),
AnneeV Number(4),
CouleurV Varchar2(10),
TypeMoteurV Varchar2(10),
ImmV Varchar2(10),
constraint CleGrandTableVoiture UNIQUE (ImmV),
constraint CleGrandTablePersonne PRIMARY KEY (Identinfiant)
);

insert into BdHabitantVoiture values (1, 'Arlette', 'Fort', 'F',
 'des Allouettes', 15, 'Olivet', 'Renault', 'Zoe', 2016, 
 'blanche', 'electrique', 'AD-123-EF');

insert into BdHabitantVoiture values (2, 'Arlette', 'Fort', 'F', 
'Alesia', 4, 'Paris', 'Renault', 'Clio', 2017, 
'blanche', 'essence', 'AB-333-CC');

insert into BdHabitantVoiture values (3, 'Arlette', 'Fort', 'F', 
'Alesia', 4, 'Paris', 'Renault', 'Clio', 2015,
 'noir', 'essence', 'AB-333-CC');

-- Mari et femme ont la meme voiture
insert into BdHabitantVoiture values (4, 'Julien', 'Dupont', 'M',
 'Cherche Midi', 4, 'Paris', 'Renault', 'Clio', 2017, 
 'bleu', 'essence', 'MM-222-XY');

insert into BdHabitantVoiture values (5, 'Marie', 'Dupont', 'F', 
'Cherche Midi', 4, 'Paris', 'Renault', 'Clio', 2017, 
'bleu', 'essence', 'MM-222-XY');
