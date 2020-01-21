#!/bin/bash
# Auteur :  Fabrice Bazire
if [ -d $1 ]
    then
    echo Quel est le nom de votre fichier ?
    read file
    if [ -f $file ]
        then cat $file
    else echo "le fichier n'existe pas"
    fi
else echo le repertoire est inexistant
fi