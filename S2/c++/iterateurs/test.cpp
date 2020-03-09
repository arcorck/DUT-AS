#include <iostream>
#include <list>
using namespace std;

int main(){
    list<int> listentiers;
    list<int>::iterator it;

    int i = 0;

    while (i<10){
        listentiers.push_back(i);
        i++;
    }

    for (it = listentiers.begin(); it != listentiers.end(); ++it){
        cout << *it << endl;
    }
    return 0;
}

