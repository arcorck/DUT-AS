drop table if exists CONSTITUER;
drop table if exists INCOMPATIBLE;
drop table if exists COMPOSE;
drop table if exists TYPE;
drop table if exists PRODUCTION;
drop table if exists FORMULE;

CREATE TABLE COMPOSE (
  refcomp varchar(4),
  nomcomp varchar(20),
  PRIMARY KEY (refcomp)
);

CREATE TABLE CONSTITUER (
  idform varchar(5),
  refcomp varchar(4),
  qte decimal(5,2),
  PRIMARY KEY (refcomp, idform)
);

CREATE TABLE FORMULE (
  idform varchar(5),
  nomform varchar(15),
  PRIMARY KEY (idform)
);

CREATE TABLE INCOMPATIBLE (
  refcomp_1 varchar(4),
  refcomp_2 varchar(4),
  PRIMARY KEY (refcomp_1, refcomp_2)
);

ALTER TABLE CONSTITUER ADD FOREIGN KEY (idform) REFERENCES FORMULE (idform);
ALTER TABLE CONSTITUER ADD FOREIGN KEY (refcomp) REFERENCES COMPOSE (refcomp);
ALTER TABLE INCOMPATIBLE ADD FOREIGN KEY (refcomp_1) REFERENCES COMPOSE (refcomp);
ALTER TABLE INCOMPATIBLE ADD FOREIGN KEY (refcomp_2) REFERENCES COMPOSE (refcomp);

insert into COMPOSE values ('Me01','Mercure'), ('Al01','Alcool'),('Ox01','Oxygène'), ('Di01','Dioxyde de soufre'), ('Di02','Dioxyde d''oxygène'), ('Su01','Sucre');
insert into INCOMPATIBLE values ('Me01','Al01'), ('Me01','Ox01');
insert into FORMULE values ('Po001','Pommade'), ('Co001', 'Comprimés');
insert into CONSTITUER values ('Po001','Al01',1.2), ('Po001','Di01',0.5),('Co001', 'Di01',0.01),('Co001','Su01',5.3), ('Co001','Di02',1.2); 

create table PRODUCTION(
    idform varchar(5) primary key, 
    qteAProduire int, 
    foreign key (idform) references FORMULE(idform) 
);

insert into PRODUCTION values ('Co001',5),('Po001',10);


-- Question 1
delimiter |
drop procedure if exists completeIncompatible|
create procedure completeIncompatible()
begin
    declare fini int default false;
    declare comp_1 varchar(4);
    declare comp_2 varchar(4);
    declare ingredients cursor for 
        select refComp_1, refComp_2 from INCOMPATIBLE;
    declare continue handler for not found set fini = true;
    open ingredients;
    while not fini do
        fetch ingredients into comp_1, comp_2;
        if not fini then
            INSERT INTO INCOMPATIBLE VALUES (comp_2, comp_1);
        end if;
    end while;
    close ingredients;
end|
delimiter ;

call completeIncompatible();


-- Question 2
delimiter |
drop function if exists effectuerCommande |
create function effectuerCommande() returns varchar(500)
  begin
  declare ReferenceCompose_bis varchar(4);
  declare QuantiteAProduire_bis int;
  declare NomFormule_bis varchar(15);
  declare Quantite_bis double;
  declare NomCompose_bis varchar(20);

  declare TotalProduit double;

  declare TotalProduits double;
  declare prec varchar(20);
  declare debut int;
  declare ResultatAAfficher varchar(500);
  declare fini int default false;

  declare curseur cursor for
   select refcomp,qteAProduire,nomform,qte,nomcomp
   from PRODUCTION natural join FORMULE natural join CONSTITUER natural join COMPOSE
   order by refcomp,qteAProduire desc;

  declare continue handler for not found set fini=true;

  set ResultatAAfficher:="\n";
  set TotalProduits=0;
  set TotalProduit=0;
  set debut=1;
  set prec='';

  open curseur;
  while not fini do
    fetch curseur into ReferenceCompose_bis,QuantiteAProduire_bis,NomFormule_bis,Quantite_bis,NomCompose_bis;
    if not fini then
      if prec=NomCompose_bis then
        set TotalProduit=QuantiteAProduire_bis*Quantite_bis;
        set TotalProduits=TotalProduits+TotalProduit;
        set ResultatAAfficher:=concat(concat(ResultatAAfficher,rpad(concat("  ",NomFormule_bis),25,' ')),Round(TotalProduit,2));
        set ResultatAAfficher:=concat(ResultatAAfficher,'\n');
        set prec:=NomCompose_bis;
      end if;

      if prec!=NomCompose_bis then
       if debut!=1 then
          set ResultatAAfficher:=concat(concat(ResultatAAfficher,rpad(concat("  ",'quantite totale'),25,' ')),Round(TotalProduits,2));
          set ResultatAAfficher:=concat(ResultatAAfficher,'\n');
          set TotalProduits=0;
          set TotalProduit=0;
          set ResultatAAfficher:=concat(concat(ResultatAAfficher,concat(ReferenceCompose_bis,' ')),concat(NomCompose_bis,'\n'));
          set TotalProduit=QuantiteAProduire_bis*Quantite_bis;
          set TotalProduits=TotalProduits+TotalProduit;
          set ResultatAAfficher:=concat(concat(ResultatAAfficher,rpad(concat("  ",NomFormule_bis),25,' ')),Round(TotalProduit,2));
          set ResultatAAfficher:=concat(ResultatAAfficher,'\n');
          set prec:=NomCompose_bis;
       end if;
      end if;

      if prec!=NomCompose_bis then
        if debut=1 then
          set ResultatAAfficher:=concat(concat(ResultatAAfficher,concat(ReferenceCompose_bis,' ')),concat(NomCompose_bis,'\n'));
          set TotalProduit=QuantiteAProduire_bis*Quantite_bis;
          set TotalProduits=TotalProduits+TotalProduit;
          set ResultatAAfficher:=concat(concat(ResultatAAfficher,rpad(concat("  ",NomFormule_bis),25,' ')),Round(TotalProduit,2));
          set ResultatAAfficher:=concat(ResultatAAfficher,'\n');
          set debut=0;
          set prec:=NomCompose_bis;
        end if;
      end if;
    end if;

  end while;

  set ResultatAAfficher:=concat(concat(ResultatAAfficher,rpad(concat("  ",'quantite totale'),25,' ')),Round(TotalProduits,2));
  set ResultatAAfficher=concat(ResultatAAfficher,'\n');
  close curseur;
  return ResultatAAfficher;
  end|

delimiter ;

select effectuerCommande();