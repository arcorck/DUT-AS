#include <iostream>
#include <string>
#include <list>
#include <vector>
using namespace std;


class Plante {
    private :

        string nom,couleur;
        int taille;
    
    public :

        Plante(string nom="?", int taille=0,string couleur="Vert")
        {
            this->couleur = couleur;
            this->nom = nom;
            this->taille = taille;
        }

        int getTaille()
        {
            return this->taille;
        }
        string getCouleur()
        {
            return this->couleur;
        }
        string getNom()
        {
            return this->nom;
        }
        
        void setTaille(int taille){
            this->taille=taille;
        }
        void setCouleur(string couleur){
            this->couleur = couleur;
        }

        string toString()
        {
            return "La plante "+this->nom+ " est de taille "+to_string(this->taille) +" cm et est de couleur " + this->couleur  +"\n";
        }
};

ostream & operator <<(ostream & s, Plante plante){
    s<<plante.toString();
    return s;
}

class Herbier{
    vector<Plante> mesPlantes;
    public:
        
        void add(Plante plante){
            this->mesPlantes.push_back(plante);
        }
        
        string toString(){
            string res = "";
            for(Plante pl:this->mesPlantes){
                res += pl.toString();
            }
            return res;
        }

        Plante plusPetite(){
            int tailleMini = this->mesPlantes[0].getTaille();
            Plante plante = this->mesPlantes[0];

            for(int i=0; i<this->mesPlantes.size();++i)
            {
                if(this->mesPlantes[i].getTaille() < tailleMini)
                {
                    tailleMini = this->mesPlantes[i].getTaille();
                    plante = this->mesPlantes[i];
                }
            }
            return plante;
        }

        
        void trierHerbierParTaille(){

        }
};

ostream & operator <<(ostream & s, Herbier plantes){
    s<<plantes.toString()<<endl;
    return s;
}

int main() {
    Plante plante1 ("Tulipe",15,"Orange");
    Plante plante2 ("Rose",11,"Noire");
    Plante plante3 ("Coquelicot",9,"Rouge");
    Plante plante4 ("Pissenlit",5,"Jaune");
    Plante plante5 ("Ibiscus",20,"Violette");
    Plante plante6 ("Edelweiss",7,"Blanche");
    Plante plante7 ("Marguerite",6,"Jaune");
    Plante plante8 ("Iris",14,"Violette");

    cout << plante1 << plante2 << plante3 << endl; 
    plante1 = plante2;
    plante2.setTaille(85);
    cout << plante2 << endl;
    Plante * pp1;
    pp1 = new Plante("Navet",10,"Violet");

    cout << pp1->toString() << endl;

    cout << *pp1 << endl;
    delete pp1;
    pp1 = new Plante("Rose",100,"Rose");
    cout << *pp1 << endl;


    Herbier herbier1;

    herbier1.add(plante1);
    herbier1.add(plante2);
    herbier1.add(plante3);
    herbier1.add(plante4);
    herbier1.add(plante5);
    herbier1.add(plante6);
    herbier1.add(plante7);
    herbier1.add(plante8);

    cout<<"Mon herbier : \n"<<herbier1<<endl;
    cout<<"La plus petite plante est :\n"<<herbier1.plusPetite()<<endl;
}