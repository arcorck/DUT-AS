#!/bin/bash
# Auteur :  Fabrice Bazire
if [ -f $1 ]
    then echo ecrivez une ligne
    read ligne
    echo $ligne | tr a "@" | tr e 3 > $1
else echo "erreur $1 n'est pas un fichier existant"
fi