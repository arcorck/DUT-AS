-- TP 1
-- Bazire Fabrice 

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Donner la liste des panels dont fait partie Caroline BOURIER.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- +-----------------+
-- select nompan from SONDE natural join CONSTITUER natural join PANEL where nomsond = 'BOURIER' and prenomsond = 'Caroline';

-- select nompan from SONDE natural join CONSTITUER natural join PANEL where nomsond in (
--    select nomsond from SONDE where nomsond = 'BOURIER'
-- ) and prenomsond in (
--    select prenomsond from SONDE where prenomsond = 'Caroline'
-- );

-- select nompan from PANEL p where exists (
--    select * from CONSTITUER c where p.idpan=c.idpan and exists(
--        select * from SONDE s where nomsond = 'BOURIER' and prenomsond = 'Caroline' and s.numsond=c.numsond
--    )
-- );


-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les panels dont un des sondés est de la tranche d'âge 70 à 120 ans?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- | France global 2 |
-- +-----------------+
-- select distinct nompan from SONDE natural join CONSTITUER natural join PANEL where year(now())-year(datenaissond) > 70 and year(now())-year(datenaissond) < 120;

-- IN

-- select nompan from PANEL p where exists (
--     select * from CONSTITUER c natural join SONDE natural join CARACTERISTIQUE natural join TRANCHE where valDebut>=70 and p.idpan = c.idpan
-- );

-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés de la tranche d'age 70-120 ans qui sont ouvriers?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------+------------+
-- | nomSond   | prenomSond |
-- +-----------+------------+
-- | ERYS      | Imane      |
-- | BERRGAIES | Claire     |
-- | JABAT     | Rose       |
-- | WALLOCHE  | Marion     |
-- | LENUJA    | Pauline    |
-- | etc...

-- select nomsond, prenomsond from SONDE natural join CARACTERISTIQUE natural join CATEGORIE where year(now())-year(datenaissond) > 70 and year(now())-year(datenaissond) < 120 and intitulecat = 'Ouvriers';



-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les ouvriers qui portent le prénom Olivier?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------+------------+
-- | nomSond   | prenomSond |
-- +-----------+------------+
-- | THALOUERD | Olivier    |
-- | POTRININ  | Olivier    |
-- +-----------+------------+

 select nomsond, prenomsond from SONDE natural join CARACTERISTIQUE natural join CATEGORIE where prenomsond = 'Olivier' and intitulecat = 'Ouvriers';



-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les tranches d'âge qui comportent une ou plusieurs femmes nées un 25 avril?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +----------+--------+
-- | valDebut | valFin |
-- +----------+--------+
-- | 40       | 49     |
-- +----------+--------+
-- = Reponse question 5.



-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés prénommés Jean qui appartiennent à au moins 2 panels différents? 

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+----------+
-- | prenomSond | nomSond  |
-- +------------+----------+
-- | Jean       | DILY     |
-- | Jean       | JATECHU  |
-- | Jean       | PIETIENE |
-- | Jean       | FAL      |
-- | Jean       | BOYEGHE  |
-- +------------+----------+
-- = Reponse question 6.


