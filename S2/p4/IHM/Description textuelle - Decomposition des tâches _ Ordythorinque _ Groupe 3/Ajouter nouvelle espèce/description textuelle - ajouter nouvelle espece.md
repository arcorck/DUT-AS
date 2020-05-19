Description textuelle : Ajouter une nouvelle espèce
====================================================

Pré-conditions
--------------
- L'intendant est identifié

Post-conditions
---------------
- L'espèce est en attente d'ajout, le patrouilleur doit remplir les champs manquants si nécessaire

Scénario nominal
----------------
| Acteur Organisateur | Système vote électronique |
|---------------------|---------------------------|
| 1. Demande d'ajout d'une espèce |
| 2. Affiche le formulaire |
| 3. Saisie du nom de l'espèce |
| 4. Saisie de la description de l'espèce |
| 5. Saisie du niveau de danger de l'espèce |
| 6. Possible ajout d'un champ |
| 7. Cliquer sur Suivant |
| 8. Affichage du formulaire rempli |
| 9. Cliquer sur Soumettre aux patrouilleurs |
| 10. Enregistre le formulaire |

Scénarios alternatifs
---------------------

**A2**: L'espèce existe déjà

Le scénario alternatif commence au point 7 du scénario nominal.
| Acteur Organisateur | Système vote électronique |
|---------------------|---------------------------|
|2. Affiche le formulaire avec un message d'erreur |
Le scénario nominal reprend au point 3.
