-- TP 1
-- Bazire Fabrice

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les panels dont ne fait pas partie Louane DJARA?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- | Moins de 50 ans |
-- +-----------------+

-- select nompan from PANEL where nompan not in (select nompan from PANEL natural join CONSTITUER natural join SONDE where nomsond = "DJARA" and prenomsond = "Louane");

-- select nompan from PANEL p1 where not exists (select * from PANEL p2 natural join CONSTITUER natural join SONDE where nomsond = "DJARA" and prenomsond = "Louane" and p1.nompan = p2.nompan);

-- select nompan from PANEL where nompan != ALL  (select nompan from PANEL natural join CONSTITUER natural join SONDE where nomsond = "DJARA" and prenomsond = "Louane");



-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les prénoms de sondé commençant par un A qui n'apparaissent pas dans la tranche d'age 20-29 ans? Classez ces noms par ordre alphabétique.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+
-- | prenomSond |
-- +------------+
-- | Alice      |
-- | Allan      |
-- | Amaury     |
-- | Ambre      |
-- | Anaïs      |
-- | etc...

-- select distinct prenomSond from SONDE where prenomsond LIKE 'a%' and prenomsond in (select prenomsond from SONDE natural join CARACTERISTIQUE natural join TRANCHE where valdebut < 20 and valfin > 29) ORDER BY prenomsond;

select prenomsond from SONDE s, CARACTERISTIQUE c, TRANCHE t where t.valdebut < 20 and t.valfin > 29 and s.idc = c.idc and c.idtr = t.idtr;




-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--   Quels sont les panels dont tous les sondés ont moins de 60 ans? Rappel: CURDATE() donne la date du jour et DATEDIFF(d1,d2) donne le nombre de jours entre d1 et d2.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | Moins de 50 ans |
-- +-----------------+
-- = Reponse question 3.



-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quelles sont les catégories qui comportent des personnes nées en 1974? On rappelle que YEAR(d) donne l'année de la date d sous la forme d'un entier.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------------------------------+
-- | intituleCat                    |
-- +--------------------------------+
-- | Cadres, professions intellectu |
-- | Professions intermédiaires     |
-- | Employés                       |
-- | Ouvriers                       |
-- | Inactifs ayant déjà travaillé  |
-- +--------------------------------+
-- = Reponse question 4.



-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--   Quels sont les sondés nés en 1997 qui appartiennent aux panels France global 1 et France global 2?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------+------------+
-- | nomSond   | prenomSond |
-- +-----------+------------+
-- | DOILELTIS | Nina       |
-- +-----------+------------+
-- = Reponse question 5.



-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés nés en 1974 qui ont la même date de naissance?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------+------------+----------+------------+
-- | nomSond | prenomSond | nomSond  | prenomSond |
-- +---------+------------+----------+------------+
-- | DASA    | Maxime     | PEKARDAC | Bilal      |
-- +---------+------------+----------+------------+
-- = Reponse question 6.


