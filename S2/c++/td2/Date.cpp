#include<iostream>
using namespace std;

class Date{
    private :
        int j, m, a;
    public : 
        Date (int jour, int mois, int an){
            this->j = jour;
            this->m = mois;
            this->a = an;
        }

        bool bissextile(){
            if (this->a % 400 == 0){
                return true;
            }else{
                if (this->a % 4 == 0) {
                    if (this->a % 100 != 0){
                        return true;
                    }
                    else{
                        return false;
                    }
                }else{
                    return false;
                }
            }
        }

        int nbJourMois() {
            if (this->m < 1 || this->m > 12 || this->j < 1 || this->j > 31){
                return -1;
            }else{
                if (this->m == 1 || this->m == 3 || this->m == 5 || this->m == 7 || this->m == 8 || this->m == 10 || this->m == 12){
                    return 31;
                }else{
                    if (this->m == 4 || this->m == 6 || this->m == 9 || this->m == 11 ){
                        return 30;
                    }else{
                        if (this->bissextile()){
                            return 29;
                        }else{
                            return 28;
                        }
                    }
                }  
            }
        }

        bool valide() {
            if (this->m > 12 || this->m < 1 || this->j < 1){
                return false;
            }
            if (this->m == 1 || this->m == 3 || this->m == 5 || this->m == 7 || this->m == 8 || this->m == 10 || this->m == 12){
                return this->j <= 31;
            }else{
                if (this->m == 4 || this->m == 6 || this->m == 9 || this->m == 11 ){
                    return this->j <= 30;
                }else{
                    if (this->bissextile()){
                        return this->j <= 29;
                    }else{
                        return this->j <= 28;
                    }
                }
            } 
        }
        
         std::string toString() const{ // méthode d'affichage (noter le décorateur const)
            std::string res = "";
            res += std::to_string(this->j);
            res += "/";
            res += std::to_string(this->m);
            res += "/";
            res += std::to_string(this->a);
            return res;
        }
};

ostream & operator <<(ostream & sortie, const Date & date) {
    sortie<<date.toString();
    return sortie;
}

int main (){
    Date d(15,1,1997), d1(15,2,2000);
    cout << "date d : " << d << endl;
    cout << "date d1 : " << d1 << endl;
    cout << "d est bissextile : " << d.bissextile() << endl;
    cout << "d1 est bissextile : " << d1.bissextile() << endl;
    cout << "d est valide : " << d.valide() << endl;
    cout << "d1 est valide : " << d1.valide() << endl;
    cout << "nombre de jour de janvier : " << d.nbJourMois() << endl;
    cout << "nombre de jour de février bissextile : " << d1.nbJourMois() << endl;
    return 0;
}