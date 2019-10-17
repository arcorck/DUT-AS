#!/bin/bash
# Auteur :  Fabrice Bazire
if [ -f $1 ]
then cat $1
else echo "le fichier n'existe pas"
fi