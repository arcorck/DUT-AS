#!/bin/rm
# Auteur :  Fabrice Bazire
mkdir algorithmique_m1102
mkdir algorithmique_m1102/TD18
mkdir algorithmique_m1102/TD24
mkdir algorithmique_m1102/TD42
mkdir "bases_de_l'informatique_M1101"
mkdir "bases_de_l'informatique_M1101"/TP1
mkdir "bases_de_l'informatique_M1101"/TP2
mkdir DocumentsNumériques_M1105
mkdir DocumentsNumériques_M1105/TP1
mkdir DocumentsNumériques_M1105/TP2
mkdir ExpressionCommunication
mkdir FoncOrganisations_m1204
touch fichiervide.txt
mv fichiervide.txt algorithmique_m1102/TD42
mv DocumentsNumériques_M1105/TP1 "TP1_LibreOfficeWriter"; mv TP1_LibreOfficeWriter DocumentsNumériques_M1105
rm -r algorithmique_m1102/*
cp /pub/1A/ASR-M1101/tp1-commandes-de-base.pdf "bases_de_l'informatique_M1101"/TP1_LibreOfficeWriter
cp /pub/1A/DocNum/TP1/* DocumentsNumériques_M1105/TP1