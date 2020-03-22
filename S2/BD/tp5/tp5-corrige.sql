---------------------
-- Exercice 1
---------------------

\! echo "Exercice 1"

-- requete 1

\! echo "requete 1"

DROP TABLE IF EXISTS EFFECTUER;
DROP TABLE IF EXISTS COURSE;
DROP TABLE IF EXISTS EVENEMENT;
DROP TABLE IF EXISTS LIEU;
DROP TABLE IF EXISTS COUREUR;
DROP TABLE IF EXISTS CLUB;
DROP TABLE IF EXISTS CATEGORIE;

CREATE TABLE EVENEMENT (
  idEv int,
  nomEv varchar(15),
  dateEv date,
  idL int,
  PRIMARY KEY (idEv)
);

CREATE TABLE LIEU (
  idL int,
  nomL varchar(30),
  PRIMARY KEY (idL)
);

CREATE TABLE COURSE (
  idEv int,
  idCourse int,
  heure time,
  idCat int,
  PRIMARY KEY (idEv, idCourse)
);

CREATE TABLE EFFECTUER (
  idCo int,
  idEv int,
  idCourse int,
  temps time,
  PRIMARY KEY (idCo, idEv, idCourse)
);

CREATE TABLE COUREUR (
  idCo int,
  nomCo varchar(15),
  prenomCo varchar(15),
  idCat int,
  idCl int,
  PRIMARY KEY (idCo)
);

CREATE TABLE CLUB (
  idCl int,
  sigleCl varchar(10),
  nomCl varchar(30),
  PRIMARY KEY (idCl)
);

CREATE TABLE CATEGORIE (
  idCat int,
  nomCat varchar(10),
  PRIMARY KEY (idCat)
);

ALTER TABLE EVENEMENT ADD FOREIGN KEY (idL) REFERENCES LIEU (idL);
ALTER TABLE COURSE ADD FOREIGN KEY (idCat) REFERENCES CATEGORIE (idCat);
ALTER TABLE COURSE ADD FOREIGN KEY (idEv) REFERENCES EVENEMENT (idEv);
ALTER TABLE EFFECTUER ADD FOREIGN KEY (idEv, idCourse) REFERENCES COURSE (idEv, idCourse);
ALTER TABLE EFFECTUER ADD FOREIGN KEY (idCo) REFERENCES COUREUR (idCo);
ALTER TABLE COUREUR ADD FOREIGN KEY (idCl) REFERENCES CLUB (idCl);
ALTER TABLE COUREUR ADD FOREIGN KEY (idCat) REFERENCES CATEGORIE (idCat);
-- requete 3

\! echo "requete 3"

DROP TABLE EFFECTUER;
DROP TABLE COURSE;
DROP TABLE EVENEMENT;
DROP TABLE LIEU;
DROP TABLE COUREUR;
DROP TABLE CLUB;
DROP TABLE CATEGORIE;
-- requete 4

\! echo "requete 4"

DROP TABLE IF EXISTS EFFECTUER;
DROP TABLE IF EXISTS COURSE;
DROP TABLE IF EXISTS EVENEMENT;
DROP TABLE IF EXISTS LIEU;
DROP TABLE IF EXISTS COUREUR;
DROP TABLE IF EXISTS CLUB;
DROP TABLE IF EXISTS CATEGORIE;

CREATE TABLE EVENEMENT (
  idEv int,
  nomEv varchar(15),
  dateEv date,
  idL int,
  PRIMARY KEY (idEv)
);

CREATE TABLE LIEU (
  idL int,
  nomL varchar(30),
  PRIMARY KEY (idL)
);

CREATE TABLE COURSE (
  idEv int,
  idCourse int,
  heure time,
  idCat int,
  PRIMARY KEY (idEv, idCourse)
);

CREATE TABLE EFFECTUER (
  idCo int,
  idEv int,
  idCourse int,
  temps time,
  PRIMARY KEY (idCo, idEv, idCourse)
);

CREATE TABLE COUREUR (
  idCo int,
  nomCo varchar(15),
  prenomCo varchar(15),
  idCat int,
  idCl int,
  PRIMARY KEY (idCo)
);

CREATE TABLE CLUB (
  idCl int,
  sigleCl varchar(10),
  nomCl varchar(30),
  PRIMARY KEY (idCl)
);

CREATE TABLE CATEGORIE (
  idCat int,
  nomCat varchar(10),
  PRIMARY KEY (idCat)
);

ALTER TABLE EVENEMENT ADD FOREIGN KEY (idL) REFERENCES LIEU (idL);
ALTER TABLE COURSE ADD FOREIGN KEY (idCat) REFERENCES CATEGORIE (idCat);
ALTER TABLE COURSE ADD FOREIGN KEY (idEv) REFERENCES EVENEMENT (idEv);
ALTER TABLE EFFECTUER ADD FOREIGN KEY (idEv, idCourse) REFERENCES COURSE (idEv, idCourse);
ALTER TABLE EFFECTUER ADD FOREIGN KEY (idCo) REFERENCES COUREUR (idCo);
ALTER TABLE COUREUR ADD FOREIGN KEY (idCl) REFERENCES CLUB (idCl);
ALTER TABLE COUREUR ADD FOREIGN KEY (idCat) REFERENCES CATEGORIE (idCat);
-- requete 4

\! echo "requete 4"

insert into CLUB(idCl,sigleCl,nomCl) values 
       (1,'USO','Union Sportive Orléans'),
       (2,'ASM','Association Sportive Monts');
