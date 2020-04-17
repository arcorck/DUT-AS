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

class Tablo{
  private:
    float *tab;
    int taille;

	//Lorsque l'objet comporte un pointeur dans ces attributs
	//je dois définir obligatoirement :
	//  - un constructeur
	//  - un constructeur de recopie
	//  - un destructeur
	//  - laz surcharge de l'affectation
	//je dis que mon objet est sous forme de coplien
  public:
    Tablo(int dim){
		this->taille=dim;
		this->tab = new float[dim];
	}
	
	~Tablo(){
		delete [] this->tab;
		this->tab = nullptr;
	}
	
	Tablo(const Tablo &t){
		this->taille = t.taille;
		this->tab = new float[this->taille];
		for(int i=0; i<this->taille; ++i){
			this->tab[i]=t.tab[i];
		}
	}

	Tablo & operator= (const Tablo &t){
		if (this != &t){
			delete[] this->tab;
			this->taille = t.taille;
			this->tab = new float[this->taille];
			for (int i = 0; i < this->taille; ++i){
				this->tab[i] = t.tab[i];
			}
		}
		return *this;
	}
	
	void put(int i, float val) const{
		if(i< this->taille && i >=0){
		    this->tab[i]=val;
		}
		else{
			throw(string("out of range"));
		}
	}
	
	float get(int i) const{
		if(i< this->taille && i >=0){
		    return(this->tab[i]);
		}
		else{
			throw(string("out of range"));
		}
	}	
	
	void doubleTaille(){
		float * old = this->tab;
		this->tab = new float[(this->taille)*2];
		for(int i=0; i<this->taille; ++i){
			this->tab[i]=old[i];
		}
		this->taille = (this->taille)*2;
		delete [] old;
	}
	
	string toString()const{
		string res = "tableau de taille : " + to_string(this->taille) + "[";
		for (int i= 0; i<this->taille; ++i){
			res += to_string(this->tab[i]) + ", ";
		}
		res += "]";
		return res;
	}
	
	void push_back (float val){
		float * old = this->tab;
		this->tab = new float[(this->taille)+1];
		for(int i=0; i<this->taille; ++i){
			this->tab[i]=old[i];
		}
		this->taille = (this->taille)+1;
		this->tab[this->taille-1] = val;
		delete [] old;
	}

	int size(){
		return this->taille;
	}

	float & operator[] (int i){
		return this->tab[i];
	}

	float operator[] (int i) const{
		return this->tab[i];
	}
	
};


// Employe : une personne ayant un métier et un salaire
class Etudiant : public Personne {
  string formation;
  Tablo notes;
  int nbNotes;
public :
  Etudiant(string prenom, string nom, int age, string form) : Personne(prenom, nom, age), formation(form), nbNotes(0), notes(Tablo(50)){}
  
  ostream & affiche(ostream &s) const {
    Personne::affiche(s);
    s<<"\nEtudiant en : "<<this->formation<<" avec "<<this->nbNotes<<" notes [";
    for (int i = 0; i < this->nbNotes-1; i++){
        s << this->notes[i] << " ; ";
    }
    s << this->notes[nbNotes-1] << "]";
    return s; 
    }

    string getFormation() const {
      return this->formation;
    }

    int getNbNotes() const {
      return this->nbNotes;
    }

    void ajouterNote(float n) {
        this->notes.put(this->nbNotes, n);
        this->nbNotes+=1;
    }

    float getMoyenne() const{
        float somme = 0;
        for (int i = 0; i < this->nbNotes; i++){
            somme+=notes.get(i);
        }
        return somme / this->nbNotes;
    }
};

ostream & operator <<(ostream &s, const Etudiant &etu) {
  return etu.affiche(s); 
}

int main(){
    Etudiant etu("Tom", "Martin", 20, "CAP");
    etu.ajouterNote(12.0);
    etu.ajouterNote(15.0);
    etu.ajouterNote(17.5);
    etu.ajouterNote(14.0);
    etu.ajouterNote(19.0);
    cout << etu << endl;
    cout << "moyenne : ";
    cout << etu.getMoyenne() << endl; 
}