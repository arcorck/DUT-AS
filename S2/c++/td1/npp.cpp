#include <iostream>
using namespace std;

bool premier(int n) {
    if (n <= 1){
        return false;
    }
    if (n == 2){
        return true;
    }
    for (int i = 2; i < n; i++){
        if (n % i == 0){
            return false;
        }
    }
    return true;
}

bool parfait (int n){
    int somme = 1;
    if (n <= 1){
        return false;
    }
    for (int i = 2; i < n; i++){
        if (n % i == 0){
            somme += i;
        }
    }
    return (somme == n);
}

int main(){
    int n;
    cout << "Entrez un nombre pour vérifier s'il est parfait : ";
    cin >> n;
    if (premier(n)){
        cout << n << " est un nombre premier !!"<<endl;
    }else{
        cout << n << " n'est pas un nombre premier !!"<<endl;
    }
    cout<<endl;
    cout << "Les nombres parfaits jusqu'à 100 sont : ";
    for (int n = 1; n <= 100; n++){
        if (parfait(n)){
            cout << n << " " ;
        }
    }
    cout << endl;
    return 0;
}