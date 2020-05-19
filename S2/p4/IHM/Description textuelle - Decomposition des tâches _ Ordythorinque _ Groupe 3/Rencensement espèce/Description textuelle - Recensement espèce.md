Description textuelle : Recenser une espèce
==========================================

Pré-conditions
--------------
- Le patrouilleur est identifié

Post-conditions
---------------
- L'espèce est recensée

Scénario nominal
----------------
| Acteur Patrouilleur | Système Ordythorinque |
|---------------------|---------------------------|
| 1. Demande de de rencensement d'une espèce ||
|| 2. Affiche le formulaire de recensement |
| 3. Saisir le nom de l'espèce à recenser ||
| 4. Saisir le niveau de danger de l'espèce ||
| 5. Saisir si l'espèce vit en groupe ou individuellement ||
| 6. Clique sur suivant ||
| 7. Affiche le formulaire de recensement complet |
| 8. Clique sur suivant après relecture pour confirmer l'enregistrement de l'espèce||
|| 9. Enregistre le recensement de l'espèce |

Scénarios alternatifs
---------------------
**A1**: L'espèce a déjâ été recensée cette année

Le scénario alternatif commence au point 7 du scénario nominal.
| Acteur Patrouilleur | Système Ordythorinque |
|---------------------|---------------------------|
||2. Affiche le formulaire de recensement avec un message d'erreur|
Le scénario nominal reprend au point 2.
