---------------------
-- Exercice 1
---------------------

\! echo "Exercice 1"

-- requete 1

\! echo "requete 1"

create or replace view Produit10 as 
    select * 
    from PRODUIT 
    where PUProd>=10;
select * from  Produit10;
-- requete 2

\! echo "requete 2"

create or replace view DixMars2015 as 
    select distinct refProd, nomProd, puProd
    from PRODUIT natural join DETAIL natural join FACTURE 
    where dateFac=STR_TO_DATE('10/03/2015','%d/%m/%Y');
select * from DixMars2015;
-- requete 3

\! echo "requete 3"

create or replace view nbClientsParVille(ville,nbCli) as 
    select adresseCli, count(numCli) 
    from CLIENT 
    group by adresseCli;
select * from  nbClientsParVille where ville like 'M%';
-- requete 4

\! echo "requete 4"

create or replace view CAParMois(mois,annee,CA) as 
    select month(dateFac), year(dateFac), sum(qte*PUProd) 
    from FACTURE natural join DETAIL natural join PRODUIT 
    group by month(dateFac), year(dateFac) 
    order by year(dateFac), month(dateFac);
select * from CAParMois where annee=2015;
-- requete 5

\! echo "requete 5"

drop view CAParMois;
drop view DixMars2015;
drop view Produit10;
drop view nbClientsParVille;
---------------------
-- Exercice 2
---------------------

\! echo "Exercice 2"

-- requete 1

\! echo "requete 1"

       prepare supPrix from 'select * from PRODUIT where puProd>=?';
-- requete 2

\! echo "requete 2"

      set @prix:=10;
      execute supPrix using @prix;
-- requete 3

\! echo "requete 3"

       prepare detFac from 'select refProd, nomProd,PUprod,qte from
       PRODUIT natural join DETAIL where numFac=?';
-- requete 4

\! echo "requete 4"

       set @num:=221;
       execute detFac using @num;
---------------------
-- Exercice 3
---------------------

\! echo "Exercice 3"

-- requete 1

\! echo "requete 1"

select distinct nomProd 
from PRODUIT natural left outer join DETAIL 
where numFac is NULL;
-- requete 2

\! echo "requete 2"

select distinct nomProd, count(numFac) nbFac 
from PRODUIT natural left outer join DETAIL 
where nomProd like 'M%' 
group by nomProd;
-- requete 3

\! echo "requete 3"

select distinct nomProd, sum(IFNULL(qte,0)) qteTotale 
from PRODUIT natural left outer join DETAIL 
where nomProd like 'M%' group by nomProd;
---------------------
-- Exercice 4
---------------------

\! echo "Exercice 4"

-- requete 1

\! echo "requete 1"

create or replace view Annee(annee) as 
    select distinct YEAR(dateFac) from FACTURE order by YEAR(dateFac);
create or replace view ClientAnnee (numCli, nomCli, prenomCli, annee) as 
    select numCli, nomCli, prenomCli, annee
    from CLIENT, Annee;
create or replace view CAParClientParAn(numCli, annee, CA) as
    select numCli, YEAR(dateFac), sum(qte*PUProd) 
    from  FACTURE natural join DETAIL natural join PRODUIT 
    group by numCli, YEAR(dateFac);
create or replace view CAParClientParAnAvec0 (numCli, nomCli, prenomCli, annee, CA) as
    select numCli, nomCli, prenomCli, annee, IFNULL(CA,0)
    from ClientAnnee natural left outer join CAParClientParAn;
select * from CAParClientParAnAvec0 where nomCli='ZET' and prenomCli='Mathieu';
-- requete 2

\! echo "requete 2"

create or replace view Annee(annee) as 
    select distinct YEAR(dateFac) from FACTURE order by YEAR(dateFac);
create or replace view ProduitAnnee (refProd, nomProd, PUProd, annee) as 
    select refProd, nomProd, PUProd, annee
    from PRODUIT, Annee;
create or replace view CAParProduitParAn(refProd, annee, CA) as
    select refProd, YEAR(dateFac), sum(qte*PUProd) 
    from  FACTURE natural join DETAIL natural join PRODUIT 
    group by refProd, YEAR(dateFac);
create or replace view CAParProduitParAnAvec0 (refProd, nomProd, annee, CA) as
    select refProd, nomProd, annee, IFNULL(CA,0)
    from ProduitAnnee natural left outer join CAParProduitParAn order by refProd, annee;
select * from CAParProduitParAnAvec0 where nomProd like 'T%';
