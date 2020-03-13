drop TABLE lesuser;
create TABLE lesuser(
    pseudo varchar(25) not null primary key,
    nom varchar(25) not null,
    mdp varchar(60) not null
)ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;