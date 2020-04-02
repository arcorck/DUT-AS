#include<iostream>
using namespace std;

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
	
	void put(int i, float val){
		if(i< this->taille && i >=0){
		    this->tab[i]=val;
		}
		else{
			throw(string("out of range"));
		}
	}
	
	float get(int i){
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


void fonctionTab(Tablo t1){
	cout << "Dans ma fonction " << endl;
}



int main(){
  
  Tablo tab1(10);
  cout << tab1.toString() << endl;
  // tableau de taille : 10[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ]
  
  tab1.put(5, 12.5);
  //cout << tab1.toString() << endl;
  
  Tablo tab2(tab1);
  //cout << tab2.toString() << endl;
  
  tab2.put(1, 11);
  tab1.put(1, 25);
  cout << tab1.toString() << endl;
  //cout << tab2.toString() << endl;

  cout << "taille du tableau tab1 : " << tab1.size() << endl;
  tab1.doubleTaille();
  cout << tab1.toString() << endl;
  cout << "taille du tableau tab1 : " << tab1.size() << endl;

  tab1 = tab2;
  tab1.put(0,125);
  cout << tab1.toString() << endl;
  cout << tab2.toString() << endl;

  cout << tab1[8] << endl;
  tab1[8] = 18;
  cout << tab1[8] << endl;

  return 0;
}

