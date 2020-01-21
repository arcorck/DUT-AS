#!/bin/bash
# Auteur :  Fabrice Bazire
echo "L'argument est $1"
if [ -f $1 ]
    then
    if [ -w $1 ] 
        then rm $1
        echo "le fichier " $1 " a ete supprimé"
    else 
        echo "le fichier " $1 " n'a pas ete supprimé car vous n'avez pas le droit de le faire"
    fi
else 
    echo $1 " n'a pas ete supprimé car ce n'est pas un fichier existant"
fi