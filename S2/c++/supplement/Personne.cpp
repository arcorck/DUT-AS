#include <iostream>
#include <string>
#include <list>
using namespace std;

class Personne{
    string nom;
    int age;
    
    public :
        Personne(string nom="Dupont", int age=0){
            this->nom = nom;
            (*this).age = age;
            //(*this).champ et this->champ sont équivalents 
        }

        int getAge(){
            return this->age;
        }

        string getNom(){
            return this->nom;
        }

        string toString(){
            return this->nom + " est agé de " + to_string(this->age) + " an(s)\n";
        }

        ~Personne() {}
};

ostream & operator << (ostream & s, Personne p){
    s << p.toString();
    return s;
}

class ListePersonnes {
    list<Personne> personnes;

    public : 
        ListePersonnes(){} //non obligatoire car existe par défaut 

        void add (Personne p){
            this->personnes.push_back(p);
        }

        string toString(){
            string res = "";
            for (Personne p : this->personnes){
                res += p.toString();
            }
            return res;
        }

        Personne doyen(){
            int age = this->personnes.front().getAge();
            Personne personne;
            for (Personne pers : this->personnes){
                if (pers.getAge() > age){
                    age = pers.getAge();
                    personne = pers;
                }
            }
            return personne;
        }
};

ostream & operator << (ostream & s, ListePersonnes lp){
    s << lp.toString();
    return s;
}

int main (){
    Personne m("Martin", 21);
    Personne a("Arnaud", 23);
    Personne n("Nicolas", 22);
    Personne f("Fab", 23);
    //cout << m << a;
    ListePersonnes lp;
    lp.add(m);
    lp.add(a);
    lp.add(n);
    lp.add(f);
    cout << lp;
    cout << "le doyen : " << lp.doyen();
}