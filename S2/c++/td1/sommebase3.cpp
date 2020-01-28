#include <iostream>
using namespace std;
#include <math.h> 

int somme (int nb1, int nb2){
    int res = 0, retenue = 0, puissance = 0, aux = 0;
    if (nb1 == 0){
        res = nb2;
    }else {
        if (nb2 == 0){
            res = nb1;
        }else{
            while (nb1 != 0 and nb2 != 0){
                aux = retenue + nb1%10 + nb2%10;
                if (aux >= 3){
                    retenue = 1;
                    aux = aux%3;
                }else{
                    retenue = 0;
                }
                res += aux * pow(10,puissance);
                puissance++;
                nb1 = nb1/10;
                nb2 = nb2/10;
            }
            while (nb1 != 0){
                aux = retenue + nb1%10;
                if (aux >= 3){
                    retenue = 1;
                    aux = aux%3;
                }else{
                    retenue = 0;
                }
                res += aux * pow(10,puissance);
                puissance++;
                nb1 = nb1/10;
            }
            while (nb2 != 0){
                aux = retenue + nb2%10;
                if (aux >= 3){
                    retenue = 1;
                    aux = aux%3;
                }else{
                    retenue = 0;
                }
                res += aux * pow(10,puissance);
                puissance++;
                nb2 = nb2/10;
            }
            if (retenue == 1){
                res += 1 * pow(10, puissance);
            }
        }
    }
    return res;
}

int main (){
    int nb1, nb2;
    cout << "Entrez le premier nombre : ";
    cin >> nb1;
    cout << "Entrez le second nombre : ";
    cin >> nb2;
    cout << somme(nb1, nb2) << endl;
}