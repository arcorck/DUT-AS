#!/bin/rm
# Auteur :  Fabrice Bazire
mkdir exercice3
cd exercice3
touch fic4
mkdir rep1; cd rep1
touch fic1
chmod 000 fic1
touch fic2
chmod 400 fic2
touch fic3
chmod 600 fic3
ls -l
cd ..
mkdir rep2; cd rep2
touch fic1
chmod 000 fic1
touch fic2
chmod 400 fic2
touch fic3
chmod 600 fic3
ls -l
cd ..
mkdir rep3; cd rep3
touch fic1
chmod 000 fic1
touch fic2
chmod 400 fic2
touch fic3
chmod 600 fic3
ls -l
cd ..
mkdir rep4; cd rep4
touch fic1
chmod 000 fic1
touch fic2
chmod 400 fic2
touch fic3
chmod 600 fic3
ls -l
cd ..
chmod 500 rep1
chmod 700 rep2
chmod 600 rep3
chmod 100 rep4
chmod 400 fic4
ls -l