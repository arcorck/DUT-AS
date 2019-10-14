#!/bin/bash
# Auteur :  Fabrice Bazire
echo Quel est le nom de votre fichier ?
read file
if [ -f $file ]
then cat $file
else echo "le fichier n'existe pas"
fi