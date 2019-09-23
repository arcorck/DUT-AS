create table Habitant(
Id Number(2),
Prenom Varchar2(20),
Nom Varchar2(20),
Sexe Varchar2(1),
Rue Varchar2(20),
page 2 sur 4
Num Number(2),
Ville Varchar2(10),
constraint KeyHabitant PRIMARY KEY (Id));

create table Voiture(
MarqueV Varchar2(10),
NomV Varchar2(10),
AnneeV Number(4),
CouleurV Varchar2(10),
TypeMoteurV Varchar2(10),
ImmV Varchar2(10),
constraint KeyVoiture PRIMARY KEY (ImmV));

create table Posseder(
Id Number(2),
ImmV Varchar2(10),
constraint FKHabitant FOREIGN KEY (Id) REFERENCES Habitant (Id),
constraint FKVoiture FOREIGN KEY (ImmV) REFERENCES Voiture (ImmV));
