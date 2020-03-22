-- drop table CLUB;
-- drop table COUREUR; 
-- drop table EFFECTUER; 
-- drop table EVENEMENT; 
-- drop table CATEGORIE; 
-- drop table LIEU;
-- drop table COURSE;
-- Ce script n'est pas bon car les tables ne sont pas supprimés dans le bon ordre 
-- du point de vue des clés étrangères nombreuses

-- Il faut appliquer la suppression dans cet ordre pour qu'il n'y ai pas de problèmes
drop table Effectuer;
drop table Coureur;
drop table Course;
drop table Evenement;
drop table Club;
drop table Categorie;
drop table Lieu;