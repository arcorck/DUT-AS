#include<iostream>
#include<string>
using namespace std; 

class Animal {
  string espece; 

public : 
  Animal(string espece = "?") : espece(espece) {}

  ostream & affiche(ostream & s) const {
    return s<<"Animal d'espéce "<<this->espece<<" ";
  }

  // string toString() const {
  //   return "Animal d'espèce "+this->espece;
  // }

  string getEspece() const {
    return this->espece;
  }

  ~Animal() {cout<<"destruction Animal "<<endl;}
}; 

ostream & operator <<(ostream &s, const Animal &a) {
  return a.affiche(s); 
}

// ostream & operator <<(ostream &s, const Animal &a) {
//   s << a.toString(); 
//   return s;
// }

class Chien : public Animal {
  string nomMaitre; 

public : 
  Chien(string nom ="?") : Animal("mammifère (chien)") , nomMaitre(nom) {}

  ostream & affiche(ostream & s) const {
    Animal::affiche(s);
    return s << "appartenant à " << this->nomMaitre << endl;
  }

  string getMaitre() const {
    return nomMaitre;
  }

  ~Chien() {
    cout << "destruction chien" << endl;
  }
};


ostream & operator <<(ostream &s, const Chien &c) {
  return c.affiche(s); 
}
 

class Chat : public Animal {
  string couleurPelage; 

public : 
  Chat(string pelage ="?") : Animal("mammifère (chat)") , couleurPelage(pelage) {}

    ostream & affiche(ostream & s) const {
    Animal::affiche(s);
    return s << "à un pelage " << this->couleurPelage <<  endl;
  }

  string getCouleur() const {
    return couleurPelage;
  }

  ~Chat() {
    cout << "destruction chat" << endl;
  }
};

ostream & operator <<(ostream &s, const Chat &c) {
  return c.affiche(s); 
}
 

int main() {
  Animal animal("mammifère"); 
  Chien chien("Arthur");
  Chat chat("roux");
  cout<<animal<<endl; 
  cout<<chien;   
  cout<<chat;   
}