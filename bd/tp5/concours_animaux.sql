-- @ SCRIPTS/CreateDropConcoursAnimaux.sql;

drop table Classement;
drop table Concours;
drop table Animaux;
drop table Proprietaires;

create table Proprietaires
(Id Number(4)  primary key, 
Nom VarChar2(20),  
Prenom  VarChar2(20),
Ville Varchar2(20));

create table Animaux
( Prop Number(4),
NomAnimal VarChar2(20),  
Type VarChar2(10),  
Race VarChar2(10),  
Categorie VarChar2(10), 
DateNais date,
constraint keyAnimal primary key (Prop,NomAnimal),
constraint FKproprietaire foreign key (Prop) references Proprietaires (Id)); 

create table Concours
(Titre Varchar2(20),
Annee  date,
Categorie Varchar2(10),
Certificat Varchar2(20),
TypeConcours Varchar2(3),
Ville Varchar2(20),
check (TypeConcours = 'INT' or TypeConcours = 'NAT'),
constraint keyConcours primary key (Titre, Annee),
constraint uniqueConcours unique (Ville, Annee, Categorie));


create table Classement (
Prop Number(4) , 
Animal VarChar2(20), 
TitreC Varchar2(20),
AnneeC  date, 
PositionClassement number(3),
constraint KEYClassement primary key (Prop, Animal, TitreC, AnneeC),
constraint FKPropClassement foreign key (Prop) references Proprietaires(Id) on delete cascade,
constraint FKAnimalClassement foreign key (Prop, Animal) references Animaux(Prop,NomAnimal) on delete cascade,
constraint FKConcoursClassement foreign key (TitreC,AnneeC) references Concours(Titre, Annee) on delete cascade);

-- 1.1) pensez a ajouter en premier lieu le proprietaire car sinon erreur : cle etrangere vers id de proprietaire 
insert into Proprietaires values (123, 'Niarchos', 'Denis', 'Orleans');
insert into Animaux values (123, 'Bargos', 'course', '???', 'coureur', TO_DATE('01-01-2001', 'DD-MM-YYYY'));

-- 1.2) Non, car classement possede une cle etrangere sur chacune des autres tables de la base donc
-- si celles ci ne sont pas paramétrées correctement, on ne peut pas inserer dans classement

-- 1.3) et 1.4) liste des dependances fonctionnelles :
--   Proprietaire : Id -> Nom, Prenom, Ville
--   Animaux : Prop, Nom -> Type, Race, Categorie, DateNais
--   Concours : Titre, Annee -> Categorie, Certificat, TypeConcours, Ville
--   Classement : Prop, Animal, TitreC, AnneeC -> PositionClassement
--   Concours : Ville, Annee, Categorie -> Titre, Certificat, TypeConcours

-- 1.5) categorie de Animaux est inclus dans categorie de concours
--      nomanimal de animaux est inclus dans animal de classement
--      id de proprietaire est inclus dans prop de classement 

-- 1.6) Impossible car on doit d'abord supprimer toute les tables ayant une cle etrangere sur Propriétaire

-- 1.7) Cette contrainte veut dire qu'à une date donnée, à un lieu donnée et pour une catégorie donnée,
-- il ne peut y avoir qu'un seul concours 