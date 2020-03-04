#include <iostream>
using namespace std;

class Fantome{
    private : 
        string nom, origine;
        int nuisance;
    
    public :
        Complexe(string n, string o, int n=-1){
            this->nom = n;
            this->origine = o;
            this->nuisance = n;
        }

        string getNom ()const{
            return this->nom;
        }

        string getOrigine ()const{
            return this->origine;
        }

        int getNuisance ()const{
            return this->nuisance;
        }

        std::string toString() const{ // méthode d'affichage (noter le décorateur const)
            std::string res = "Fantome ";
            res += this->getNom();
            res += " d'origine ";
            res += this->getOrigine();
            res += " de nuisance ";
            res += std::to_string(this->getNuisance());
            res += "\n";
            return res;
        }  

        ~Fantome() {cout<<"destructeur de Fantome"<<endl;}      
};

ostream & operator <<(ostream & sortie, const Fantome & f) {
    sortie<<f.toString();
    return sortie;
}

int main (){
    Fantome lemure ("Lémure", "romaine", 5);
    Fantome willis ("Willis", "slave", 2);
    Fantome mau ("Mau", "egyptienne");
    cout << "Des Fantomes : " << lemure << " " << mau << endl;
    return 0;
}