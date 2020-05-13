#include<iostream>
using namespace std;

class CommentCrier {
public : 
  virtual void crier() = 0;
  virtual ~CommentCrier() = 0; 
}; 

CommentCrier::~CommentCrier() {cout<<"destructeur de CommmentCrier ";}

class QueManger {
  public : 
  virtual void manger() = 0;
  virtual ~QueManger() = 0; 
}; 

QueManger::~QueManger() {cout<<"destructeur de QueManger ";}

  
class Animal : public CommentCrier, public QueManger {
  std::string espece; 
public : 
  Animal(std::string espece = "?") : espece(espece) {}
  // virtual 
  ostream & affiche(ostream & s) const {
    return s<<" d'espèce "<<this->espece<<" ";
  }  
  std::string getEspece() const {return this->espece;}
  ~Animal() override {cout<<"destruction Animal ";}
}; 

ostream & operator <<(ostream &s, const Animal &a) {
  return a.affiche(s); 
}

class Chien : public Animal {
  std::string nomMaitre; 
public : 
  Chien(std::string nom ="?") : Animal("mammifère"), nomMaitre(nom) {}
  //virtual
  ostream & affiche(ostream & s) const
  // override
  {
    s<<"Chien"; 
    Animal::affiche(s);
    return s<<"appartient à "<<this->nomMaitre; 
  }
  std::string getMaitre() const {return this->nomMaitre;}
  ~Chien() override {cout<<"destruction Chien ";}
  void crier() override {cout<<"j'aboie ";}
  void manger() override {cout<<"je mange de la pâtée pour chien ";}
};

class Chat : public Animal {
  std::string couleurPelage; 
public : 
  Chat(std::string pelage ="?") : Animal("mammifère"), couleurPelage(pelage) {}
  //virtual
  ostream & affiche(ostream & s) const
  // override
  {
    s<<"Chat";
    Animal::affiche(s);
    return s<<"au pelage couleur "<<this->couleurPelage; 
  }
  std::string getCouleur() const {return this-> couleurPelage;}
  ~Chat() override {cout<<"destruction Chat ";}
  void crier() override {cout<<"je miaule ";}
  void manger() override {cout<<"je mange des souris ";}
};  


int main() {
  Animal * zoo[2];
  zoo[0] = new Chien("Arthur"); 
  zoo[1] = new Chat("roux"); 
  for(int i = 0; i < 2; ++i) {
    cout<<*zoo[i]<<" ";
    cout<<endl; 
    zoo[i] -> crier();
    zoo[i] -> manger();
    cout<<endl<<endl; 
  }
  for(int i = 0; i < 2; ++i) {
    delete zoo[i];
    cout<<endl;
  }
}

