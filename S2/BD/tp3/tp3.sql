-- TP 3
-- Nom: Bazire , Prenom: Fabrice

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Combien y a-t-il de personnes dans la table SONDE?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +----------+
-- | nbSondes |
-- +----------+
-- | 1348     |
-- +----------+

-- select count( numsond ) nbSondes from SONDE ;


-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Combien y a-t-il de personnes qui s'appellent Jean?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------+
-- | nbJean |
-- +--------+
-- | 9      |
-- +--------+

-- select count( numsond ) nbJean from SONDE where prenomsond = "Jean";



-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Combien de prénoms différents y a-t-il dans la base de données?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +----------+
-- | nbPrenom |
-- +----------+
-- | 181      |
-- +----------+

-- select count(distinct prenomsond) nbPrenom from SONDE;



-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quel est l'âge de la plus jeune femme du panel France global 2? Pour faire ce calcul on aura besoin de la date du jour retournée  par la fonction CURDATE() et de faire une différence entre deux dates grâce à la fonction DATEDIFF(date1,date2) qui retourne le nombre de jours qui sépare date1 et date2.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------+
-- | minAge |
-- +--------+
-- | 20     |
-- +--------+

-- select min(round(DATEDIFF(CURDATE(), datenaissond)/365)) minAge from  SONDE natural join CONSTITUER natural join PANEL natural join CARACTERISTIQUE where nomPan = "France global 2" and sexe = "F";



-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quel est l'age moyen du panel  Moins de 50 ans?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------+
-- | ageMoyen    |
-- +-------------+
-- | 35.95177670 |
-- +-------------+

-- select avg(DATEDIFF(CURDATE(), datenaissond)/365.25) ageMoyen from  SONDE natural join CONSTITUER natural join PANEL where nomPan = "Moins de 50 ans" ;



-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Donner le nom du sondé le plus jeune de la base de données.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------+------------+
-- | nomSond | prenomSond |
-- +---------+------------+
-- | PENCHE  | Elise      |
-- +---------+------------+

-- select nomsond, prenomsond from SONDE where datenaissond = (select max(datenaissond) from  SONDE);


-- +------------------+--
-- * Question 7 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  On voudrait le nombre de sondés dans chaque panel.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+--------+
-- | nomPan          | nbSond |
-- +-----------------+--------+
-- | France global 1 | 800    |
-- | France global 2 | 800    |
-- | Moins de 50 ans | 665    |
-- +-----------------+--------+

-- select nomPan, count(numsond) nbSond from SONDE natural join CONSTITUER natural join PANEL group by nompan;


-- +------------------+--
-- * Question 8 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  On voudrait l'âge moyen des sondés dans chaque catégorie.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------------------------------+-------------+
-- | intituleCat                    | ageMoy      |
-- +--------------------------------+-------------+
-- | Agriculteurs exploitants       | 39.94500714 |
-- | Artisans, commerçants, chefs d | 41.61595000 |
-- | Autres sans activité professio | 62.49244940 |
-- | Cadres, professions intellectu | 41.94489344 |
-- | Employés                       | 46.25833302 |
-- | etc...




-- +------------------+--
-- * Question 9 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  On veut la même chose mais pour chaque panel.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+--------------------------------+-------------+
-- | nomPan          | intituleCat                    | ageMoy      |
-- +-----------------+--------------------------------+-------------+
-- | France global 1 | Agriculteurs exploitants       | 40.84178750 |
-- | France global 1 | Artisans, commerçants, chefs d | 44.26609375 |
-- | France global 1 | Autres sans activité professio | 61.19708854 |
-- | France global 1 | Cadres, professions intellectu | 41.82176806 |
-- | France global 1 | Employés                       | 45.44019375 |
-- | etc...
-- = Reponse question 9.



-- +-------------------+--
-- * Question 10 :     --
-- +-------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Pour chaque catégorie, on veut le nombre de femmes.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------------------------------+-----+
-- | intituleCat                    | nbF |
-- +--------------------------------+-----+
-- | Agriculteurs exploitants       | 6   |
-- | Artisans, commerçants, chefs d | 23  |
-- | Autres sans activité professio | 96  |
-- | Cadres, professions intellectu | 60  |
-- | Employés                       | 108 |
-- | etc...
-- = Reponse question 10.



-- +-------------------+--
-- * Question 11 :     --
-- +-------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--   Donner la liste des prénoms portés par plus de 20 sondés.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+--------+
-- | prenomSond | nbPers |
-- +------------+--------+
-- | Camille    | 22     |
-- | Claire     | 24     |
-- | Lucie      | 20     |
-- | Mathieu    | 20     |
-- | Mathilde   | 25     |
-- | etc...
-- = Reponse question 11.



-- +-------------------+--
-- * Question 12 :     --
-- +-------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Pourquoi certaines catégories ont disparu? A-t-on une chance de trouver un nombre de personnes à 0?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------------------------------+--------+
-- | intituleCat                    | nbPers |
-- +--------------------------------+--------+
-- | Autres sans activité professio | 1      |
-- | Cadres, professions intellectu | 1      |
-- | Employés                       | 3      |
-- | Inactifs ayant déjà travaillé  | 1      |
-- +--------------------------------+--------+
-- = Reponse question 12.


