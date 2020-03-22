#include<iostream>
using namespace std;

void lire(int t[], int taille) {
  cout<<" saisie des "<<taille<<" éléments du tableau "<<endl;
  for(int i(0); i < taille; ++i) {
    cout<<i+1<<"ème ";
    cin>>t[i]; 
  }
}

void affiche(int t[], int taille) {
  for(int i(0); i < taille; ++i)
    cout<<t[i]<<" ";
  cout<<endl; 
}

void lire2(int * tab, int taille) {
  cout<<" saisie des élements du tableau "<<endl;
  for(int i = 0; i < taille; ++i) {
    cout<<i<<"ème élément : ";
    cin>>tab[i];
  }
}
void affiche2(int * tab, int taille) {
  cout<<"[";
  for(int i = 0; i < taille; ++i)
    cout<<tab[i]<< " ";
  cout<<"] "<<endl;
}

int min(int t[], int taille) {
  int min = t[0];
  for (int i = 0; i < taille; i++){
    if (t[i] < min){
      min = t[i];
    }
  }
  return min;
}

int indice_min(int t[], int taille) {
  int min = t[0];
  int indice = 0;
  for (int i = 0; i < taille; i++){
    if (t[i] < min){
      min = t[i];
      indice = i;
    }
  }
  return indice;
}

void nombre_de_chiffres_et_mult_3 (int n, int & nb_chiffres, bool & mult_3){
  int somme = 0;
  if (n < 10){
    nb_chiffres = 1;
    somme = n;
  }else{
    while (n >= 1){
    nb_chiffres ++;
    somme += n%10;
    n = n/10;
    }
  }
  mult_3 = somme % 3 == 0;
}

void operations_tab(int t[], int taille, int & somme, int & nb_elem_pos, int & nb_elem_neg, int & nb_elem_nul, int & nb_mult_5) {
  for (int i = 0; i < taille; i++){
    somme += t[i];
    if (t[i] % 5 == 0){
      nb_mult_5++;
    }
    if (t[i] > 0){
      nb_elem_pos ++;
    }else{
      if (t[i] < 0){
        nb_elem_neg ++;
      }else{
        nb_elem_nul ++;
      }
    }
  }
}

int main(){
  int tab [6];
  tab [0] = -5;
  tab [1] = 0;
  tab [2] = 5;
  tab [3] = 6;
  tab [4] = -6;
  tab [5] = 8;
  int somme, nb_pos, nb_neg, nb_nul, nb_mult_5 = 0;
  operations_tab(tab, 6, somme, nb_pos, nb_neg, nb_nul, nb_mult_5);
  cout << "somme : " << somme << endl;
  cout << "nombre de positifs : " << nb_pos << endl;
  cout << "nombre de negtaifs : " << nb_neg << endl;
  cout << "nombre de nuls : " << nb_nul << endl;
  cout << "nombre de multiples de 5 : " << nb_mult_5 << endl;
}