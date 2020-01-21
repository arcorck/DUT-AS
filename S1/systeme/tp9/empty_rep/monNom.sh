#!/bin/bash
# Auteur :  Fabrice Bazire
echo quel est votre nom ?
read nom
echo $nom > monNom.txt
echo verifions le contenu : 
cat monNom.txt