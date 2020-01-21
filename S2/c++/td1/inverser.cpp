#include <iostream>
using namespace std;
#include <math.h> 

int nombre_chiffre (int nb){
    int res(0);
    res = 0;
    while (nb / 10 != 0){
        res += 1;
        nb = nb / 10;
    }
    return res;
}

int inverser(int nb) {
    int inverse(0);
    int indice(0);
    int nb_chiffre(0);
    nb_chiffre = nombre_chiffre(nb);
    indice = 0;
    while (nb_chiffre >= 0){
        inverse = inverse +  ((nb * pow(10, (nb_chiffre * (-1)))) * pow(10, indice));
        nb_chiffre --;
        cout << "nombre avant : " << endl;
        cout << nb << endl;
        nb = nb - (nb * pow(10, (nb_chiffre * (-1))));
        cout << "nombre apres : " << endl;
        cout << nb << endl;
        indice++;
    }
    return inverse;
}

int main (){
    cout << inverser(2354) << endl;
    return 0;
}