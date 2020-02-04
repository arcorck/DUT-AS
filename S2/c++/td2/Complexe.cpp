#include <iostream>
using namespace std;

class Complexe{
    private : 
        float x, y;
    
    public :
        Complexe(float x, float y){
            this->x = x;
            this->y = y;
        }

        Complexe(){
            this->x = 0.0;
            this->y = 0.0;
        }

        float getPrem() const{
            return this->x;
        }

        float getSec() const{
            return this->y;
        }

        void setPrem(float val){
            this->x = val;
        }

        void setSec(float val){
            this->y = val;
        }

        std::string toString() const{ // méthode d'affichage (noter le décorateur const)
            std::string res = "(";
            res += std::to_string(this->getPrem());
            res += ",";
            res += std::to_string(this->getSec());
            res += ")";
            return res;
        }

        ~Complexe() {cout<<"destructeur de Complexe"<<endl;}

};

ostream & operator <<(ostream & sortie, const Complexe & complexe) {
    sortie<<complexe.toString();
    return sortie;
}

int main(){
    Complexe complexe(1.0f, 2.5f);
    cout << complexe << endl;
    return 0;
}