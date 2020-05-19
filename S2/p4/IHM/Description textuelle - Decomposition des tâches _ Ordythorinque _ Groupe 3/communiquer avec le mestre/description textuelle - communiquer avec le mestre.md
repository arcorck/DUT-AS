Description textuelle : Ajouter une nouvelle espèce
====================================================

Pré-conditions
--------------
- Le garde est identifié

Post-conditions
---------------
- la sympathie du mestre a augmentée

Scénario nominal
----------------
| Acteur Organisateur | Système vote électronique |
|---------------------|---------------------------|
| 1. Demande d'echange |
| 2. Affiche le formulaire |
| 3. Selectionner un item |
| 4. Afficher un prix|
| 5. Cliquer sur accepter |
| 6. Demande de sympathie |
| 7. Afficher les dialogues |
| 8. Selectionner un dialogue |
| 9. Afficher le dialogue |

Scénarios alternatifs
---------------------

**A2**: le mestre ne souhaite pas sympathiser

Le scénario alternatif commence au point 6 du scénario nominal.
| Acteur Organisateur | Système vote électronique |
|---------------------|---------------------------|
|1. Affiche le formulaire avec un message d'erreur |
Le scénario nominal reprend au point 1.
