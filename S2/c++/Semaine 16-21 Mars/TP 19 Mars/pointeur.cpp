#include<iostream>
using namespace std;

class Chien{
  private:
	string nom;
	string couleur;
	int lgPoils;
  public:
    Chien(string n, int lg, string c){
		this->nom=n;
		this->couleur=c;
		this->lgPoils=lg;
	}
	string getNom()const{
		return this->nom;
	}
	string getCouleur()const{
		return this->couleur;
	}
	int getLgPoils()const{
		return this->lgPoils;
	}
	void setLgPoils(int nl){
		this->lgPoils=nl;
	}
	string toString()const{
		return this->nom + " de couleur " + this->couleur + " longueur des poils : " + to_string(this->lgPoils) + "cm";
	}
};

ostream& operator<<(ostream& out, const Chien &c){
	out << c.toString();
	return out;
}

int main(){
	Chien will("Will", 4, "blanc et noir");
	Chien *ptrChien;
	ptrChien = &will;
	cout << will << endl;
	cout << *ptrChien << endl;
}
