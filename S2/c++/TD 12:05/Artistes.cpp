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

#include <iostream>
#include <string>
using namespace std;

class QuelArt {
public : 
  virtual void quelArt() = 0;
  virtual ~QuelArt() = 0; 
}; 

QuelArt::~QuelArt() {cout<<"destructeur de QuelArt ";}

class Artiste : public QuelArt{
    string nom;

    public :
        Artiste(string n = "aucun nom") : nom(n){
            cout << "ConstructArtiste" << endl;
        }

        string getNom() const {
            return this->nom; 
        }

        string toString () const{
            return "Nom : " + this->nom;
        }

        virtual ostream & affiche(ostream &s) const {
            s << this->toString() << endl;
            return s; 
        } 
        ~Artiste(){
          cout << "DestructArtiste" << endl;
    }
};

ostream & operator <<(ostream &s, const Artiste &artiste){
    return artiste.affiche(s);
}

class Acteur : public Artiste{
    string nationalite;
    int naissance;

    public :
        Acteur (string n = "aucun nom", string nationalite = "nul part", int birth = 0) : Artiste (n), nationalite(nationalite), naissance(birth){ 
             cout << "ConstructActeur" << endl;
        }

        string toString () const {
            return "Nom : " + Artiste::getNom() + "est né en " + to_string(this->naissance) + " et est de nationalité " + this->nationalite;
        }

        ostream & affiche(ostream &s) const {
            s << this->toString() << endl;
            return s; 
        } 
        ~Acteur(){
          cout << "DestructActeur" << endl;
        }
        void quelArt() {cout<<"je joue dans les films ";}
};

class Chanteur : public Artiste{
    string nationalite;
    string type_musique;

    public :
        Chanteur (string n = "aucun nom", string nationalite = "nul part", string musique = "aucun type de musique") : Artiste (n), nationalite(nationalite), type_musique(musique){ 
             cout << "ConstructChanteur" << endl;
        }

        string toString () const {
            return "Nom : " + Artiste::getNom() + " est de nationalité " + this->nationalite + " et joue du " + this->type_musique;
        }

        ostream & affiche(ostream &s) const {
            s << this->toString() << endl;
            return s; 
        } 
        ~Chanteur(){
          cout << "DestructChanteur" << endl;
        } 
        void quelArt() {cout<<"je chante ";}
};

int main(){
    Artiste * lesartistes[2];
    lesartistes[0] = new Acteur("Thierry Lhermitte", "Française", 1952); 
    lesartistes[1] = new Chanteur("Freddy Mercury", "britannique", "rock"); 
    for(int i = 0; i < 2; ++i) {
    cout<<*lesartistes[i]<<" ";
    cout<<endl; 
    lesartistes[i] -> quelArt();
    cout<<endl<<endl; 
    }
    for(int i = 0; i < 2; ++i) {
        delete lesartistes[i];
        cout<<endl;
    }
    return 0;
}