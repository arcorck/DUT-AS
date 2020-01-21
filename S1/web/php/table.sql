        DROP TABLE CARNET;

        CREATE TABLE CARNET(
          ID int(11) NOT NULL AUTO_INCREMENT,
          NOM varchar(30) DEFAULT NULL,
          PRENOM varchar(30) DEFAULT NULL,
          NAISSANCE date DEFAULT NULL,
          VILLE varchar(30) DEFAULT NULL,
          PRIMARY KEY (ID)
        ) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

        INSERT INTO CARNET VALUES 
        (1,'SMITH','JOHN','1980-12-17','ORLEANS'),
        (2,'DURAND','JEAN','1983-01-13','ORLEANS'),
        (3,'GUDULE','JEANNE','1967-11-06','TOURS'),
        (4,'ZAPATA','EMILIO','1956-12-01','ORLEANS'),
        (5,'JOURDAIN','NICOLAS','2000-09-10','TOURS'),
        (6,'DUPUY','MARIE','1986-01-11','BLOIS'),
        (7,'ANDREAS','LOU','1861-02-12','ST Petersbourg'),
        (9,'Kafka','Franz','1883-07-03','Prague'),
        (11,'Dalton','Joe','2003-12-06','Dallas');