insert into CATEGORIE(idCat,nomCat) values 
       (1, 'Senior'), 
       (2,'Junior');
insert into LIEU(idL,nomL) values 
       (1,'Orléans'), 
       (2,'Olivet'), 
       (3,'Tours');
insert into EVENEMENT(idEv,nomEv,dateEv,idL) values
       (1,'Foulées',STR_TO_DATE('12/12/15','%d/%m/%Y'),1),
       (2,'Corrida',STR_TO_DATE('25/12/15','%d/%m/%Y'),2),
       (3,'Cross''O',STR_TO_DATE('10/01/16','%d/%m/%Y'),1),
       (4,'Vite-Tours',STR_TO_DATE('18/03/16','%d/%m/%Y'),3);
insert into COURSE(idEv,idCourse,heure,idCat) values
       (1,1,STR_TO_DATE('09:00','%H:%i'),1),
       (2,1,STR_TO_DATE('11:00','%H:%i'),2),
       (3,1,STR_TO_DATE('10:00','%H:%i'),2),
       (4,1,STR_TO_DATE('09:00','%H:%i'),1),
       (4,2,STR_TO_DATE('10:30','%H:%i'),2);
insert into COUREUR(idCo,nomCo,prenomCo,idCl,idCat) values 
       (1, 'Dupont','Jean',1,1),
       (2, 'Duval', 'Marie',2,2);

insert into EFFECTUER(idCo,idEv,idCourse,temps) values
       (1,1,1,STR_TO_DATE('12:32','%i:%s')),
       (2,2,1,STR_TO_DATE('11:53','%i:%s')),
       (2,3,1,STR_TO_DATE('11:59','%i:%s'));
-- requete 5

\! echo "requete 5"

delete from CLUB where sigleCl='USO';
-- ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`limet`.`COUREUR`, CONSTRAINT `COUREUR_ibfk_1` FOREIGN KEY (`idcl`) REFERENCES `CLUB` (`idcl`))
---------------------
-- Exercice 2
---------------------

\! echo "Exercice 2"

-- requete 1

\! echo "requete 1"

-- Complément jeu d'essai
insert into COURSE(idEv,idCourse,heure,idCat) values
       (2,2,STR_TO_DATE('09:15','%H:%i'),1);
insert into COUREUR(idCo,nomCo,prenomCo,idCl,idCat) values 
       (3, 'Mansoif','Gérard',1,1),
       (4, 'Terrieur', 'Alex',1,1),
       (5, 'Lelivre','Julie',2,2);

insert into EFFECTUER(idCo,idEv,idCourse,temps) values
       (3,1,1,STR_TO_DATE('12:10','%i:%s')),
       (4,4,1,STR_TO_DATE('15:23','%i:%s')),
       (5,3,1,STR_TO_DATE('17:02','%i:%s')),
       (3,2,2,STR_TO_DATE('18:31','%i:%s'));
-- requete 1

\! echo "requete 1"

select nomEv, dateEv 
from EVENEMENT natural join LIEU 
where nomL='Orléans' 
order by dateEv;

select nomEv, dateEv
from EVENEMENT 
where idL in (select idL
              from LIEU
              where nomL='Orléans') 
order by dateEv;
-- requete 2

\! echo "requete 2"

select nomCo, prenomCo, temps
from COUREUR natural join EFFECTUER natural join EVENEMENT natural join 
     COURSE natural join LIEU natural join CLUB natural join CATEGORIE 
where nomEv='Foulées' and nomL='Orléans' and sigleCl='USO' and nomCat='Senior'
order by temps;

select nomCo, prenomCo, temps 
from COUREUR natural join EFFECTUER natural join 
     EVENEMENT natural join COURSE 
where nomEv='Foulées' and
      idL in (select idL from LIEU where nomL='Orléans') and 
      idCl in (select idCl from CLUB where sigleCL='USO') and
      idCat in (select idCat from CATEGORIE where nomCat='Senior')
order by temps;
-- requete 3

\! echo "requete 3"

select distinct nomEv, nomCat, nomL, dateEv 
from COUREUR natural join EFFECTUER natural join 
     EVENEMENT natural join COURSE natural join LIEU natural join CLUB
     natural join CATEGORIE 
where sigleCl='USO';

select nomEv, nomCat, nomL, dateEv
from EVENEMENT natural join COURSE natural join LIEU natural join CATEGORIE 
where (idEv,idCourse) in (
   select idEv, idCourse 
   from COUREUR natural join EFFECTUER 
        natural join CLUB
   where sigleCl='USO')
;

-- requete 4

\! echo "requete 4"

select distinct nomCo, prenomCo 
from COUREUR natural join EFFECTUER natural join 
     COURSE natural join CATEGORIE 
where nomCat='Junior';

select nomCo, prenomCo 
from COUREUR 
where idCo in (
     select idCo
     from EFFECTUER natural join 
          COURSE natural join CATEGORIE 
     where nomCat='Junior')
;
-- requete 5

\! echo "requete 5"

select distinct  nomCo, prenomCo 
from COUREUR C,  EFFECTUER E1, EFFECTUER E2
where C.idCo=E1.idCo and C.idCo=E2.idCo and
      E1.idEv in (select idEv
                      from EVENEMENT natural join LIEU
                      where nomL='Orléans' and nomEv='Foulées')
      and
      E2.idEv in (select idEv
                      from EVENEMENT natural join LIEU
                      where nomL='Olivet' and nomEv='Corrida')
;
