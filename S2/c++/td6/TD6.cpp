#include <iostream>
#include <string>
using namespace std;

class Personne {
  string nom, prenom;
  int age;
public :
  Personne(string prenom="Juste", string nom="Leblanc", int age=40) :nom(nom), prenom(prenom), age(age) {}
  string getNom() {return this->nom; }
  string getPrenom() {return this->prenom; }
  int getAge() {return this->age;}
  ostream & affiche(ostream &s) const {
    s<<this->prenom<<" "<<this->nom<<" âgé de "<<this->age <<" an(s) "; 
    return s; 
  }	   
};


ostream & operator <<(ostream &s, const Personne &personne) {
  return personne.affiche(s); 
}

// Employe : une personne ayant un métier et un salaire
class Employe : public Personne {
  string metier;
  int salaire;
public :
  Employe(string prenom, string nom, int age, string metier, int salaire) : Personne(prenom, nom, age), metier(metier), salaire(salaire){}
  ostream & affiche(ostream &s) const {
    Personne::affiche(s);
    s<<"exerçant le métier de "<<this->metier<<" salaire : "<<this->salaire<<" euros"<<endl;
    return s; 
  }
  string getMetier() const {return this->metier;}
  int getSalaire() const {return this->salaire;}
};

ostream & operator <<(ostream &s, const Employe &employe) {
  return employe.affiche(s); 
}


// Etudiant : une personne avec une formation et un tableau de notes!!!


int main() {
  Personne personne("arthur", "martin", 20);
  Employe employe("jules", "cesar", 56, "chef des romains", 3429);
  cout<<personne<<employe; 
  // ajout de l'étudiant ensuite 
  
}
