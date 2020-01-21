#!/bin/bash
# Auteur :  Fabrice Bazire
if [ -d $2 ]
    then echo Le nombre de fichiers avec une extension en .$1 dans le repertoire $2 est : 
    ls $2/*.$1 | wc -w
else echo dossier inexistant
fi