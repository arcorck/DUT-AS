#include <iostream>
using namespace std;

class Couple{
    private : 
        int x, y;
    
    public :
        Couple(int x, int y){
            this->x = x;
            this->y = y;
        }

        Couple(){
            this->x = 0;
            this->y = 0;
        }

        int getPrem() const{
            return this->x;
        }

        int getSec() const{
            return this->y;
        }

        void setPrem(int val){
            this->x = val;
        }

        void setSec(int val){
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

        bool operator == (Couple c){ // surcharge de ==
            return this->x == c.x &&
            this->y == c.y;
        }

        Couple operator + (Couple c){ // surcharge de +
            return Couple (this->x + c.x, this->y + c.y);
        }

        ~Couple() {cout<<"destructeur de Couple"<<endl;}

};

ostream & operator <<(ostream & sortie, const Couple & couple) {
    sortie<<couple.toString();
    return sortie;
}

int main(){
    Couple couple;
    Couple couple1(4, -2);
    Couple couple2(-1, 0);
    cout << couple << " " << couple1 << " " << couple2 << endl; 
    couple = couple1 + couple2;
    cout << couple << endl;
    couple.setPrem(66);
    couple.setSec(-15);
    cout << couple << endl;
    if (couple == couple1){
        cout << "couple et couple 1 égaux" << endl;
    }else{
        cout << "couple et couple 1 non égaux" << endl;
    }
    couple1.setPrem(66);
    couple1.setSec(-15);
    if (couple == couple1){
        cout << "couple et couple 1 égaux" << endl;
    }else{
        cout << "couple et couple 1 non égaux" << endl;
    }
    return 0;
}