-- Requetes non imbriquées


-- evenement ayant eu lieu a orleans (ordre chronologique)
select nomEv, dateEv, nomL from Evenement Natural join Lieu where nomL = 'Orleans' order by dateEv;

-- liste des coureurs de l'USO ayant couru les foulées roses en sénior (dans l'ordre d'arrivée)
select nomCo, prenomCo, temps
from Coureur natural join Club natural join Effectuer nautral join Course natural join Evenement
where sigleCl = 'USO' and nomEv = "Les Foulees Roses" order by temps;

-- liste des courses auxquelles l'uso a participe
select nomEv, dateEv 
from Evenement natural join Effectuer natural join Coureur natural join Club
where sigleCl = 'USO';

-- liste des coureurs ayant participé à une course junior
select distinct prenomCo, nomCo 
from Categorie natural join Coureur natural join Effectuer
where nomCat = "junior";



-- Requetes imbriquées


-- evenement ayant eu lieu a orleans (ordre chronologique)
select nomEv, dateEv, nomL from Evenement Natural join Lieu where idEv in 
(select idEv from Evenement Natural join Lieu where nomL = 'Orleans')
order by dateEv;

-- liste des coureurs de l'USO ayant couru les foulées roses en sénior (dans l'ordre d'arrivée)
select nomCo, prenomCo, temps
from Coureur natural join Club natural join Effectuer natural join Course natural join Evenement
where sigleCl = 'USO' and idEv in (
     select idEv
     from Effectuer natural join Evenement
     where nomEv = 'Les Foulees Roses'
) order by temps;

-- liste des courses auxquelles l'uso a participe
select nomEv, dateEv 
from Evenement 
where idEv in (
    select idEv 
    from Effectuer natural join Coureur natural join Club
    where sigleCl = "USO"
);

-- liste des coureurs ayant participé à une course junior
select distinct prenomCo, nomCo 
from Coureur 
where idCo in (
    select distinct idCo
    from Categorie natural join Coureur natural join Effectuer
    where nomCat = "junior"
);



-- liste des coureurs qui ont participé aux foulees roses et a la corrida d'olivet
select prenomCo, nomCo
from Coureur natural join Effectuer natural join Evenement
where nomEv = 'La Corrida'
and idCo in (
select idCo
from Coureur natural join Effectuer natural join Evenement
where nomEv = 'Les Foulees Roses');