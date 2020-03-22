#include <iostream>
#include<string>
using namespace std;

int main(){
    int nbr = 12345;
    int NbrInverse = 0;
    while (nbr != 0){
        NbrInverse = NbrInverse * 10;
        NbrInverse = NbrInverse + nbr%10;
        nbr = nbr/10;
    }
    cout << NbrInverse <<endl;
    int * i;
    *i = 12;
    cout << i <<endl;
    return 0;
}