#ifndef ARTISTEHPP
#define ARTISTEHPP

#include<iostream>
using namespace std;
#include"Art.hpp"

class Artiste : public Art{
    private :
        string nom;
    public :
        Artiste(string nom = "?") : nom(nom) {}
        ~Artiste() override {cout <<"destructeur Artiste ";}
        virtual ostream &affiche(ostream & s) const{
            return s<<"de nom "<<this->nom<<" ";
        }
        // string getNom() const{return this->nom;} // possible de mettre la définition inline
        string getNom() const; // la définition de cette méthode sera donnée dans le .cpp correspondant
};

ostream & operator <<(ostream &s, const Artiste &a);
#endif

