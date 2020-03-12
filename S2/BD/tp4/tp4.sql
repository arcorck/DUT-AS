-- EXERCICE 1

-- 1) 
create or replace  view Produit10 (ref, nom, prix)
AS SELECT refProd, nomProd, PUProd from PRODUIT where PUProd > 10;

-- select * from Produit10;


-- 2)
create or replace  view DixMars2015 (ref, nom, prix)
As select refProd, nomProd, PUProd from PRODUIT natural join DETAIL natural join FACTURE where 
YEAR(dateFac) = 2015 and Month(dateFac) = 03 and Day(dateFac) = 10;

-- select * from DixMars2015;


-- 3)
create or replace  view NbClientsParVille (Ville, nombreDeClients)
AS SELECT adresseCli, count(*) from CLIENT group by adresseCli;

-- select * from NbClientsParVille;


-- 4)
create or replace  view CAParMois (mois, annee, CA)
as select Month(dateFac), Year(dateFac), SUM(qte*PUProd) 
from FACTURE natural join DETAIL natural Join PRODUIT 
group by Month(dateFac), Year(dateFac); 

-- select * from CAParMois;


-- 5)
drop view Produit10;
drop view DixMars2015;
drop view NbClientsParVille;
drop view CAParMois;






-- EXERCICE 2

-- 1)
prepare ProduitSup from 'select * from PRODUIT where PUProd > ?';
set @prix := 10; 
execute ProduitSup using @prix;


-- 2)
prepare numFacture from 'select  refProd, nomProd, PUprod, qte from FACTURE Natural join DETAIL natural join PRODUIT where  '