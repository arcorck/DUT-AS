#!/bin/bash
# Auteur :  Fabrice Bazire
echo quel est votre nom ?
read nom
heure=$(date +%H:%M)
echo "Je m'appelle $nom il est $heure heures"