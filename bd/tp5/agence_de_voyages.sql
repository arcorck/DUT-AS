drop table Activite;
drop table Client;
drop table Sejour;
drop table Station;


create table Station (
    nomStation Varchar2(20) NOT NULL primary key,
    capacite Number(5) NOT NULL,
    lieu Varchar2(25) NOT NULL,
    region Varchar2(20),
    tarif Number(4) DEFAULT 0,
    check (region = 'Ocean Indien' or region = 'Europe' or region = 'Ameriques' or region = 'Antilles' or region = 'Extreme Orient'));

create table Activite (
    nomStation Varchar2(20) NOT NULL, 
    libelle Varchar2(20),
    prix Number(4) DEFAULT 0,
    constraint keyActivite primary key (libelle),
    constraint FKActStation foreign key (nomStation) references Station(nomStation) on delete cascade);

create table Client (
    id Number(4), 
    nom Varchar2(20), 
    prenom Varchar2(20), 
    ville Varchar2(20), 
    region Varchar2(20), 
    solde Number(6) DEFAULT 0 NOT NULL,
    constraint keyClient primary key (id),
    check (region = 'Ocean Indien' or region = 'Antilles' or region = 'Europe' or region = 'Ameriques' or region = 'Extreme Orient'));

create table Sejour (
    id Number(4),
    station Varchar2(20),  
    debut date, 
    nbPlaces Number(4) NOT NULL,
    constraint keysejour primary key (id, debut),
    constraint FKSejoursStation foreign key (station) references Station(nomStation) on delete cascade);
    
insert into Station values ('Venusa', 350, 'Guadeloupe', 'Antilles', 1200);
insert into Station values ('Cabo Frio', 450, 'Bresil', 'Ameriques', 1200);
insert into Activite values('Venusa', 'Voile', 150);
insert into Activite values('Venusa', 'Plongee', 250);
insert into Activite values('Cabo Frio', 'Natation', 50);
insert into Client values (10, 'Foog', 'Phileas', 'Londres', 'Europe', 12465);
insert into Client values (20, 'Pascal', 'Blaise', 'Paris', 'Europe', 6785);
insert into Client values (30, 'Kerouac', 'Jack', 'New-York', 'Ameriques', 8543);
insert into Sejour values (30, 'Venusa', '06-02-2010', 2);
insert into Sejour values (10, 'Venusa', '06-02-2010', 3);
insert into Sejour values (20, 'Venusa', '06-02-2010', 3);
insert into Sejour values (10, 'Cabo Frio', '08-02-2010', 2);