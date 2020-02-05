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

        Complexe operator + (Complexe c){ // surcharge de +
            return Complexe (this->x + c.x, this->y + c.y);
        }

        Complexe operator - (Complexe c){ // surcharge de +
            return Complexe (this->x - c.x, this->y - c.y);
        }

        Complexe operator * (Complexe c){ // surcharge de +
            return Complexe (this->x * c.x, this->y * c.y);
        }

        float operator () (int i){ // surcharge de +
            if (i == 1){
                return this->x;
            }else{
                if (i==2){
                    return this->y;
                }else{
                    return 0.0;
                }
            }
        }
    
        ~Complexe() {cout<<"destructeur de Complexe"<<endl;}

};

ostream & operator <<(ostream & sortie, const Complexe & complexe) {
    sortie<<complexe.toString();
    return sortie;
}

int main(){
    Complexe c1(1.0f, 2.5f), c2(1.5f, 3.0f);
    cout << "c1 : " << c1 << endl;
    cout << "c2 : " << c2 << endl;
    cout << "c1 + c2 : " << c1+c2 << endl;
    cout << "c1 - c2 : " << c1-c2 << endl;
    cout << "c1 x c2 : " << c1*c2 << endl;
    cout << "x de c1 : " << c1(1) << endl;
    cout << "y de c1 : " << c1(2) << endl;
    return 0;
}