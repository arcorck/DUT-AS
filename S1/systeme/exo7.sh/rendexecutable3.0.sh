#!/bin/bash
# Auteur :  Fabrice Bazire
if [ -f $1 ]
    then
    if [ -x $1 ]
        then echo "le fichier " $1 " possede deja les droits d'execution"
    else
        chmod u+x $1
    echo "l'affectation des droits d'execution sur le fichier " $1 "a eu lieu avec succes"
    fi
else
    echo "le fichier n'existe pas"
fi