#include<iostream>
#include<string>
using namespace std ; 

/*
Complétez les codes
Testez le main pour les instructions qui vous paraissent correctes
commentez et expliquez ce qui ne vous parait pas correct 
 */ 


class Couple {
  int x, y;
public :
  Couple(int x = 0, int y = 0) : x(x), y(y) {}

  int operator [](int i) const {
    if (i == 0){
      return this->x;
    }else{
      if (i == 1){
        return this->y;
      }else{
        string s = "L'indice est incorrect";
        throw s;
      }
    }
  } 

  int & operator [](int i) {
    if (i == 0){
      return this->x;
    }else{
      if (i == 1){
        return this->y;
      }else{
        string s = "L'indice est incorrect";
        throw s;
      }
    }
  } 

  ostream & affiche(ostream &s) const {
    s<<"("<<this->x<<","<<this->y<<")"; 
    return s; 
  }	  

  ~Couple() {cout<<" detruit Couple "<<endl; }
}; 

ostream & operator <<(ostream &s, const Couple &couple) {
  return couple.affiche(s);
}

class Triplet : public Couple {

int x, y, z;
  
public :
  Triplet(int x=0, int y=0, int z=0) : x(x), y(y), z(z) {}
  
  int operator [](int i) const {
    if (i == 0){
      return this->x;
    }else{
      if (i == 1){
        return this->y;
      }else{
        if (i == 2){
          return this->z;
        }else{
          string s = "L'indice est incorrect";
          throw s;
        }
      }
    }
  }  

  int & operator [](int i) {
    if (i == 0){
      return this->x;
    }else{
      if (i == 1){
        return this->y;
      }else{
        if (i == 2){
          return this->z;
        }else{
          string s = "L'indice est incorrect";
          throw s;;
        }
      }
    }
  }   

  ostream & affiche(ostream &s) const {
    s<<"("<<this->x<<","<<this->y<<","<<this->z<<")"; 
    return s; 
  } 

  ~Triplet() {cout<<" detruit Triplet "; }
}; 

ostream & operator <<(ostream &s, const Triplet &triplet) {
  return triplet.affiche(s);
}


int main() {
  Couple c1(5, -2), c2(6, 3);
  try
  {
    cout << c1[5] << endl;
  }
  catch(string s)
  {
    cout << s << endl;
  }
  Triplet t1(6, 8, 2), t2(-1, -2, -3);
  cout<<"c1 : "<<c1<<" c2 : "<<c2<<" t1 : "<<t1<<" t2 : "<<t2<<endl;
  try
  {
    cout << t1[5] << endl;
  }
  catch(string s)
  {
    cout << s << endl;
  }
  c1 = t1;
  cout<<"c1 : "<<c1<<" t1 : " <<t1<<endl;
  // 
  //t1 = c1; 
  try
  {
    cout<<" c1[3] : "<<c1[3]<<endl;
  }
  catch(string s)
  {
    cout << s << endl;
  }
  
  // 
  
  t1[3] = 11;
  cout<<"t1 : "<<t1<<endl;
  // 
  Couple * c1P = new Couple(4, -4);
  cout<<"*c1P : "<<*c1P<<endl; 
  // 
  c1P = new Triplet(2, -2, 0);
  cout<<"*c1P : "<<*c1P<<endl; 
  // 
try
  {
    cout<<"(*c1P)[3] : "<<(*c1P)[3]<<endl; 
  }
  catch(string s)
  {
    cout << s << endl;
  }
  
  // Triplet * t1P = new Triplet(4, -4, 12);
  // cout<<"*t1P : "<<*t1P<<endl; 
  // // 

  // //t1P = new Couple(12, -24);
  // cout<<"*t1P "<<*t1P<<endl;
  // // 

}
