#include<iostream>
#define Max 5
using namespace std;


int parValeur(int x, char c) {
  ++x;
  c += 1;
  cout<<"fonction parValeur : x "<<x<<" c "<<c<<endl;
  return x + (int) c; 
}


void parReference(int &x, char &c) {
   ++x;
  c += 1;
  cout<<"fonction parReference : x "<<x<<" c "<<c<<endl;

}

int main() {
  int entier(6);
  char caractere('c');
  int z = parValeur(entier, caractere);
  cout<<"Programme principal (parValeur) : z "<<z<<" entier "<<entier<<" caractere "<<caractere<<endl;

  parReference(entier, caractere);
  cout<<"Programme principal (parReference) : entier "<<entier<<" caractere "<<caractere<<endl;
}