#ifndef ACTEURHPP
#define ACTEURHPP

#include<iostream>
using namespace std;
#include"Artiste.hpp"

class Acteur : public Artiste{
    private :
        string nationalite;
        int anneeNaiss;        
    public :
        Acteur(string nom, string origine="?",int annee=1999) : Artiste(nom), nationalite(origine), anneeNaiss(annee) {}
        ~Acteur() override{cout<<"destructeur Acteur ";}
        
        ostream & affiche(ostream & s) const override
        {
            s<<"Acteur ";
            Artiste::affiche(s);
            return s<<" nationnalité : "<<this->nationalite << " année naiss : " << this->anneeNaiss;
        }
		string getNationalite() const;  // definition dans le .cpp
        int getAnneeNaiss() const {return this->anneeNaiss;}

        void quelArtC() override {cout<<"Mon art c'est le théatre";}
};

#endif

