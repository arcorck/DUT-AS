#include<iostream>
using namespace std;
#include"Artiste.hpp"

string Artiste::getNom() const{
	return this->nom;
}


ostream & operator <<(ostream &s, const Artiste &a){
    return a.affiche(s);
}
