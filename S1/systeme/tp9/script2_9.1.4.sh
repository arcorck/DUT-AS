#!/bin/bash
# Auteur :  Fabrice Bazire
if [ -f $1 ]
    then touch $1-2.txt
    cat $1 | tr a-z A-Z > $1-2.txt
else echo "erreur $1 n'est pas un fichier existant"
fi