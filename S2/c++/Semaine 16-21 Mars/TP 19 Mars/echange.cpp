#include<iostream>
using namespace std;


void echange1(int a, int b){
	int c;
	c=a;
	a=b;
	b=c;
	cout << a << " " << b << endl;
}

void echange2(int &a, int &b){
	int c;
	c=a;
	a=b;
	b=c;
	//cout << a << " " << b << "  ";
}

void echange3(int &a, int b){
	int c;
	c=a;
	a=b;
	b=c;
	cout << a << " " << b << endl;
}

void echange4(int a, int &b){
	int c;
	c=a;
	a=b;
	b=c;
	cout << a << " " << b << endl;
}

void tri3 (int &a, int &b, int &c){
	if (a > b){
		echange2(a,b);
	}
	if (a > c){
		echange2(a,c);
	}
	if (b > c){
		echange2(b,c);
	}
}


int main(){
	int nb1, nb2;
	nb1=10;
	nb2=20;
	
	//echangei(nb1, nb2);
	//cout << nb1 << " " << nb2 << endl;

	int min = 67, interm = 99, max = -34;
	tri3 (min, interm, max);
	cout << "minimum : " << min << endl;
	cout << "maximum : " << max << endl;
	cout << "intermediaire : " << interm << endl;
}
