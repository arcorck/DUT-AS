CREATE TABLE `PARTIE` (
  `IdPartie` int(15) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `NumeroEtape` int(5) DEFAULT NULL,
  `Score` int(20) DEFAULT NULL,
  `DateDebut` date DEFAULT NULL,
  `DateFin` date DEFAULT NULL
) ;

CREATE TABLE `INVITATION` (
  `NumeroInvitation` int(300) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `DemandeAmi` varchar(150) DEFAULT NULL,
  `InvitationPartie` varchar(150) DEFAULT NULL,
  `DateDemandeAmi` date DEFAULT NULL,
  `DateInvitationPartie` date DEFAULT NULL
) ;

CREATE TABLE `MESSAGE` (
  `IdMessage` int(300) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `ContenuMessage` varchar(400) DEFAULT NULL,
  `Expediteur` varchar(32) DEFAULT NULL,
  `Destinateur` varchar(32) DEFAULT NULL,
  `DateMessage` date DEFAULT NULL
) ;

