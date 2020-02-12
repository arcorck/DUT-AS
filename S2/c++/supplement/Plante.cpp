#include <iostream>
#include <string>
#include <vector>
#include <list>
using namespace std;

class Plante{
    string nom, couleur;
    double taille;

    public : 
        Plante(string nom="Plante", string couleur="blanc", double taille=0){
            this->nom = nom;
            this->couleur = couleur;
            (*this).taille = taille;
            //(*this).champ et this->champ sont équivalents 
        }

        string getNom(){
            return this->nom;
        }

        string getCouleur(){
            return this->couleur;
        }

        double getTaille(){
            return this->taille;
        }

        void setTaille (double t){
            this->taille = t;
        }

        void setCouleur (string c){
            this->couleur = c; 
        }

        string toString(){
            return "La plante " + this->nom + " est de couleur " + this->couleur + " et mesure environ " + to_string(this->taille) + " cm\n";
        }

        ~Plante() {}
};

ostream & operator << (ostream & s, Plante p){
    s << p.toString();
    return s;
}

class Herbier {
    vector<Plante> mesplantes;

    public :
        Herbier (){}

        void add(Plante p){
            this->mesplantes.push_back(p);
        }

        string toString(){
            string res = "Mon herbier est consitué de : ";
            for (Plante p : this->mesplantes){
                res += "\n  -  " + p.getNom();
            }
            return res;
        }

        Plante laplusPetite () {
            float min = this->mesplantes[0].getTaille();
            Plante res;
            for (Plante p : this->mesplantes){
                if (p.getTaille() < min ){
                    min = p.getTaille();
                    res = p;
                }
            }
            return res;
        }
};

ostream & operator << (ostream & s, Herbier h){
    s << h.toString();
    return s;
}

int main (){
    Plante p1 ("jonquille", "verte", 12);
    Plante p2 ("Tulipe", "jaune", 18.54);
    Plante p3 ("Orchidee", "violette", 23.6);
    cout << p1 << p2 << p3 <<endl;
    Herbier monherbier;
    monherbier.add(p1);
    monherbier.add(p2);
    monherbier.add(p3);
    cout << monherbier << endl;
    cout << " " << endl;
    cout << "La plante la plus petite est : " << monherbier.laplusPetite().getNom() << endl;
    return 0;
}