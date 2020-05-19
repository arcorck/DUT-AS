/* 
 * Pour ce TD, on veut conserver dans une même structure différents artistes qui seront soit chanteur soit acteur soit ....
 * Pour chaque artiste, je devrai disposer d'une méthode void quelArtC() const; qui affichera l'art pratiqué par l'artiste. 
 * (Le chant pour un chanteur et le cinéma ou le théatre pour un acteur.)
 * Tous les artistes auront un nom (string), les acteurs auront en plus une nationalité (string) et une année de naissance;
 * les chanteurs seront associés à un type de musique (string).
 *
 * En vous basant sur le cours6.cpp vu avec Mme Anglade la semaine dernière, et le fichier Plante.cpp vu avec M. Chabin, 
 * proposez et implémentez une hièrarchie composée de 4 objets (Art, Artiste, Chanteur, Acteur). 
 * Complétez avec un programme principal qui associera un acteur et un chanteur dans un tableau.
 * Affichez le contenu de ce tableau  en vérifiant que l'on affiche bien les bonnes informations.
 * A la fin de votre programme principal, pensez à liberer tout l'espace que vous avez alloué 
 * dynamiquement (et vérifiez qu'il est bien libéré en ajoutant des messages dans les destructeurs.)
 * 
*/

#include<iostream>
using namespace std;

class ArtPratique {
    public :
        virtual void quelArtC() = 0;
        virtual ~ArtPratique()=0;
};
ArtPratique::~ArtPratique() {cout<<"destructeur de ArtPratique;";}


class Artiste : public ArtPratique{
    private :
        std::string nom;
    public :
        Artiste(std::string nom = "?") : nom(nom) {}
        virtual ostream &affiche(ostream & s) const{//tenter d'exécuter en retirant le mot virtual
            return s<<"de nom "<<this->nom<<" ";
        }
        std::string getNom() const{return this->nom;}
        ~Artiste() override {cout <<"destructeur Artiste";}
};

ostream & operator <<(ostream &s, const Artiste &a){
    return a.affiche(s);
}

class Chanteur : public Artiste{
    private :
        std::string typeDeMusique;
    public :
        Chanteur(std::string nom, std::string musique="?") : Artiste(nom), typeDeMusique(musique) {}
        ostream & affiche(ostream & s) const
        {
            s<<"Chanteur ";
            Artiste::affiche(s);
            //s<<"Chanteur de nom " << this->getNom();
            return s<<"joue le genre de musique "<<this->typeDeMusique;
        }
        std::string getTypeDeMusique() const {return this->typeDeMusique;}
        ~Chanteur() override{cout<<"destructeur Chanteur ";}
        void quelArtC() override {cout<<"Mon art c'est le chant";}
};

class Acteur : public Artiste{
    private :
        std::string nationalite;
        int anneeNaiss;        
    public :
        Acteur(std::string nom, std::string origine="?",int age=20) : Artiste(nom), nationalite(origine), anneeNaiss(age) {}
        ostream & affiche(ostream & s) const
        {
            s<<"Acteur ";
            Artiste::affiche(s);
            // s<<"Acteur de nom " << this->getNom();
            return s<<" nationnalité : "<<this->nationalite << " année naiss : " << this->anneeNaiss;
        }
        std::string getNationalite() const {return this->nationalite;}
        int getAnneeNaiss() const {return this->anneeNaiss;}

        ~Acteur() override{cout<<"destructeur Acteur ";}
        void quelArtC() override {cout<<"Mon art c'est le théatre";}
};

int main() {
  Artiste * lesArtistes[2];
  lesArtistes[0] = new Chanteur("Arthur", "Jazz"); 
  lesArtistes[1] = new Acteur("Ray","France",25); 
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
