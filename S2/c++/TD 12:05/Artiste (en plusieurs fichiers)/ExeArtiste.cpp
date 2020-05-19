#include<iostream>
using namespace std;
#include"Artiste.hpp"
#include"Chanteur.hpp"
#include"Acteur.hpp"

int main() {
  Artiste * lesArtistes[2];
  lesArtistes[0] = new Chanteur("Arthur", "Jazz"); 
  lesArtistes[1] = new Acteur("Ray","France",1970); 
  for(int i = 0; i < 2; ++i) {
    cout<<*lesArtistes[i]<<" ";
    cout<<endl; 
    lesArtistes[i] -> quelArtC();
    cout<<endl<<endl; 
  }
  for(int i = 0; i < 2; ++i) {
    delete lesArtistes[i];
    cout<<endl;
  }
}
