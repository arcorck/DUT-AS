drop table if exists CONSTITUER;
drop table if exists INCOMPATIBLE;
drop table if exists COMPOSE;
drop table if exists TYPE;
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