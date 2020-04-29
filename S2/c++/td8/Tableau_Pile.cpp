#include <iostream>
#include <vector>
using namespace std;

class Tableau{
    vector<int> table;
    int taille; // taille max
    int nombre; // nombre d'éléments (0 à l'initialisation)

    public :
        // permet de construire un tableau contenant 0 élément mais de taille n // on réserve la place pour ces n éléments
        Tableau(int n = 10){
            this->taille = n;
            this->nombre = 0;
            for (size_t i = 0; i < n; ++i) {
                this->table.push_back(0);
            }
        }

        // surcharge du [] permettant d'écrire t[i] = 3;
        // prévoir quand on ajoute un élément et quand on modifie
        int & operator[](int i){
            this->table.push_back(i);
            this->nombre++;
            return this->table.at(i);
        }

        // surcharge de [] mais uniquement comme observateur
        int operator[](int i) const {
            return this->table.at(i);
        }

        int getTaille() const {
            return this->taille; 
        }

        int getNbElem() const {
            return this->nombre; 
        }

        void toString () {
            for (int i = 0; i < this->nombre-1; ++i){
                cout << this->table[i] << ", ";
            }
            cout << this->table[this->nombre] << endl;
        }

        ostream & affiche(ostream &s) const {
            for (int i = 0; i < this->nombre-1; ++i){
                s << this->table[i] << ", ";
            }
            s << this->table[this->nombre] << endl;
            return s; 
        } 

        void setNbElem() {--this->nombre;} // servira pour la pile

        friend ostream & operator <<(ostream &s, const Tableau &tab){
            return tab.affiche(s);
        }
};

// class Pile : private Tableau {
//     public :
//         Pile() : Tableau() {}

//         // empiler un élément
//         void empiler(int val){
            
//         }

//         // sommet de pile
//         int sommet() const{

//         } 

//         // pile vide ?
//         bool pileVide() const {
            
//         }

//         // supprimer un élément de la pile
//         void depiler() {

//         }
// };

int main (){
    Tableau t(5);
    cout << "taille : " << t.getTaille() << endl;
    cout << "nb elem : " << t.getNbElem() << endl;
    t[0] = 5;
    cout << "taille : " << t.getTaille() << endl;
    cout << "nb elem : " << t.getNbElem() << endl;
    t[4] = 4;
    cout << t[0] << endl;
    cout << t[4] << endl;
    cout << "taille : " << t.getTaille() << endl;
    cout << "nb elem : " << t.getNbElem() << endl;
    t[0] = 9;
    cout << t;
}