#include <iostream>
#include <string>
using namespace std;

/*
 * On vous propose ici d'implémenter une hierarchie de classes en C++ qui vont nous permettre de gérer des plantes.
 * 
 * Chaque plante a un nom, cela peut-être :
 * un arbre qui disposera d'une hauteur, 
 * un fruitier qui en plus d'une hauteur disposera aussi du nom du fruit qu'il produit, 
 * une fleur avec une couleur,
 * un légume avec féculent oui/non et un prix au kilo.
 * 
 * 1. Proposez un diagramme de classes.
 * 2. Rappelez ce qu'est la forme coplien pour une classe?
 * 3. Pensez-vous avoir besoin de mettre sous forme coplien certaines classes de votre hierarchie?
 * 4. Implémentatez les différentes classes avec les méthodes classiques.
 * 5. Ajoutez la méthode "ostream & affiche(ostream &s) const" à chacune de vos classes.
 * 6. Ajoutez dans vos constructeurs l'affichage d'un message "constructeur plante" ...
 * 7. Ajoutez des destructeurs avec juste un affichage "destructeur plante" ...
 * 8. Testez votre implémentation dans un programme principale en manipulant au moins une instance de chaque classe.
 * 
 * Soit la déclaration suivante : Plante * tab[6]; qui sera un tableau de 6 cases.
 * 9. Quel est le type des éléments contenus dans chaque case.
 * 10. Quels types d'instance peuvent réellement être mises dans tab?
 * 11. Remplissez la variable tab en utilisant de l'allocation dynamique.
.* 12. Faites affichez le contenu de votre tableau.
 * 13. Que constatez-vous?
 * 
 * En attendant de voir comment faire de la compilation séparée en C++ vous mettrez toutes vos classes dans un même 
 * fichier Plante.cpp
 */

class Plante {
    string nom;

    public :
        Plante(string n = "aucun nom") : nom(n){
            // cout << "ConstructPlante" << endl;
        }

        string getNom() const {
            return this->nom; 
        }

        string toString () const{
            return "Nom : " + this->nom;
        }

        ostream & affiche(ostream &s) const {
            s << this->toString() << endl;
            return s; 
        } 
        ~Plante(){
        //  cout << "DestructPlante" << endl;
    }
};

ostream & operator <<(ostream &s, const Plante &plante){
    return plante.affiche(s);
}

class Arbre : public Plante{
    double hauteur_;

    public :
        Arbre (string n = "aucun nom", double h = 0) : Plante (n), hauteur_(h){ 
            // cout << "ConstructArbre" << endl;
        }

        string toString () const {
            return "Nom : " + Plante::getNom() + ", a une hauteur de " + to_string(this->hauteur_) + " mètres et est un arbre";
        }

        ostream & affiche(ostream &s) const {
            s << this->toString() << endl;
            return s; 
        } 
        ~Arbre(){
        //  cout << "DestructArbre" << endl;
        }
};

ostream & operator <<(ostream &s, const Arbre &arbre){
    return arbre.affiche(s);
}

class Fruitier : public Arbre {
    string fruit;

    public :
        Fruitier (string n = "aucun nom", double h = 0, string f = "aucun fruit") : Arbre(n,h), fruit(f){ 
            // cout << "ConstructFruitier" << endl;
        }

        string toString () const {
            return Arbre::toString() + " fruitier\nL'arbre a pour fruit : " + this->fruit;
        }

        ostream & affiche(ostream &s) const {
            s << this->toString() << endl;
            return s; 
        } 
        ~Fruitier(){
        //  cout << "DestructFruitier" << endl;
        }
};

ostream & operator <<(ostream &s, const Fruitier &f){
    return f.affiche(s);
}

class Fleur : public Plante{
    string couleur;

    public :
        Fleur (string n = "aucun nom", string c = "sans couleur") : Plante (n), couleur(c){ 
            // cout << "ConstructFleur" << endl;
        }

        string toString () const {
            return "Fleur ayant pour nom : " + Plante::getNom() + " et de couleur " + this->couleur;
        }

        ostream & affiche(ostream &s) const {
            s << this->toString() << endl;
            return s; 
        } 
        ~Fleur(){
        //  cout << "DestructFleur" << endl;
        }
};

ostream & operator <<(ostream &s, const Fleur &f){
    return f.affiche(s);
}

class Legume : public Plante{
    bool feculent;
    double prix;

    public :
        Legume (string n = "aucun nom", bool f = false, double p = 0) : Plante (n), feculent(f), prix(p){ 
            // cout << "ConstructLegume" << endl;
        }

        string toString () const {
            if (this->prix){
                return "Legume ayant pour nom : " + Plante::getNom() + ", est un féculent vendu " + to_string(this->prix) + "€/kg";
            }else{
                return "Legume ayant pour nom : " + Plante::getNom() + ", n'est pas un féculent et est vendu " + to_string(this->prix) + "€/kg";
            }
        }

        ostream & affiche(ostream &s) const {
            s << this->toString() << endl;
            return s; 
        } 
        ~Legume(){
        //  cout << "DestructLegume" << endl;
        }
};

ostream & operator <<(ostream &s, const Legume &l){
    return l.affiche(s);
}

int main(){
    Plante p("Orchidée");
    cout << p.getNom() << endl;
    cout << p << endl;
    Arbre a;
    Arbre b ("Chene", 6.2);
    cout << a;
    cout << b;
    cout << a.getNom() << endl;
    cout << b.getNom() << endl;
    cout << endl;
    Fruitier f;
    Fruitier g ("Cerisier", 4, "Cerise");
    cout << f;
    cout << g << endl;
    Fleur q;
    Fleur m ("Tulipe", "Rose");
    cout << q;
    cout << m << endl;
    Legume w;
    Legume x ("Flageolet", true, 8.56);
    cout << w;
    cout << x;
}