#include <iostream>
#include <list>
using namespace std;

class Fantome{
    private : 
        string nom, origine;
        int nuisance;
    
    public :
        Fantome(string name, string o, int n=-1){
            this->nom = name;
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
            if (this->getNuisance() != -1){
                res += " de nuisance ";
                res += std::to_string(this->getNuisance());
            }
            res += "\n";
            return res;
        }  

        ~Fantome() {}      
};

ostream & operator <<(ostream & sortie, const Fantome & f) {
    sortie<<f.toString();
    return sortie;
}

class Armee{
    private : 
        list<Fantome> armee ;
    
    public :
        Armee(){}

        string toString() const{ // méthode d'affichage (noter le décorateur const)
            string res = "";
            for (Fantome f : this->armee){
                res += f.toString();
            }
            return res;
        }  

        void enrole(Fantome f){
            this->armee.push_back(f);
        }

        void enroleSpecial(Fantome fant){
            bool existe = false;
            for (Fantome f : this->armee){
                if (f.getNuisance() == fant.getNuisance()){
                    existe = true;
                }
            }
            if (!existe){
                this->armee.push_back(fant);
            }
        }

        Fantome leMoinsNuisible (){
            Fantome fantomemoinsnuisible (" ", " ");
            int min =  this->armee.front().getNuisance();
            for (Fantome f : this->armee){
                if (f.getNuisance() < min && f.getNuisance()!=-1){
                    fantomemoinsnuisible = f;
                }
            }
            return fantomemoinsnuisible;
        }

        list<Fantome> nuisancePlusDe (int nuisance){
            list<Fantome> res;
            for (Fantome f : this->armee){
                if (f.getNuisance() >= nuisance){
                    res.push_back(f);
                }
            }
            return res;
        }

        ~Armee() {}      
};

ostream & operator <<(ostream & sortie, const list<Fantome> & a) {
    sortie<<a.toString();
    return sortie;
}

int main (){
    Fantome lemure ("Lémure", "romaine", 5);
    Fantome willis ("Willis", "slave", 2);
    Fantome mau ("Mau", "egyptienne");
    cout << "Des Fantomes : " << lemure << " " << mau << endl;
    Armee armeeFantomes;
    armeeFantomes.enrole(lemure);
    armeeFantomes.enrole(willis);
    armeeFantomes.enrole(mau);
    cout << "Armee enrôlement : " << armeeFantomes << endl;
    armeeFantomes.enroleSpecial(Fantome("Inanna", "mesopotoamienne", 7));
    armeeFantomes.enroleSpecial(Fantome("Charon", "grecque", 2));
    cout << "Armee enrôlement : " << armeeFantomes << endl;
    cout << "fantome le moins nuisible : " << armeeFantomes.leMoinsNuisible() << endl;
    cout << "fantomes avec une nuisance de plus de 3 : " << armeeFantomes.nuisancePlusDe(3) << endl;
    return 0;
}