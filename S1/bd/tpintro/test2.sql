drop table Posseder;
drop table Habitant;
drop table Voiture;

create table Habitant(
Id Number(2),
Prenom Varchar2(20),
Nom Varchar2(20),
Sexe Varchar2(1),
Rue Varchar2(20),
Num Number(2),
Ville Varchar2(10),
constraint KeyHabitant PRIMARY KEY (Id)
);

create table Voiture(
MarqueV Varchar2(10),
NomV Varchar2(10),
AnneeV Number(4),
CouleurV Varchar2(10),
TypeMoteurV Varchar2(10),
ImmV Varchar2(12),
constraint KeyVoiture PRIMARY KEY (ImmV)
);

create table Posseder(
Id Number(2),
ImmV Varchar2(10),
constraint FKHabitant FOREIGN KEY (Id) REFERENCES Habitant (Id),
constraint FKVoiture FOREIGN KEY (ImmV) REFERENCES Voiture (ImmV)
);


insert into Voiture values ('Renault', 'Clio', 2017, 'bleu', 'essence', 'MM-222-XY');

--insert into Voiture values ('citroen', 'c3', 2012, 'violette', 'ethanol', 'MM-222-XY');

insert into Voiture values ('Toyota', 'Verso', 2015, 'bleu', 'diesel', 'AA-333-BB');

insert into Habitant values (4, 'Julien', 'Dupont', 'M', 'Cherche Midi', 4, 'Paris');

insert into Habitant values (5, 'Marie', 'Dupont', 'F', 'Cherche Midi', 4, 'Paris');

insert into Habitant values (6, 'Carol', 'Alves', 'F','Denis Papin', 43, 'Orleans');

--insert into Habitant values (4, 'Peter', 'Smith', 'M', 'Saint Jacques', 4, 'Paris') ;

insert into Posseder values (4, 'MM-222-XY');

insert into Posseder values (5, 'MM-222-XY');

insert into Posseder values (6, 'AA-333-BB');

--insert into Posseder values (4, 'AA-333-CC');

--insert into Posseder values (7, 'AA-333-BB');

select * from Habitant;

select * from Voiture;

select * from Posseder;