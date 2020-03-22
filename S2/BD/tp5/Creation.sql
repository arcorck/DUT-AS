CREATE TABLE `Lieu` (
  `idL` int(5) PRIMARY KEY NOT NULL ,
  `nomL` varchar(50) DEFAULT NULL
) ;

CREATE TABLE `Evenement` (
  `idEv` int(5) PRIMARY KEY NOT NULL ,
  `nomEv` varchar(50) DEFAULT NULL,
  `dateEv` DATE DEFAULT NULL,
  `idL` int(5) DEFAULT NULL,
  FOREIGN KEY (idL) REFERENCES Lieu(idL)
) ;

CREATE TABLE `Categorie` (
  `IdCat` int(5) PRIMARY KEY NOT NULL ,
  `nomCat` varchar(50) DEFAULT NULL
) ;

CREATE TABLE `Course` (
  `idEv` int(5) NOT NULL ,
  `idCourse` int(5) NOT NULL,
  `heure` TIME DEFAULT NULL,
  `idCat` int(5) DEFAULT NULL,
  PRIMARY KEY (idEv, idCourse),
  FOREIGN KEY (idEv) REFERENCES Evenement(idEv),
  FOREIGN KEY (idCat) REFERENCES Categorie(idCat)
) ;

CREATE TABLE `Club` (
  `idCl` int(5) PRIMARY KEY NOT NULL ,
  `sigleCl` varchar(50) DEFAULT NULL,
  `nomCl` varchar(50) DEFAULT NULL
) ;

CREATE TABLE `Coureur` (
  `idCo` int(5) PRIMARY KEY NOT NULL ,
  `nomCo` varchar(20) DEFAULT NULL,
  `prenomCo` varchar(20) DEFAULT NULL,
  `idCat` int(5) DEFAULT NULL,
  `idCl` int(5) DEFAULT NULL,
  FOREIGN KEY (idCat) REFERENCES Categorie(idCat),
  FOREIGN KEY (idCl) REFERENCES Club(idCl)
) ;

CREATE TABLE `Effectuer` (
  `idCo` int(5) NOT NULL,
  `idEv` int(5) NOT NULL,
  `idCourse` int(5) NOT NULL,
  `temps` Time DEFAULT NULL,
  PRIMARY KEY (idCo, idEv, idCourse));


ALTER TABLE EFFECTUER ADD FOREIGN KEY (idEv, idCourse) REFERENCES COURSE (idEv, idCourse);
ALTER TABLE EFFECTUER ADD FOREIGN KEY (idCo) REFERENCES COUREUR (idCo);
