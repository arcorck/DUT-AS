#include <iostream>
using namespace std;
#include <math.h> 

int moyenne(){
    cout << "Combien voulez vous entrer de notes ? " << endl;

    int nbnotes(0); //On prepare une case mémoire pour stocker un entier

    cin >> nbnotes; //On fait entrer un nombre dans cette case

    while (nbnotes < 0) {
        cout << "ERREUR : Combien voulez vous entrer de notes ? " << endl;
        cin >> nbnotes;
    }

    int note(0);

    int lesnotes(0);

    for (int compteur(0) ; compteur < nbnotes ; compteur++)
    {
        cout << "Entrer une note : " << endl;
        cin >> note;
        while (note < 0 || note > 20) {
            cout << "La note doit être compris entre 0 et 20, entrer une autre note : " << endl;
            cin >> note;
        }
        lesnotes += note;
    }

    cout << "La moyenne est de : ";
    return lesnotes/nbnotes;
}


int main () {

    cout << moyenne() << endl;    
    
    return 0;
}