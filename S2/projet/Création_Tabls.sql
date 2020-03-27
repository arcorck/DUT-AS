-- DROP TABLE STATISTIQUES;
-- DROP TABLE PLATEFORME;
-- DROP TABLE STATISTIQUE_PARTIE;
-- DROP TABLE MESSAGE;
-- DROP TABLE INVITATION;
-- DROP TABLE UTILISATEUR;
-- DROP TABLE ADMINISTRATEUR;
-- DROP TABLE PARTIE;


CREATE TABLE `PARTIE` (
  `IdPartie` int(5) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `NumeroEtape` int(5) DEFAULT NULL,
  `Score` int(20) DEFAULT NULL,
  `DateDebut` date DEFAULT NULL,
  `DateFin` date DEFAULT NULL,
  `IdJoueur1` int(15) DEFAULT NULL UNIQUE,
  `IdJoueur2` int(15) DEFAULT NULL UNIQUE,
  `NbCoups` int(2) DEFAULT NULL UNIQUE,
  `IdPlateforme` int(5)
) ;

CREATE TABLE `INVITATION` (
  `NumeroInvitation` int(5) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `DemandeAmi` varchar(150) DEFAULT NULL,
  `InvitationPartie` varchar(150) DEFAULT NULL,
  `DateDemandeAmi` date DEFAULT NULL,
  `DateInvitationPartie` date DEFAULT NULL,
  `IdUtilisateur` int(5)
) ;

CREATE TABLE `MESSAGE` (
  `IdMessage` int(5) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `ContenuMessage` varchar(400) DEFAULT NULL,
  `Expediteur` varchar(32) DEFAULT NULL,
  `Destinateur` varchar(32) DEFAULT NULL,
  `DateMessage` date DEFAULT NULL,
  `IdUtilisateur` int(5) DEFAULT NULL
) ;

create table `UTILISATEUR` (
  `IdUtilisateur` int(5) PRIMARY KEY,
  `Pseudo` varchar(32),
  `Email` varchar(150),
  `Mdp` varchar(16),
  `Avatar` varchar(32),
  `EtatUtil` boolean,
  `IdAdmin` int(5)
);

create table `PLATEFORME`(
  `IdPlateforme` int(5) PRIMARY KEY,
  `EtatPlateforme` varchar(10),
  `IdStats` int(5)
);

create table `STATISTIQUES`(
  `IdStats` int(5) PRIMARY KEY,
  `PartieJoue` int(5),
  `MeilleurJoueur` int(5),
  `IdUtilisateur` int(5)
);

create table `ADMINISTRATEUR`(
  `IdAdmin` int(5) PRIMARY KEY,
  `PseudoAdmin` varchar(32),
  `Rapport` varchar(300)
);

CREATE TABLE `STATISTIQUE_PARTIE`(
    `IdStatsPartie` int(5) PRIMARY KEY NOT NULL AUTO_INCREMENT, -- stats partie
    `CoupMini` int(2) DEFAULT NULL,
    `IdJoueur1` int(5) DEFAULT NULL,
    `IdJoueur2` int(5) DEFAULT NULL,
    `NbPartieJoue` int(2) DEFAULT NULL
);

ALTER TABLE STATISTIQUES ADD FOREIGN KEY (IdUtilisateur) REFERENCES UTILISATEUR (IdUtilisateur);
ALTER TABLE UTILISATEUR ADD FOREIGN KEY (IdAdmin) REFERENCES ADMINISTRATEUR (IdAdmin);
ALTER TABLE INVITATION ADD FOREIGN KEY (IdUtilisateur) REFERENCES UTILISATEUR (IdUtilisateur);
ALTER TABLE MESSAGE ADD FOREIGN KEY (IdUtilisateur) REFERENCES UTILISATEUR (IdUtilisateur);
ALTER TABLE PARTIE ADD FOREIGN KEY (IdPlateforme) REFERENCES PLATEFORME (IdPlateforme);
ALTER TABLE STATISTIQUE_PARTIE ADD FOREIGN KEY (CoupMini) REFERENCES PARTIE (NbCoups);
ALTER TABLE STATISTIQUE_PARTIE ADD FOREIGN KEY (IdJoueur1) REFERENCES UTILISATEUR (IdUtilisateur);
ALTER TABLE STATISTIQUE_PARTIE ADD FOREIGN KEY (IdJoueur2) REFERENCES UTILISATEUR (IdUtilisateur);
ALTER TABLE PLATEFORME ADD FOREIGN KEY (IdStats) REFERENCES STATISTIQUES (IdStats);
