/* CREATE DATABASE IF NOT EXISTS Facture DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE Facture;
*/

CREATE TABLE CLIENT (
  numCli int,
  nomCli varchar(15),
  prenomCli varchar(15),
  adresseCli varchar(15),
  PRIMARY KEY (numCli)
);

CREATE TABLE FACTURE (
  numFac int,
  dateFac date,
  numCli int,
  PRIMARY KEY (numFac)
);

CREATE TABLE DETAIL (
  numFac int,
  refProd int,
  qte int,
  PRIMARY KEY (numFac, refProd)
);

CREATE TABLE PRODUIT (
  refProd int,
  nomProd varchar(15),
  puProd decimal(6,2),
  PRIMARY KEY (refProd)
);

ALTER TABLE FACTURE ADD FOREIGN KEY (numCli) REFERENCES CLIENT (numCli);
ALTER TABLE DETAIL ADD FOREIGN KEY (refProd) REFERENCES PRODUIT (refProd);
ALTER TABLE DETAIL ADD FOREIGN KEY (numFac) REFERENCES FACTURE (numFac);