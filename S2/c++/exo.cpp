//ecrire une fonction qui retourne le plus grand entier d'un tableau d'entier
//ecrire une fonction qui retourne la premiere position du plus grand entier d'un tableau d'entiers
//ecrire une fonction qui retourne le max et l'indice du max d'un tableau d'entiers

#include <iostream>
using namespace std;

int max_tab(int tab [], int taille){
    int max = tab[0];
    for (int i = 1; i < taille; i++){
        if (tab[i] > max){
            max = tab[i];
        }
    }
    return max;
}

int indice_max_tab(int tab [], int taille){
    int max = tab[0];
    int indice = 0;
    for (int i = 1; i < taille; i++){
        if (tab[i] > max){
            max = tab[i];
            indice = i;
        }
    }
    return indice;
}

void maxEtIndiceMax (int tab [], int taille, int & max, int & indice_max){
    max = tab[0];
    indice_max = 0;
    for (int i = 1; i < taille; i++){
        if (tab[i] > max){
            max = tab[i];
            indice_max = i;
        }
    }
}

void aff_tab(int tab [], int taille){
    cout << "| ";
    for (int i = 0; i < taille; i++){
        cout << to_string(tab[i]) << " | "; 
    }
}

int main (){
    int tab [10];
    int max = 0, ind_max = 0; 
    for (int i = 0; i < 10; i++){
        tab[i] = 20 - 2*(i+5);
    }
    maxEtIndiceMax (tab, 20, max, ind_max);
    aff_tab(tab,10);
    cout << "\nmax : " << max_tab(tab, 10) << endl;
    cout << "indice max : " << indice_max_tab(tab, 10) << endl;
    cout << "\nmax 2 : " << max << endl;
    cout << "indice max 2 : " << ind_max << endl;
    return 0;
}