-- Devoir 220
-- Nom: BAZIRE , Prenom: Fabrice

-- Devoir sur machine 1
-- durée 1 heure
-- On rappelle que la fonction YEAR(date) retourne l'année d'une date
-- 
-- Veillez à bien répondre aux emplacements indiqués.
-- Seule la première requête est prise en compte.

-- +-----------------------+--
-- * Question 220385 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés du panel France Global 2 qui sont nés en 1978? 

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------+-----------+------------+
-- | numSond | nomSond   | prenomSond |
-- +---------+-----------+------------+
-- | 634     | CUNERET   | Blandine   |
-- | 638     | RONERELE  | Clémence   |
-- | 678     | MANQUIE   | Nolwenn    |
-- | 704     | LALIOT    | Agathe     |
-- | 808     | NEJIS     | Léonie     |
-- | 1033    | CABEL     | Kévin      |
-- | 1185    | BERRAPS   | Dimitri    |
-- | 1195    | DOUPERAUF | Logan      |
-- | 1216    | LIERTE    | Enora      |
-- | 1285    | DUFORD    | Mathieu    |
-- | etc...
-- = Reponse question 220385.
select numSond, nomSond, prenomSond from SONDE natural join CONSTITUER natural join PANEL where nomPan = "France Global 2" and YEAR(datenaissond) = 1978;



-- +-----------------------+--
-- * Question 220408 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quelles sont les catégories qui ne comportent aucun sondé se prénommant Simon

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+-------------------------------------------------+
-- | idCat | intituleCat                                     |
-- +-------+-------------------------------------------------+
-- | 1     | Agriculteurs exploitants                        |
-- | 2     | Artisans, commerçants, chefs d'entreprise       |
-- | 3     | Cadres, professions intellectuelles supérieures |
-- | 6     | Ouvriers                                        |
-- | 7     | Inactifs ayant déjà travaillé                   |
-- | 8     | Autres sans activité professionnelle            |
-- +-------+-------------------------------------------------+
-- = Reponse question 220408.
select distinct idcat, intituleCat from CATEGORIE natural join CARACTERISTIQUE natural join SONDE where prenomSond in (select prenomSond from SONDE where prenomSond = "Simon");


-- +-----------------------+--
-- * Question 220420 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quel est le nombre de femmes par tranche d'âge?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------+----------+--------+----------+
-- | idTR | valDebut | valFin | nbFemmes |
-- +------+----------+--------+----------+
-- | 1    | 20       | 29     | 94       |
-- | 2    | 30       | 39     | 117      |
-- | 3    | 40       | 49     | 114      |
-- | 4    | 50       | 59     | 115      |
-- | 5    | 60       | 69     | 102      |
-- | 6    | 70       | 120    | 133      |
-- +------+----------+--------+----------+
-- = Reponse question 220420.
select idTR, valDebut, valFin, count(*) nbFemmes from TRANCHE natural join CARACTERISTIQUE natural join SONDE where sexe = 'F' group by idTR;


-- +-----------------------+--
-- * Question 220431 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quelles sont les tranches d'âge qui contiennent plus de 4 personnes prénommées Camille?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------+----------+--------+-----------+
-- | idTR | valDebut | valFin | nbCamille |
-- +------+----------+--------+-----------+
-- | 5    | 60       | 69     | 5         |
-- | 6    | 70       | 120    | 6         |
-- +------+----------+--------+-----------+
-- = Reponse question 220431.
select idTR, valDebut, valFin, count(*) nbCamille from TRANCHE natural join CARACTERISTIQUE natural join SONDE where prenomSond = "Camille" group by idTR having nbCamille>4;


-- +-----------------------+--
-- * Question 220486 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quelles sont les catégories dont tous les sondés nés en 1978 sont des femmes? (on considère que les catégories qui n'ont aucun sondé né en 1978 font partie de la réponse) 

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+-------------------------------------------------+
-- | idcat | intitulecat                                     |
-- +-------+-------------------------------------------------+
-- | 3     | Cadres, professions intellectuelles supérieures |
-- | 7     | Inactifs ayant déjà travaillé                   |
-- | 8     | Autres sans activité professionnelle            |
-- +-------+-------------------------------------------------+
-- = Reponse question 220486.
select distinct idcat, intituleCat from CATEGORIE natural join CARACTERISTIQUE natural join SONDE where sexe = 'F' and YEAR(datenaissond) in (select YEAR(datenaissond) from SONDE where YEAR(datenaissond) = 1978);

