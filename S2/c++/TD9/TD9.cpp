#include <iostream>
#include <string>
using namespace std;

class Deplacement {
    public : 
        virtual float getCo2() const = 0;
        virtual string toString() const = 0;
        virtual ~Deplacement() = 0; 
}; 
Deplacement::~Deplacement() {
    // cout<<"destructeur de Deplacement ";
}

ostream & operator <<(ostream &s, const Deplacement &dep){
    return s << dep.toString();
}

class Trajet : public Deplacement{
    int distance = 0;
    string motif = ""; 

    public : 
        Trajet (string motif = "aucun motif", int dist = 0) : distance(dist), motif(motif){
            // cout << "ConstructTrajet" << endl;
        } 
        
        int getDistance() const{
            return this->distance;
        }

        string getMotif(){
            return this->motif;
        }

        string toString() const override{
            return "Déplacement de " + this->motif + ", d'une distance de " + to_string(this->distance) + " km";
        }
        
        ~Trajet() override {
        //   cout << "destructTrajet" << endl;
        }
}; 
ostream & operator <<(ostream &s, const Trajet &t){
    return s << t.toString();
}

class TrajetVelo : public Trajet {
    public :
        TrajetVelo (string motif = "aucun motif", int dist = 0) : Trajet(motif, dist){ 
            //  cout << "ConstructTrajetVelo" << endl;
        }

        float getCo2 () const{
            return 0;
        }

        virtual string toString() const{
            return Trajet::toString() + " éfféctué à vélo a émis " + to_string(this->getCo2()) + "g de CO2";
        }

        ~TrajetVelo(){
        //   cout << "destructTrajetVelo" << endl;
        }
};

class TrajetCommun : public Trajet {
    public :
        TrajetCommun  (string motif = "aucun motif", int dist = 0) : Trajet(motif, dist){ 
            //  cout << "ConstructTrajetCommun" << endl;
        }

        float getCo2 () const{
            return 0.5 * Trajet::getDistance();
        }

        virtual string toString() const {
            return Trajet::toString() + " éfféctué en transports en commun a émis "  + to_string(this->getCo2()) + "g de CO2";
        }

        ~TrajetCommun(){
        //   cout << "destructTrajetCommun" << endl;
        }
};

class TrajetVoiture : public Trajet {
    int tauxCO2;

    public :
        TrajetVoiture  (string motif = "aucun motif", int dist = 0, int t = 0) : Trajet(motif, dist), tauxCO2(t){ 
            //  cout << "ConstructTrajetVoiture" << endl;
        }

        float getCo2 () const{
            return this->tauxCO2 * Trajet::getDistance() / 100.0;
        }

        virtual string toString() const {
            return Trajet::toString() + " éfféctué en voiture émettant " + to_string(this->tauxCO2) + "g de CO2 pour 100km a émis "  + to_string(this->getCo2()) + "g de CO2";
        }

        ~TrajetVoiture(){
          //cout << "destructTrajetVoiture" << endl;
        }
};

int main() {
    Deplacement *pt1 = new TrajetVelo("Loisir", 24); 
    Deplacement *pt2 = new TrajetCommun("Travail", 10); 
    Deplacement *pt3 = new TrajetVoiture("Travail", 10, 123);
    cout<< *pt1 << "a émis" << pt1->getCo2() << endl;
    // Déplacement Loisir de 24km en Velo a émis : 0g de CO2.
    cout<< *pt2 << endl;
    // Déplacement Travail de 10km en transport en commun a émis : 5g de CO2.
    cout<< *pt3 << endl;
    // Déplacement Travail de 10km en voiture émettant 123g de CO2 pour 100km a émis : ˓→12.3g de CO2.
    delete pt1;
    // destructeur TrajetVelo destructeur Trajet Fin du déplacement
    delete pt2;
    // destructeur TrajetCommun destructeur Trajet Fin du déplacement
    delete pt3;
    // destructeur TrajetVoiture destructeur Trajet Fin du déplacement
    return 0; 
}
