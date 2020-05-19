#ifndef CHANTEURHPP
#define CHANTEURHPP

#include<iostream>
using namespace std;
#include"Artiste.hpp"

class Chanteur : public Artiste{
    private :
        string typeDeMusique;
    public :
        Chanteur(string nom, string musique="?") : Artiste(nom), typeDeMusique(musique) {}
        ~Chanteur() override{cout<<"destructeur Chanteur ";}

        ostream & affiche(ostream & s) const override
        {
            s<<"Chanteur ";
            Artiste::affiche(s);
            return s<<"joue le genre de musique "<<this->typeDeMusique;
        }
        
        string getTypeDeMusique() const; // definition dans le .cpp

        void quelArtC() override {cout<<"Mon art c'est le chant";}
};

#endif
