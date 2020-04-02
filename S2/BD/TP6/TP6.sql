DROP TABLE CONSTITUER;
DROP TABLE INCOMPATIBLE;
DROP TABLE COMPOSE;
DROP TABLE FORMULE;
DROP TABLE TYPE;



CREATE TABLE `COMPOSE` ( 
    `refcomp` varchar(4) PRIMARY KEY,
    `nomcomp` varchar(20),
    `idty` varchar(5) UNIQUE
);


CREATE TABLE `CONSTITUER` ( 
    `idform` varchar(5),
    `refcomp` varchar(4), 
    `qte` decimal(5,2),
    PRIMARY KEY (refcomp , idform) 
);

CREATE TABLE `FORMULE` (
    `idform` varchar(5) PRIMARY KEY, 
    `nomform` varchar(15)
);

CREATE TABLE `INCOMPATIBLE` (
    `refcomp_1` varchar(4), 
    `refcomp_2` varchar(4),
    PRIMARY KEY (refcomp_1 , refcomp_2)
);

CREATE TABLE `TYPE` (
    `idty` varchar(5) PRIMARY KEY,
    `nomty` varchar (20)
);

ALTER TABLE CONSTITUER ADD FOREIGN KEY (idform) REFERENCES FORMULE (idform);
ALTER TABLE CONSTITUER ADD FOREIGN KEY (refcomp) REFERENCES COMPOSE (refcomp); 
ALTER TABLE INCOMPATIBLE ADD FOREIGN KEY (refcomp_1) REFERENCES COMPOSE (refcomp); 
ALTER TABLE INCOMPATIBLE ADD FOREIGN KEY (refcomp_2) REFERENCES COMPOSE (refcomp);
ALTER TABLE COMPOSE ADD FOREIGN KEY (idty) REFERENCES TYPE (idty);

-- appeler une fonction : select
-- appeler une procedure : call

-- EXERCICE 1 


-- Question 1
delimiter |
drop function if exists premier|
create function premier(liste varchar(255)) returns varchar(20)
begin
   declare res varchar(20);
   declare pos int;
   set pos:=LOCATE(',',liste,1);
   if pos = 0 then
      set res:=liste;
   else
      set res:=substring(liste,1,pos-1);
   end if;
   return res;
end|
delimiter ;


-- Question 2
delimiter |
drop function if exists reste|
create function reste(liste varchar(255)) returns varchar(20)
begin
   declare res varchar(20);
   declare pos int;
   set pos:=LOCATE(',',liste,1);
   if pos = 0 then
      set res:="";
   else
      set res:=substring(liste,pos+1,LENGTH(liste)-pos);
   end if;
   return res;
end|
delimiter ;


-- Question 3
delimiter |
drop procedure if exists testerListe|
create procedure testerListe(liste varchar(255))
begin
   declare elem varchar(30);
   drop table if exists TEST_TP6;
   create table TEST_TP6(elem varchar(30));
   while liste !='' do
       set elem:=premier(liste);
       insert into TEST_TP6 values(elem);
       set liste:=reste(liste);
   end while;
end|
delimiter ;





-- EXERCICE 2

-- Question 1
delimiter |
drop function if exists nbFormules|
create function nbFormules(nomCompose varchar(20)) returns int
begin
   declare nbforms int;
   select count(idForm) into nbforms from CONSTITUER natural join COMPOSE where nomComp = nomCompose;
   return nbforms;
end|
delimiter ;

-- Question 2
delimiter |
drop procedure if exists creerFormule|
create procedure creerFormule(idF varchar(5), nomF varchar(15), listeComposes varchar(255))
begin
   declare comp varchar(20)
   declare refCompose varchar(4)
   insert into FORMULE VALUES (idF, nomF);
   while listeComposes != '' do
      set Comp = premier(listeComposes);
      select refComp into refCompose from COMPOSE where nomComp = Comp;
      INSERT INTO CONSTITUER VALUES (idF, refCompose, 1);
      set listeComposes := reste(listeComposes);
   end while;
end|
delimiter ;



-- Exercice 3
drop function if exists genereEtiquette|
create function genereEtiquette(nomFormule varchar(15)) returns varchar(255)
begin
   declare res varchar(255) default concat(nomFormule,':');
   declare fini int default false;
   declare unIngr varchar(20);
   declare quantite decimal(5,2);
   declare ingredients cursor for 
       select nomComp, qte
       from FORMULE natural join CONSTITUER natural join COMPOSE
       where FORMULE.nomForm = nomFormule;
   declare continue handler for not found set fini = true;

   open ingredients;
   while not fini do
      fetch ingredients into unIngr, quantite;
      if not fini then
         set res := concat(res,concat(' ',unIngr));
     set res := concat(res,concat('(',concat(convert(quantite,char),')')));
      end if;
   end while;
   close ingredients;
   return res;
end|