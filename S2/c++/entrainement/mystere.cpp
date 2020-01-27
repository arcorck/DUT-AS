#include <iostream>
using namespace std;
#include <string> 
#include <stdio.h>
#include <stdlib.h>
#include <time.h> //Ne pas oublier d'inclure le fichier time.h

string melangerLettres(string mot)
{
    string melange ;
 
    //Tant qu'on n'a pas extrait toutes les lettres du mot
    while (mot.size() != 0)
    {
        // On choisit un numéro de lettre au hasard dans le mot
        int const position = rand() % mot.size();
 
        // On ajoute la lettre dans le mot mélangé
        melange += mot.at(position);
 
        // On retire cette lettre du mot mystère
        // Pour ne pas la prendre une deuxième fois
        mot.erase(position, 1);
    }
 
    //On renvoie le mot mélangé
    return melange;
}

void jeu (string mot, string melange, int essais){
    string essai;
    int i = 0;
    while (essai != mot and i < essais){
        cout << "Pour rappel le mot à trouver est : " << melange << endl;
        cout << "A vous : ";
        cin >> essai;
        i++;
    }
    if (essai == mot){
        cout << "Vous avez réussi" << endl;
    }else{
        cout << "Vous avez échoué" << endl;
    }
}

int main (){
    cout << "Joueur 1 : entrez un mot : " ;
    string mot;
    cin >> mot;
    cout << "Combien voulez vous laisser de chance au joueur 2 pour trouver le mot : " << endl;
    int essais;
    cin >> essais;
    string melange;
    melange = melangerLettres(mot);
    cout << "Joueur 2 : le mot mélangé est : " << melange << endl;
    jeu (mot, melange, essais);
    return 0;
}