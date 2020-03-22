INSERT INTO `Club`(`idCl`, `sigleCl`, `nomCl`) VALUES (1, 'USO', 'Union sportive Orléans Loiret footbal');
INSERT INTO `Categorie`(`idCat`,`nomCat`) VALUES (1,'Senior');
INSERT INTO `Lieu`(`idL`, `nomL`) VALUES (1,'Orleans');
INSERT INTO `Evenement` VALUES (1, 'Les Foulees Roses', '2015-12-12',1);
INSERT INTO `Coureur` (`idCo`, `nomCo`, `prenomCo`, `idCat`, `idCl`) VALUES (1, 'Dupont', 'Jean', 1, 1);
INSERT into `Course` VALUES (1, 1, '09:00:00', 1);
INSERT INTO `Effectuer` VALUES (1,1,1, '00:12:32');

INSERT INTO `Club`(`idCl`, `sigleCl`, `nomCl`) VALUES (2, 'ASM', 'ASM Clermont Auvergne Rugby');
INSERT INTO `Categorie`(`idCat`,`nomCat`) VALUES (2,'Junior');
INSERT INTO `Lieu`(`idL`, `nomL`) VALUES (2,'Olivet');
INSERT INTO `Evenement` VALUES (2, 'La Corrida', '2015-12-25',2);
INSERT INTO `Coureur` (`idCo`, `nomCo`, `prenomCo`, `idCat`, `idCl`) VALUES (2, 'Duval', 'Marie', 2, 2);
INSERT into `Course` VALUES (2, 2, '11:00:00', 2);
INSERT INTO `Effectuer` VALUES (2,2,2, '00:11:53');

INSERT INTO `Evenement` VALUES (3, 'Cross dOrleans', '2016-01-10',1);
INSERT into `Course` VALUES (3, 3, '10:00:00', 2);
INSERT INTO `Effectuer` VALUES (2,3,3, '00:08:59');

INSERT INTO `Lieu`(`idL`, `nomL`) VALUES (3,'Tours');
INSERT INTO `Evenement` VALUES (4, 'Vite-Tours', '2016-03-18',3);
INSERT into `Course` VALUES (4, 4, '09:00:00', 1);
INSERT into `Course` VALUES (4, 5, '10:30:00', 2);

-- On ne peut pas supprimer le club uso car il y a Jean Dupont qui appartient à ce Club

-- Supplément pour les requêtes
INSERT INTO `Club`(`idCl`, `sigleCl`, `nomCl`) VALUES (3, 'SOR', 'Stade Olympique Romorantin');
INSERT INTO `Categorie`(`idCat`,`nomCat`) VALUES (3,'Benjamin');
INSERT INTO `Club`(`idCl`, `sigleCl`, `nomCl`) VALUES (4, 'XV', 'Quinze de France');
INSERT INTO `Categorie`(`idCat`,`nomCat`) VALUES (4,'Poussin');
INSERT INTO `Coureur` (`idCo`, `nomCo`, `prenomCo`, `idCat`, `idCl`) VALUES (3, 'Dupont', 'Jean-Marc', 3, 3);
INSERT INTO `Coureur` (`idCo`, `nomCo`, `prenomCo`, `idCat`, `idCl`) VALUES (4, 'Dupond', 'Thierry', 2, 4);
INSERT INTO `Coureur` (`idCo`, `nomCo`, `prenomCo`, `idCat`, `idCl`) VALUES (5, 'Francois', 'Albert', 4, 2);
INSERT INTO `Lieu`(`idL`, `nomL`) VALUES (4,'Lyon');
INSERT INTO `Evenement` VALUES (5, 'VeloTour Lyon', '2018-01-18',4);
INSERT into `Course` VALUES (5, 6, '08:00:00', 1);
INSERT into `Course` VALUES (5, 7, '09:00:00', 2);
INSERT into `Course` VALUES (5, 8, '10:00:00', 3);
INSERT into `Course` VALUES (5, 9, '10:30:00', 4);
INSERT INTO `Lieu`(`idL`, `nomL`) VALUES (5,'Bordeaux');
INSERT INTO `Evenement` VALUES (6, 'VeloTour Bordeaux', '2018-01-25',5);
INSERT into `Course` VALUES (6, 10, '08:00:00', 1);
INSERT into `Course` VALUES (6, 11, '09:00:00', 2);
INSERT into `Course` VALUES (6, 12, '10:00:00', 3);
INSERT into `Course` VALUES (6, 13, '10:30:00', 4);
INSERT INTO `Lieu`(`idL`, `nomL`) VALUES (6,'Toulouse');
INSERT INTO `Evenement` VALUES (7, 'VeloTour Toulouse', '2018-01-11',6);
INSERT into `Course` VALUES (7, 14, '08:00:00', 1);
INSERT into `Course` VALUES (7, 15, '09:00:00', 2);
INSERT into `Course` VALUES (7, 16, '10:00:00', 3);
INSERT into `Course` VALUES (7, 17, '10:30:00', 4);
INSERT INTO `Lieu`(`idL`, `nomL`) VALUES (7,'Agen');
INSERT INTO `Evenement` VALUES (8, 'VeloTour Agen', '2018-01-04',7);
INSERT into `Course` VALUES (8, 18, '08:00:00', 1);
INSERT into `Course` VALUES (8, 19, '09:00:00', 2);
INSERT into `Course` VALUES (8, 20, '10:00:00', 3);
INSERT into `Course` VALUES (8, 21, '10:30:00', 4);
INSERT INTO `Evenement` VALUES (9, 'VeloTour Orleans', '2018-01-31',1);
INSERT into `Course` VALUES (9, 22, '08:00:00', 1);
INSERT into `Course` VALUES (9, 23, '09:00:00', 2);
INSERT into `Course` VALUES (9, 24, '10:00:00', 3);
INSERT into `Course` VALUES (9, 26, '10:30:00', 4);
INSERT INTO `Evenement` VALUES (10, 'VeloTour Tours', '2018-02-06',3);
INSERT into `Course` VALUES (10, 27, '08:00:00', 1);
INSERT into `Course` VALUES (10, 28, '09:00:00', 2);
INSERT into `Course` VALUES (10, 29, '10:00:00', 3);
INSERT into `Course` VALUES (10, 30, '10:30:00', 4);
INSERT INTO `Effectuer` VALUES (1,7,14, '00:09:59');
INSERT INTO `Effectuer` VALUES (2,7,15, '00:08:56');
INSERT INTO `Effectuer` VALUES (3,7,16, '00:08:49');
INSERT INTO `Effectuer` VALUES (5,7,17, '00:18:59');
INSERT INTO `Effectuer` VALUES (1,9,22, '00:14:30');
INSERT INTO `Effectuer` VALUES (2,9,23, '00:11:27');
INSERT INTO `Effectuer` VALUES (3,9,24, '00:17:04');
INSERT INTO `Effectuer` VALUES (5,9,26, '00:10:45');
INSERT INTO `Effectuer` VALUES (1,10,27, '00:07:54');
INSERT INTO `Effectuer` VALUES (2,10,28, '00:08:29');
INSERT INTO `Effectuer` VALUES (3,10,29, '00:18:59');
INSERT INTO `Effectuer` VALUES (5,10,30, '00:18:09');
INSERT INTO `Effectuer` VALUES (4,6,11, '00:12:59');
INSERT INTO `Effectuer` VALUES (4,8,19, '00:04:59');
INSERT INTO `Effectuer` VALUES (2,1,1, '00:07:59');
INSERT INTO `Effectuer` VALUES (1,2,2, '00:03:59');

