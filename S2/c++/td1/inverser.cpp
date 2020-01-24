#include <iostream>
using namespace std;
#include<string>

int inverser(int nbr) {
    int NbrInverse = 0;
    while (nbr != 0){
        NbrInverse = NbrInverse * 10;
        NbrInverse = NbrInverse + nbr%10;
        nbr = nbr/10;
    }
    return NbrInverse;
}

int main (){
    cout << inverser(123456789) << endl;
    return 0;
}