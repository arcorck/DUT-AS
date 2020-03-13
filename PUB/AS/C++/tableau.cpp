#include<iostream>
using namespace std;

void affiche( int t[], int taille){
    for(int i = 0; i<taille; ++i){
        cout << t[i] << " ";
    }
    cout << endl;  
}
  
void initAlea(int t[], int taille){
    // initialise de tableau t de dimension 
    // taille avec des valeurs aléatoires
    for(int i=0; i<taille; ++i){
        t[i]=random()%100;
    }
}

bool appartient(int t[], int taille, int x){
    // retourne true si x est contenu dans t false sinon
    
    return false;
}

int laPositionDuPremier(int t[], int taille, int x){
    // retourne l'indice du premier x dans le tableau t,
    // retourne -1 si x n'est pas dans t
    
    return -1;
}


int main(){
    const int dim=20;
    srand(time(0));
    int tab[dim];
    initAlea(tab, dim);
    affiche(tab,dim);
    
    return 0;
}
    
