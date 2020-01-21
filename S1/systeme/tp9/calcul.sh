#!/bin/bash
# Auteur :  Fabrice Bazire
echo premier nombre : 
read n1
echo deuxieme nombre : 
read n2
if [ $1 == '+' ]
    then echo le resultat de $n1+$n2 est $(($n1+$n2))
else 
    if [ $1 == '-' ]
        then echo le resultat de $n1-$n2 est $(($n1-$n2))
    else
        if [ $1 == '/' ]
            then echo le resultat de $n1/$n2 est $(($n1/$n2))
        else 
            if [ $1 == 'x' ]
                then echo le resultat de $n1'x'$n2 est $(($n1*$n2))
            else 
                echo "erreur"
            fi
        fi
    fi
fi