#include <iostream>
using namespace std;

int minimum(int tab[], int taille){
    int min = tab[0];
    for (int i = 0; i < taille; i++){
        if (tab[i] < min){
            min = tab[i];
        }
    } 
    return min;
}

int nb_occ(int tab[], int taille, int occ){
    int nb = 0;
    for (int i = 0; i < taille; i++){
        if (tab[i] == occ){
            nb++;
        }
    }
    return nb;
}

bool app(int tab[], int taille, int elem){
    for (int i = 0; i < taille; i++){
        if (tab[i] == elem){
            return true;
        }
    }
    return false;
}

int app_indice(int tab[], int taille, int elem){
    for (int i = 0; i < taille; i++){
        if (tab[i] == elem){
            return i;
        }
    }
    return -1;
}

int app_dicho(int tab[], int taille, int elem, int pos, int deb, int fin){
    
}

int main(){
    int tab [10];
    for (int i = 0; i < 10; i++){
        tab[i] = i+1;
    }
    tab[9] = 5;
    cout << "min du tab : " << minimum(tab, 10) << endl;
    cout << "nombre d'occurence de 5 : " << nb_occ(tab, 10, 5) << endl;
    cout << "5 appartient au tableau : " << app(tab, 10, 5) << endl;
    cout << "15 appartient au tableau : " << app(tab, 10, 15) << endl;
    cout << "5 appartient au tableau : " << app_indice(tab, 10, 5) << endl;
    cout << "15 appartient au tableau : " << app_indice(tab, 10, 15) << endl;
    cout << "5 appartient au tableau : " << app_dicho(tab, 10, 5, 0, 0, 9) << endl;
    cout << "15 appartient au tableau : " << app_dicho(tab, 10, 15, 0, 0, 9) << endl;
    return 0;
}