#include<iostream>
#include<string>
using namespace std;

class Entier {
  int * val;
public :
  Entier(int valeur = 0) {
      this->val = new int (valeur);
  }

  int getVal() {
      return this->val;
  }

  void setVal(int valeur) {
      this->val = & valeur;
  }

  string toString() {
      return to_string(this->val);
  }
};

ostream & operator <<(ostream & sortie, Entier & entier) {
    sortie<<entier.toString();
    return sortie;
}

int main() {
  cout<<" classe Entier et pointeur "<<endl;
  Entier ent(5);
  cout<<"entier "<<ent<<" valeur "<<ent.getVal()<<endl;
  ent.setVal(-7);
  Entier autre;
  autre = ent;
  autre.setVal(-2);
  cout<<"entier "<<ent<<" autre entier "<<autre<<endl;
}