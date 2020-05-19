Description textuelle : Créer un nouveau garde de nuit
======================================================

Pré-conditions
--------------
- Les information sur le nouveau garde

Post-conditions
---------------
- Le garde peut communiquer avec un ordithrynque

Scénario nominal
----------------
| Acteur Organisateur | Système vote électronique |
|---------------------|---------------------------|
| 1. ouvrir le formulaire de création ||
|| 2. afficher le formulaire|
| 3.  rentrer les différents champs(nom,prénom et rangs)||
| 4.  appuyer sur valider||
| 5.  faire toucher le museau au garde ||
| 6.  sentir odeur |
|| 7. Enregistrer dans la base |



**A1**: Le garde existe déjà

Le scénario alternatif commence au point 6 du scénario nominal.
| Acteur Organisateur | Système vote électronique |
|---------------------|---------------------------|
||2. Affiche le formulaire de création avec un message d'erreur|
Le scénario nominal reprend au point 3.
